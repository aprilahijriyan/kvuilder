import json
from kivy.factory import Factory

def init_factory():
    r = Factory.register
    with open("components.json") as fp:
        components = json.load(fp)
        for module, classes in components.items():
            for cls in classes:
                r(cls, module=module)
