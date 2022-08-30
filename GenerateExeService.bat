@echo off
echo Checking project dependencies ...
pip install -r service\requirements.txt
echo Checking pyinstaller ...
pip install pyinstaller
if errorlevel 1 pause && exit /b
echo Generating JumpRanking_service.exe ...
pyinstaller --onefile --icon "Z:\Captura\Documentacion\Recursos graficos\Logos STT\LogoSTT.ico" --name JumpRanking_service service/jumprankingAPI_main.py
echo File generated in dist folder!
pause
