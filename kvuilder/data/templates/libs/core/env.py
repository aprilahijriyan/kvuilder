import os

from kivy.utils import platform

def init_environment():
    os.environ["KIVY_NO_CONSOLELOG"] = "1"
    os.environ["KIVY_NO_CONFIG"] = "1"
    os.environ["KIVY_NO_ENV_CONFIG"] = "1"
    
    if platform == "win":
        os.environ["USE_OPENGL_MOCK"] = "0"
        os.environ["KIVY_GL_BACKEND"] = "angle_sdl2"