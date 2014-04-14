# -*- mode: python -*-
a = Analysis(['legit.py'],
             pathex=['c:\\Users\\akeem.mclennon\\Documents\\projects\\legit'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='legit.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True )
