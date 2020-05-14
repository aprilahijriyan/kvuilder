from libs.core.env import init_environment
from libs.core.factory import init_factory
from libs.core.path import init_base_path

def init():
    init_base_path()
    init_environment()
    init_factory()
