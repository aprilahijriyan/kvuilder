import os
import sys
import traceback

from libs.core.setup import init

init()

try:
    import kivy
    kivy.require('1.11.1')

    from kivy.config import Config
    Config.set("kivy", "log_enable", 0)
    Config.set('kivy', 'keyboard_mode', 'system')
    Config.set('kivy', 'exit_on_escape', "0")
    Config.set('graphics', 'multisamples', '0')
    Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

except Exception:
    traceback.print_exc()
    sys.exit(1)


def main():
    '''
    Fungsi utama untuk menjalankan kivy application
    '''
    
    app = None
    try:
        from hello_kivy import MainApp
        app = MainApp()
        app.run()

    except Exception:
        print(traceback.format_exc())
        if app is not None:
            app.stop()

    sys.exit(1)

if __name__ in ('__main__', '__android__'):
    main()
