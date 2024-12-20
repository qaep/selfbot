@echo off
title INTRUSIF SELFBOT V1.0
chcp 65001 >nul
cls
mode 720,400
:main
cls
echo.
echo "                                                                                                                           ___       ,-`."
echo "   _____ _   _ _______ _____  _    _  _____ _____ ______    _____ ______ _      ______ ____   ____ _______             .-~~   ~~-.,-~ _~"
echo "  |_   _| \ | |__   __|  __ \| |  | |/ ____|_   _|  ____|  / ____|  ____| |    |  ____|  _ \ / __ \__   __|          #`           `._-"
echo "    | | |  \| |  | |  | |__) | |  | | (___   | | | |__    | (___ | |__  | |    | |__  | |_) | |  | | | |            .`           _-~."
echo "    | | | . ` |  | |  |  _  /| |  | |\___ \  | | |  __|    \___ \|  __| | |    |  __| |  _ <| |  | | | |            |          _-   |"
echo "   _| |_| |\  |  | |  | | \ \| |__| |____) |_| |_| |       ____) | |____| |____| |    | |_) | |__| | | |            `       _-~     '"
echo "  |_____|_| \_|  |_|  |_|  \_\\____/|_____/|_____|_|      |_____/|______|______|_|    |____/ \____/  |_|        . _-~`. _-~       .'"
echo "                                                                                                               ,-' _,-~`-__   __-'"
echo "                                                                                                              ,.-~`   .    ~~~"
echo.
echo     -----------------------------------------------------------------------------------------------------------------------------------------                                                                  
echo.
echo.
echo discontinued
echo discontinued

echo discontinued
echo discontinued

echo discontinued
echo discontinued

echo discontinued
echo discontinued

echo discontinued
echo discontinued

echo discontinued
echo discontinued

echo discontinued
echo discontinued

echo discontinued
echo discontinued

echo discontinued
echo discontinued

echo discontinued
echo discontinued

echo discontinued
echo discontinued

echo 1. Lancer intrusif selfbot avec la console affichée (py)
echo.
echo 2. Lancer intrusif selfbot sans la console affichée (pyw)
echo.
echo 3. Quitter
echo ============================
set /p choice="Chosis une option (1-3): "
if "%choice%"=="1" goto py
if "%choice%"=="2" goto pyw
if "%choice%"=="3" exit
goto main


:py
goto install
python main.py


:pyw
cls
echo -- INTRUSIF SELFBOT SANS CONSOLE --
echo.
echo.
echo 1. Lancer intrusif selfbot sans la console affichée (pyw)
echo.
echo 2. Arrêter intrusif selfbot sans la console affichée (pyw)
echo.
echo 3. Aller au menu principal
echo ============================
set /p choice="Chosis une option (1-3): "
if "%choice%"=="1" goto pyw1
if "%choice%"=="2" goto pyw2
if "%choice%"=="3" goto main
goto pyw


:pyw1
cls
goto install
start /b pythonw main.py
cls
echo Selfbot lancé sans console
pause
goto main


:pyw2
cls
taskkill /F /pid pythonw.exe
cls
echo Selfbot arrêté
pause
goto main


:install
cls
echo Installation des modules...
python -m pip install discord==1.7.3
python -m pip install asyncio==3.4.3
python -m pip install aiohttp==3.7.4
python -m pip install requests==2.31.0
python -m pip install colorama==0.4.6
python -m pip install discord.py==1.7.3
cls
echo tous les modules ont été installés
pause
cls
