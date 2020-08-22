from kivy.uix.scrollview import ScrollView
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.properties import StringProperty, BooleanProperty, ObjectProperty
from kivymd.uix.label import MDLabel

Builder.load_string('''
<ScrollableLabel>:
    MDLabel:
        size_hint_y: None
        height: self.texture_size[1]
        text_size: self.width, None
        text: root.text
''')

class ScrollableLabel(ScrollView):
    text = StringProperty('')

class ClickableLabel(MDLabel):
    clickable = BooleanProperty(True)
    callback = ObjectProperty()

    def on_touch_down(self, touch):
        if self.clickable and touch.is_double_tap:
            if callable(self.callback):
                Clock.schedule_once(lambda x: self.callback(self), 0)
        return super().on_touch_down(touch)
