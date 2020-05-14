import sys
import os

def is_freeze():
    rv = hasattr(sys, "_MEIPASS")
    return rv

def get_base_path():
    rv = None
    if is_freeze():
        rv = sys._MEIPASS
    else:
        rv = os.getcwd()

    return rv

def join_path(target):
    base = get_base_path()
    rv = os.path.join(base, target)
    return rv

def join_asset_file(*paths):
    base = join_path("assets")
    for f in paths:
        base = join_path(base, f)
    return base
