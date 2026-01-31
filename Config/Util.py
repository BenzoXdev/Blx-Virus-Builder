# Copyright (c) BLX - Virus Builder standalone
# Utilitaires minimaux pour Virus Builder

from .Config import *
try:
    import colorama
    import ctypes
    import subprocess
    import os
    import time
    import sys
    import datetime
    import requests
except Exception as e:
    print(f'Modules requis non installés. Lancez "pip install -r requirements.txt". Erreur: {e}')
    input("Appuyez sur Entrée pour quitter.")
    sys.exit(1)

color_webhook = 0xa80505
username_webhook = name_tool
avatar_webhook = 'https://zupimages.net/up/26/05/ip7u.png'
avatar_creator = 'https://avatars.githubusercontent.com/u/210432555?s=400&u=34330c3f5ce30c15197ac99efbe1d10f3b711278&v=4'

color = colorama.Fore
red = color.RED
white = color.WHITE
green = color.GREEN
reset = color.RESET
blue = color.BLUE
yellow = color.YELLOW

try:
    username_pc = os.getlogin()
except Exception:
    username_pc = "username"

try:
    if sys.platform.startswith("win"):
        os_name = "Windows"
    elif sys.platform.startswith("linux"):
        os_name = "Linux"
    else:
        os_name = "Unknown"
except Exception:
    os_name = "None"

# Racine du dossier "Virus Builder" (parent du dossier Config)
tool_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def current_time_hour():
    return datetime.datetime.now().strftime('%H:%M:%S')

BEFORE = f'{red}[{white}'
AFTER = f'{red}]'
BEFORE_GREEN = f'{green}[{white}'
AFTER_GREEN = f'{green}]'

INFO = f'{BEFORE}!{AFTER} |'
ERROR = f'{BEFORE}x{AFTER} |'
ADD = f'{BEFORE}+{AFTER} |'
WAIT = f'{BEFORE}~{AFTER} |'

def Title(title):
    if os_name == "Windows":
        ctypes.windll.kernel32.SetConsoleTitleW(f"{name_tool} {version_tool} - {title}")
    elif os_name == "Linux":
        sys.stdout.write(f"\x1b]2;{name_tool} {version_tool} - {title}\x07")

def Continue():
    input(f"{BEFORE + current_time_hour() + AFTER} {INFO} Appuyez sur Entrée pour continuer -> " + reset)

def Reset():
    """Relance Virus-Builder.py (outil standalone)."""
    if os_name == "Windows":
        subprocess.run([sys.executable, os.path.join(tool_path, "Virus-Builder.py")])
    else:
        subprocess.run([sys.executable, os.path.join(tool_path, "Virus-Builder.py")])
    sys.exit(0)

def Error(e):
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Erreur: {white}{e}{reset}")
    Continue()
    Reset()

def ErrorModule(e):
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Erreur module: {white}{e}{reset}")
    Continue()
    Reset()

def Slow(text):
    delai = 0.03
    for ligne in text.split('\n'):
        print(ligne)
        time.sleep(delai)

def MainColor(text):
    start_color = (168, 5, 5)
    end_color = (255, 118, 118)
    num_steps = 9
    colors = []
    for i in range(num_steps):
        r = start_color[0] + (end_color[0] - start_color[0]) * i // (num_steps - 1)
        g = start_color[1] + (end_color[1] - start_color[1]) * i // (num_steps - 1)
        b = start_color[2] + (end_color[2] - start_color[2]) * i // (num_steps - 1)
        colors.append((r, g, b))
    colors += list(reversed(colors[:-1]))
    gradient_chars = '┴┼┘┤└┐─┬├┌└│]░▒░▒█▓▄▌▀()'

    def TextColor(r, g, b):
        return f"\033[38;2;{r};{g};{b}m"

    lines = text.split('\n')
    num_colors = len(colors)
    result = []
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char in gradient_chars:
                color_index = (i + j) % num_colors
                c = colors[color_index]
                result.append(TextColor(*c) + char + "\033[0m")
            else:
                result.append(char)
        if i < len(lines) - 1:
            result.append('\n')
    return ''.join(result)

def MainColor2(text):
    start_color = (168, 5, 5)
    end_color = (255, 118, 118)
    num_steps = 9
    colors = []
    for i in range(num_steps):
        r = start_color[0] + (end_color[0] - start_color[0]) * i // (num_steps - 1)
        g = start_color[1] + (end_color[1] - start_color[1]) * i // (num_steps - 1)
        b = start_color[2] + (end_color[2] - start_color[2]) * i // (num_steps - 1)
        colors.append((r, g, b))
    colors += list(reversed(colors[:-1]))

    def TextColor(r, g, b):
        return f"\033[38;2;{r};{g};{b}m"

    lines = text.split('\n')
    num_colors = len(colors)
    result = []
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            color_index = (i + j) % num_colors
            c = colors[color_index]
            result.append(TextColor(*c) + char + "\033[0m")
        if i < len(lines) - 1:
            result.append('\n')
    return ''.join(result)

def CheckWebhook(webhook):
    try:
        response = requests.get(webhook)
        if response.status_code in (200, "200"):
            return True
        return False
    except Exception:
        return None

virus_banner = MainColor2(r"""
                                                         ...                                       
                                                  +%@@@@@@@@@@@@@*.                                
                                               #@@@@@@@@@@@@@@@@@@@@@:                             
                                             %@@@@@@@@@@@@@@@@@@@@@@@@@:                           
                                           .@@@@@@@@@@@@@@@@@@@@@@@@@@@@:                          
                                           :@@@@@@@@@@@@@@@@@@@@@@@@@@@@%                          
                                           =@@@@@@@@@@@@@@@@@@@@@@@@@@@@%                          
                                           :@@@@@@@@@@@@@@@@@@@@@@@@@@@@*                          
                                            #@@@%.     .@@@@+      #@@@%                           
                                             +@@=      .@@@@=      .@@#                            
                                              @@@@%%%@@@@%*@@@@%%%@@@@=                            
                                             .@@@@@@@@@@*  -@@@@@@@@@@=                            
                                           .    .::-@@@@@@@@@@@@+::.    .                          
                                         *@@@@#     @@@@@@@@@@@@-    +@@@@@.                       
                                         #@@@@@%    -%@@@@@@@@%=.   *@@@@@@:                       
                                       @@@@@@@@@@@@:            .#@@@@@@@@@@@-                     
                                       +@@@@@*#@@@@@@@@*:  .+@@@@@@@@%*%@@@@#                      
                                                    *@@@@@@@@@@%.                                  
                                        .==.    .+%@@@@@@@%@@@@@@@+:     :=:                       
                                       @@@@@@@@@@@@@@*.       :@@@@@@@@@@@@@@=                     
                                       -@@@@@@@@%=                :#@@@@@@@@*                      
                                         *@@@@@:                     %@@@@@:                       
                                         :%@@%.                       *@@@=                       
""")
