#some basic import

from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.screen import MDScreen


# class
class App(MDApp):
    def build(self):
        # app screen
        screen = MDScreen()

        return screen


if __name__ == '__main__':
    App().run()
