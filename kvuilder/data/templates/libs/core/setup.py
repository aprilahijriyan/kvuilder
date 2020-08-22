import libs.core.env

from libs.core.factory import init_factory
from libs.core.path import init_base_path

def init():
    init_base_path()
    init_factory()
