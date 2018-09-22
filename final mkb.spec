# -*- mode: python -*-

block_cipher = None


a = Analysis(['final mkb.py'],
             pathex=['C:\\Users\\BITKRUSHER\\Documents\\osu-bongocat\\final mkb'],
             binaries=[],
             datas=[('images/*.png', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
a.datas +=  [('favicon.ico', 'C:\\Users\\BITKRUSHER\\Documents\\osu-bongocat\\favicon.ico', 'DATA')]
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='final mkb',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False,
          icon = 'C:\\Users\\BITKRUSHER\\Documents\\osu-bongocat\\favicon.ico' )
