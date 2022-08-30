@echo off
echo Checking project dependencies ...
pip install -r sender\requirements.txt
echo Checking pyinstaller ...
pip install pyinstaller
if errorlevel 1 pause && exit /b
echo Generating JumpRanking_sender.exe ...
pyinstaller --onefile --windowed --icon "Z:\Captura\Documentacion\Recursos graficos\Logos STT\LogoSTT.ico" --name JumpRanking_sender sender/jumpranking-sender.py
echo File generated in dist folder!
pause
