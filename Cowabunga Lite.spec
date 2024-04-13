# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import copy_metadata

datas = [('file_folders/', './file_folders')]
datas += copy_metadata('pyimg4')


a = Analysis(
    ['main_app.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=['ipsw_parser', 'zeroconf', 'pyimg4', 'zeroconf._utils.ipaddress', 'zeroconf._handlers.answers', '_cffi_backend'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Cowabunga Lite',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['cowlite.ico'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Cowabunga Lite',
)
app = BUNDLE(
    coll,
    name='Cowabunga Lite.app',
    icon='cowlite.ico',
    bundle_identifier=None,
)
