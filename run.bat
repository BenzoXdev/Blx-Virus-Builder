@echo off
cd /d "%~dp0"
python Virus-Builder.py
if errorlevel 1 pause
