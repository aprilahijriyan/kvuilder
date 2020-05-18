import os

from glob import glob
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.utils import platform as _os
from kivymd.app import MDApp

class MainApp(MDApp):
    def __init__(self, **kwds):
        super().__init__(**kwds)
        Window.bind(
            on_request_close=self.on_request_close
        )
        Window.softinput_mode = 'below_target'
        self.screen_manager = ScreenManager()

    @property
    def platform(self):
        rv = "mobile" if _os in ("android", "ios") else "desktop"
        return rv

    def get_stylesheets(self):
        path = os.path.join("libs", "stylesheet", self.platform, "**/*.kv")
        stylesheets = glob(path)
        return stylesheets

    def load_stylesheets(self):
        for f in self.get_stylesheets():
            Builder.load_file(f)

    def get_wizard_screen(self):
        from libs.screens.wizard.view import WizardScreen
        from libs.components.wizard import MDSwiperPagination
        
        screen = WizardScreen()
        wizard_manager = screen.ids.wizard_manager
        paginator = MDSwiperPagination()
        paginator.screens = wizard_manager.screen_names
        paginator.manager = wizard_manager
        wizard_manager.paginator = paginator
        screen.add_widget(paginator)
        return screen

    def get_login_screen(self):
        from libs.screens.login.view import LoginScreen

        screen = LoginScreen()
        return screen

    def get_main_screen(self):
        from libs.screens.main.view import MainScreen

        screen = MainScreen()
        return screen

    def get_screen(self):
        raise NotImplementedError

    def build(self):
        self.load_stylesheets()
        screen = self.get_screen()
        self.screen_manager.add_widget(screen)
        return self.screen_manager

    def on_request_close(self, *args):
        return True
