from kivy.factory import Factory

def registers():
    r = Factory.register
    r("ThreeLineAvatarIconListItem", module="libs.components.wizard")
    r("MDSwiperManager", module="libs.components.wizard")
    r("MDSwiperPagination", module="libs.components.wizard")
