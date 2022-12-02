from PyInstaller import __main__

__main__.run([
    '../game/main.py',
    '--onefile',
    '-n Gentrys Quest',
    '-c',
    '--hidden-import Content.Artifacts',
    '--clean',
    '-p ../game',
])