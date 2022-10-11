import PyInstaller.__main__

PyInstaller.__main__.run([
    './game/main.py',
    '--onefile',
    '-n Gentrys Quest',
    '-c',
])