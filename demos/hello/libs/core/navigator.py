from kivy.uix.screenmanager import ScreenManager, ScreenManagerException
from kivy.clock import Clock

class NavigatorScreen(object):
    """
    Navigator screen kivy.
    """

    def __init__(self, sm):
        assert isinstance(sm, ScreenManager)
        self._sm = sm
        self._history = []
        self._current_index = -1

    def goto(self, screen):
        last_scr = self._sm.current
        try:
            self._sm.current = screen
        except ScreenManagerException:
            return False

        self._history.append(last_scr)
        self._current_index += 1
        return True

    def back(self, fresh=True):
        try:
            screen = self._history.pop(self._current_index)
        except IndexError:
            return False

        screen = self._sm.get_screen(screen)
        if fresh:
            Clock.schedule_once(lambda x: self._sm.remove_widget(screen), 0)
            screen = type(screen)()
            self._sm.add_widget(screen)

        self._sm.current = screen.name
        self._current_index -= 1
        return True
