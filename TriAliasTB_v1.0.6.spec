# -*- mode: python ; coding: utf-8 -*-

import os
from PyInstaller.utils.hooks import collect_submodules

# Toujours prendre le script et l'icône dans le dossier de ce fichier SPEC.
BASE_DIR = os.path.dirname(os.path.abspath(SPEC))
SCRIPT_PATH = os.path.join(BASE_DIR, 'TriAliasTB_v1.0.6.py')
ICON_PATH = os.path.join(BASE_DIR, 'TriAliasTB.ico')

if not os.path.isfile(SCRIPT_PATH):
    raise FileNotFoundError(f'Script introuvable : {SCRIPT_PATH}')
if not os.path.isfile(ICON_PATH):
    raise FileNotFoundError(f'Icone officielle introuvable : {ICON_PATH}')

hidden = collect_submodules('win32com')
hidden += ['pythoncom', 'pywintypes', 'win32timezone']

analysis = Analysis(
    [SCRIPT_PATH],
    pathex=[BASE_DIR],
    binaries=[],
    datas=[(ICON_PATH, '.')],
    hiddenimports=hidden,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(analysis.pure)

exe = EXE(
    pyz,
    analysis.scripts,
    analysis.binaries,
    analysis.datas,
    [],
    name='TriAliasTB',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=ICON_PATH,
)
