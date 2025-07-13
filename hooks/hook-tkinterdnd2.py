from PyInstaller.utils.hooks import collect_submodules

hiddenimports = collect_submodules('tkinterdnd2')
hiddenimports.append('tkinter.tix')
