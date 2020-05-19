from kivy.lang import Builder
from kivy.clock import Clock
from kivy.properties import StringProperty
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout

Builder.load_string("""
<ContentInfoMessageBox>:
    cols: 2
    adaptive_height: True
    size_hint_x: None
    width: dp(150)

    AnchorLayout:
        anchor_x: "left"
        anchor_y: 'top'

        Image:
            id: icon
            size_hint: None, None
            size: dp(56), dp(56)
            source: 'assets/images/icons8-info-48.png'

    AnchorLayout:
        anchor_x: 'left'
        anchor_y: 'top'

        ScrollableLabel:
            size_hint: None, None
            size: dp(450), dp(80)
            text: root.text

<ContentErrorMessageBox>:
    cols: 2
    adaptive_height: True
    size_hint_x: None
    width: dp(150)

    AnchorLayout:
        anchor_x: "left"
        anchor_y: 'top'

        Image:
            id: icon
            size_hint: None, None
            size: dp(46), dp(46)
            source: 'assets/images/icons8-error-64.png'

    AnchorLayout:
        anchor_x: 'left'
        anchor_y: 'top'

        ScrollableLabel:
            size_hint: None, None
            size: dp(450), dp(80)
            text: root.text

<ContentWarningMessageBox>:
    cols: 2
    adaptive_height: True
    size_hint_x: None
    width: dp(150)

    AnchorLayout:
        anchor_x: "left"
        anchor_y: 'top'

        Image:
            id: icon
            size_hint: None, None
            size: dp(56), dp(56)
            source: 'assets/images/icons8-warning-48.png'

    AnchorLayout:
        anchor_x: 'left'
        anchor_y: 'top'

        ScrollableLabel:
            size_hint: None, None
            size: dp(450), dp(80)
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
        content = kwargs.pop("content", None)
        if content:
            kwargs["type"] = "custom"
            kwargs["content_cls"] = content

        super().__init__(**kwargs)

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
