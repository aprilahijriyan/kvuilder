from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.clock import Clock
from kivy.app import App

class LoginScreen(Screen):
    def do_login(self):
        email = self.ids.email.text
        passw = self.ids.passw.text
        app = App.get_running_app()
        sm = getattr(app, "screen_manager", None)
        if isinstance(sm, ScreenManager):
            main = app.get_main_screen()
            sm.add_widget(main)
            sm.current = "main"
            Clock.schedule_once(lambda x: sm.remove_widget(self), 0.5)
