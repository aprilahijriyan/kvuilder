import os
import sys

os.environ["KIVY_NO_CONSOLELOG"] = "1"
os.environ["KIVY_NO_CONFIG"] = "1"
os.environ["KIVY_NO_ENV_CONFIG"] = "1"

if sys.platform.startswith("win"):
    os.environ["USE_OPENGL_MOCK"] = "0"
    os.environ["KIVY_GL_BACKEND"] = "angle_sdl2"
