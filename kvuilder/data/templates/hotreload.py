from argparse import ArgumentParser, ArgumentError
import os
from kivy.lang import Builder

from kivymd.app import MDApp

KV = """
#:import KivyLexer kivy.extras.highlight.KivyLexer
#:import HotReloadViewer kivymd.utils.hot_reload_viewer.HotReloadViewer


BoxLayout:

    CodeInput:
        id: code
        lexer: KivyLexer()
        style_name: "native"
        on_text: app.update_kv_file(self.text)
        size_hint_x: .7

    HotReloadViewer:
        size_hint_x: .3
        path: app.path_to_kv_file
        errors: True
        errors_text_color: 1, 1, 0, 1
        errors_background_color: app.theme_cls.bg_dark
"""


class HotReloadApp(MDApp):
    path_to_kv_file = "kv_file.kv"

    def build(self):
        self.theme_cls.theme_style = "Dark"
        screen = Builder.load_string(KV)
        code = screen.ids.code
        with open(self.path_to_kv_file) as fp:
            data = fp.read()
            code.text = data

        return screen

    def update_kv_file(self, text):
        with open(self.path_to_kv_file, "w") as kv_file:
            kv_file.write(text)


def main():
    parser = ArgumentParser(
        usage="python3 %(prog)s <filepath>", description="HotReload Kivy (md)"
    )
    try:
        parser.add_argument("filepath", help="File path")
    except ArgumentError as err:
        parser.error(err)

    args = parser.parse_args()
    filepath = args.filepath
    if not os.path.isfile(filepath):
        try:
            with open(filepath, "w") as fp:
                pass
        except Exception as e:
            parser.error(e)

    app = HotReloadApp()
    app.path_to_kv_file = filepath
    app.run()


if __name__ == "__main__":
    main()
