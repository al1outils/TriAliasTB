@echo off
setlocal
cd /d "%~dp0"

echo ==============================================
echo Construction de TriAliasTB v1.0.6
echo Utilisation de l'icone officielle
echo ==============================================
echo.

if not exist "TriAliasTB_v1.0.6.py" (
    echo ERREUR : TriAliasTB_v1.0.6.py est introuvable.
    pause
    exit /b 1
)
if not exist "TriAliasTB_v1.0.6.spec" (
    echo ERREUR : TriAliasTB_v1.0.6.spec est introuvable.
    pause
    exit /b 1
)
if not exist "TriAliasTB.ico" (
    echo ERREUR : TriAliasTB.ico est introuvable.
    echo L'icone officielle est necessaire pour construire l'EXE.
    pause
    exit /b 1
)

python -m PyInstaller --version >nul 2>&1
if errorlevel 1 (
    echo ERREUR : PyInstaller n'est pas disponible dans cet environnement Python.
    echo Installe-le avec : python -m pip install pyinstaller pywin32
    pause
    exit /b 1
)

python -c "import win32com.client" >nul 2>&1
if errorlevel 1 (
    echo ERREUR : pywin32 n'est pas disponible dans cet environnement Python.
    echo Installe-le avec : python -m pip install pyinstaller pywin32
    pause
    exit /b 1
)

echo Suppression des anciens fichiers de compilation...
if exist "build" rmdir /S /Q "build"
if exist "dist" rmdir /S /Q "dist"

echo.
echo Construction en cours avec l'icone officielle...
python -m PyInstaller --clean --noconfirm "TriAliasTB_v1.0.6.spec"
if errorlevel 1 (
    echo.
    echo ECHEC : la construction de l'EXE a echoue.
    pause
    exit /b 1
)

echo.
if exist "dist\TriAliasTB.exe" (
    if exist "dist\TriAliasTB.ico" del /Q "dist\TriAliasTB.ico"
    echo SUCCES : dist\TriAliasTB.exe a ete cree.
    echo Le SPEC utilise TriAliasTB.ico comme icone integree a l'EXE.
    echo Aucun fichier .ico externe n'est necessaire pour l'utilisateur.
    echo.
    echo Si l'Explorateur affiche encore l'ancienne icone, il peut s'agir de son cache.
    echo Verifie le nouvel EXE depuis le dossier dist nettoye avant de reutiliser une ancienne copie.
) else (
    echo ERREUR : la construction semble terminee mais l'EXE est absent.
    pause
    exit /b 1
)

echo.
pause
endlocal
