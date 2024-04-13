from sys import platform

import PyInstaller.__main__

args = [
    'main_app.py',
    '--hidden-import=ipsw_parser',
    '--hidden-import=zeroconf',
    '--hidden-import=pyimg4',
    '--hidden-import=zeroconf._utils.ipaddress',
    '--hidden-import=zeroconf._handlers.answers',
    '--hidden-import=_cffi_backend',
    '--add-data=file_folders/:./file_folders',
    '--copy-metadata=pyimg4',
    '--onedir',
    '--name=Cowabunga Lite',
    '--icon=cowlite.ico'
]

if platform == "darwin":
    # add --windowed arg for macOS
    args.append('--windowed')

PyInstaller.__main__.run(args)