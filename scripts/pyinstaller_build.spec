# -*- mode: python -*-

block_cipher = None


a = Analysis([r"..\delethon\__main__.py",
             r"..\delethon\__init__.py",
             r"..\delethon\cmdline_utils.py",
             r"..\delethon\exceptions.py",
             r"..\delethon\constants.py",
             r"..\delethon\metadata.py",
             r"..\delethon\options.py",],
             pathex=[r'C:\Program Files (x86)\Windows Kits\10\Redist\ucrt\DLLs\x64'],
             binaries=[],
             datas=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          icon=r"..\docs\icon\delethon.ico",
          name="delethon",
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          console=True )
