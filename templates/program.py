import os

from glob import glob
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp

class MainApp(MDApp):
    def __init__(self, **kwds):
        super().__init__(**kwds)
        self.screen_manager = ScreenManager()
        Window.bind(
            on_request_close=self.on_request_close
        )
        Window.softinput_mode = 'below_target'

    def get_stylesheets(self):
        base = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(base, "libs", "stylesheet")
        stylesheets = glob(path + '/**/*.kv')
        return stylesheets

    def load_stylesheets(self):
        for f in self.get_stylesheets():
            Builder.load_file(f)

    def get_wizard_screen(self):
        from libs.screens.wizard.view import WizardScreen
        from libs.components.wizard import 
        
        screen = WizardScreen()

    def get_login_screen(self):
        pass

    def get_main_screen(self):
        pass

    def get_screen(self):
        pass

    def build(self):
        screen = self.get_screen()
        self.screen_manager.add_widget(screen)
        return self.screen_manager

    def on_request_close(self, *args):
        pass
