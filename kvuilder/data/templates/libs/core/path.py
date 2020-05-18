import os

from libs.core.utils import get_base_path

def init_base_path():
    os.chdir(get_base_path())
