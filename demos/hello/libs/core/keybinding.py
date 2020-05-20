class Modifiers:
    """
    Diambil dari https://brainly.in/question/10492799.
    """

    CTRL = "ctrl"
    ALT = "alt"
    META = "meta"
    CAPSLOCK = "capslock"
    SHIFT = "shift"

class Key(object):
    def __init__(self, code):
        self.code = code

class KeyCode:
    """
    Diambil dari https://docstore.mik.ua/orelly/webprog/DHTML_javascript/0596004672_jvdhtmlckbk-app-b.html.
    """

    # ALT = Key(18)
    ARROW_DOWN = Key(40)
    ARROW_LEFT = Key(37)
    ARROW_RIGHT = Key(39)
    ARROW_UP = Key(38)
    BACKSPACE = Key(8)
    CAPSLOCK = Key(20)
    # CTRL = Key(17)
    DELETE = Key(46)
    END = Key(35)
    ENTER = Key(13)
    ESC = Key(27)
    F1 = Key(112)
    F2 = Key(113)
    F3 = Key(114)
    F4 = Key(115)
    F5 = Key(116)
    F6 = Key(117)
    F7 = Key(118)
    F8 = Key(119)
    F9 = Key(120)
    F10 = Key(121)
    F11 = Key(122)
    F12 = Key(123)
    NUMPAD_ZERO = Key(96)
    NUMPAD_ONE = Key(97)
    NUMPAD_TWO = Key(98)
    NUMPAD_THREE = Key(99)
    NUMPAD_FOUR = Key(100)
    NUMPAD_FIVE = Key(101)
    NUMPAD_SIX = Key(102)
    NUMPAD_SEVEN = Key(103)
    NUMPAD_EIGHT = Key(104)
    NUMPAD_NINE = Key(105)
    NUMPAD_PLUS = Key(107)
    NUMPAD_MINUS = Key(109)
    NUMPAD_MULTIPLIES = Key(106)
    NUMPAD_DOT = Key(110)
    NUMPAD_DIVIDE = Key(111)
    ZERO = Key(48)
    ONE = Key(49)
    TWO = Key(50)
    THREE = Key(51)
    FOUR = Key(52)
    FIVE = Key(53)
    SIX = Key(54)
    SEVEN = Key(55)
    EIGHT = Key(56)
    NINE = Key(57)
    GRAVE_ACCENT = Key(222)
    MINUS = Key(189)
    COMMA = Key(188)
    DOT = Key(190)

keymaps = {}

if not keymaps:
    for attr in dir(KeyCode):
        val = getattr(KeyCode, attr)
        if isinstance(val, Key):
            keymaps[attr.lower().replace("_", "-")] = val.code

class KeyBinding(object):
    def __init__(self):
        self.handlers = {}

    def add(self, key, handler, modifiers=[]):
        assert isinstance(key, str)
        assert callable(handler)
        assert isinstance(modifiers, list)
        clb = {
            "handler": handler,
            "modifiers": set(modifiers)
        }
        self.handlers[key] = clb

    def translate(self, key):
        return keymaps.get(key)

    def validate(self, keycode, modifiers):
        for key, clb in self.handlers.items():
            handler = clb["handler"]
            mods = clb["modifiers"]
            mod_valid = True
            # verifikasi keyboard modifiers
            if mods and len(modifiers) == len(mods):
                mod_valid = False
                for i in range(len(mods)):
                    if mods[i] == modifiers[i]:
                        mod_valid = True

            if mod_valid:
                key = self.translate(key)
                if key and key == keycode:
                    handler()
                    break
