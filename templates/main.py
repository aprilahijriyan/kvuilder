

from glob import glob
from kivy.lang import Builder
from kivymd.app import MDApp

class MainApp(MDApp):
    def get_stylesheets(self):
        

    def load_stylesheets(self):
        for f in glob(self.get_stylesheets()):
            Builder.load_file(f)

    def build(self):
        