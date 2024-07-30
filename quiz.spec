# meu_script.spec

# Importa as funções necessárias
from PyInstaller.utils.hooks import collect_data_files

# Define o nome do seu script
a = Analysis(['quiz.py'],
             pathex=['.'],
             binaries=[],
             datas=[('img/*', 'img')],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             cipher=None,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
          cipher=a.cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='quiz',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          cipher=a.cipher,
          noarchive=False)
