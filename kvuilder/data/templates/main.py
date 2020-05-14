import os
import sys
import traceback

from libs.core.setup import init

init()

try:
    import kivy
    kivy.require('1.9.2')

    from kivy.config import Config
    Config.set('kivy', 'keyboard_mode', 'system')
    Config.set('kivy', 'exit_on_escape', "0")
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
        from ${nama_program} import MainApp
        app = MainApp()
        app.run()

    except Exception:
        traceback.print_exc()
        if app is not None:
            app.stop()

    sys.exit(1)

if __name__ in ('__main__', '__android__'):
    main()
