from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.screen import MDScreen

class img(MDApp):
    def build(self):
        screen = MDScreen()

        return screen


if __name__ == '__main__':
    img().run()
