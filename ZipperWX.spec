# -*- mode: python -*-

block_cipher = None

added_files = [
         ( 'favicon.ico', '.' ),
         ( 'ui', 'ui' )		 
              ]

a = Analysis(['ZipperWX.pyw'],
             pathex=['C:\\DATA\\perso\\PY\\zipper'],
             binaries=None,
             datas=added_files,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='U-Zip',
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='favicon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='U-Zip')
