# -*- mode: python ; coding: utf-8 -*-
a=Analysis(['TriAliasTB_v1.0.4.py'],pathex=[],binaries=[],datas=[('TriAliasTB.ico','.')],hiddenimports=['win32com.client'],hookspath=[],hooksconfig={},runtime_hooks=[],excludes=[],noarchive=False)
pyz=PYZ(a.pure)
exe=EXE(pyz,a.scripts,a.binaries,a.datas,[],name='TriAliasTB',console=False,icon='TriAliasTB.ico')
