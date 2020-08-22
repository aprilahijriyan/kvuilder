# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.building.build_main import *
from kivy import platform
import sys
import os

path = os.path.abspath(".")
sys.path.insert(0, path)

bins = []
if platform == "win":
    from kivy_deps import sdl2, angle
    bins = [Tree(p) for p in (sdl2.dep_bins + angle.dep_bins)]

from kivymd import hooks_path as kivymd_hooks_path

hiddenimports = ["pkg_resources.py2_warn"]

icon = os.path.join("assets", "images", "icon.ico")
stylesheet = os.path.join("libs", "stylesheet")
debug = True

datas = [
    ("assets", "assets"),
    (stylesheet, stylesheet),
    ("components.json", ".")
]
a = Analysis(
    ["main.py"],
    pathex=[path],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[kivymd_hooks_path],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=None)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    *bins,
    debug=debug,
    strip=False,
    upx=False,
    name="hello_kivy",
    console=debug,
    icon=icon
)
