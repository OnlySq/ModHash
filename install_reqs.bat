@ECHO OFF
pip install -r requirements.txt
ECHO "Installed requirements. Start ModHash via start.bat"

DEL "requirements.txt"

@echo @echo off>start.bat
@echo python -m main.py>>start.bat
@echo pause>nul)>>start.bat

DEL "%~f0"