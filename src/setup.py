"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['Redict.py']
DATA_FILES = [
    ('gui', ['gui/About.ui',
             'gui/completer.ui',
             'gui/dicts.ui',
             'gui/History.ui',
             'gui/lookup.ui',
             'gui/Main.ui',
             'gui/icon.png',
             'gui/tbZoomOut.png',
             'gui/tbZoomIn.png',
             'gui/tbQuit.png',
             'gui/tbLookup.png',
             'gui/tbHistory.png',
             'gui/tbCompleter.png',
             'gui/tbAbout.png']
     ),
    ('gui/stylesheets', ['gui/stylesheets/AMOLED.qss']),
    ('database', ['database/dictionaries_db.db'])
]
OPTIONS = {'iconfile': 'gui/icon.icns'}

setup(
    name = 'Redict',
    version = '0.0.1',
    author = 'Reto Wietlisbach',
    author_email = 'rwietlisbach@hotmail.com',
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app', 'setuptools', 'PyQt5', 'pyperclip', 'bs4']
)
