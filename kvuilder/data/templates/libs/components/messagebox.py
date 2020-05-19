from kivy.lang import Builder
from kivy.clock import Clock
from kivy.properties import StringProperty
from kivymd.uix.dialog import MDDialog
from kivymd.uix.gridlayout import MDGridLayout

Builder.load_string("""
<ContentInfoMessageBox>:
    cols: 2
    adaptive_height: True

    MDBoxLayout:
        orientation: 'vertical'
        adaptive_height: True
        height: dp(150)

        FitImage:
            source: 'assets/images/icons8-info-48.png'

    ScrollableLabel:
        text: root.text

<ContentErrorMessageBox>:
    cols: 2
    adaptive_height: True

    MDBoxLayout:
        orientation: 'vertical'
        adaptive_height: True
        height: dp(150)

        FitImage:
            source: 'assets/images/icons8-error-64.png'

    ScrollableLabel:
        text: root.text

<ContentWarningMessageBox>:
    cols: 2
    adaptive_height: True

    MDBoxLayout:
        orientation: 'vertical'
        adaptive_height: True
        height: dp(150)

        FitImage:
            source: 'assets/images/icons8-warning-48.png'

    ScrollableLabel:
        text: root.text

""")

class ContentInfoMessageBox(MDGridLayout):
    text = StringProperty("")

class ContentErrorMessageBox(MDGridLayout):
    text = StringProperty("")

class ContentWarningMessageBox(MDGridLayout):
    text = StringProperty("")

class Message(MDDialog):
    def __init__(self, **kwargs):
        kwargs.setdefault("radius", [15, 15, 15, 15])
        content = kwargs.get("content")
        if content:
            kwargs["type"] = "custom"
            kwargs["content_cls"] = content

        super().__init__(**kwargs)
        # Clock.schedule_once(lambda x: self.open(), 2.5)

class InfoMessage(Message):
    def __init__(self, **kwargs):
        content = ContentInfoMessageBox()
        content.text = kwargs.get("text")
        kwargs["content"] = content
        super().__init__(**kwargs)

class ErrorMessage(Message):
    def __init__(self, **kwargs):
        content = ContentErrorMessageBox()
        content.text = kwargs.get("text")
        kwargs["content"] = content
        super().__init__(**kwargs)

class WarningMessage(Message):
    def __init__(self, **kwargs):
        content = ContentWarningMessageBox()
        content.text = kwargs.get("text")
        kwargs["content"] = content
        super().__init__(**kwargs)
