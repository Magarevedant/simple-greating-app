# simple-greating-app

Let's get started!

What we are going to do...
 1. Adding logo to our app
 2. Adding greeting label to our app
 3. Adding user name input field
 4. "Great" button 


1. Adding logo
 
First we will add logo to app for that first download the .PNG file from my GitHub account
Then add a code :

from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.screen import MDScreen

class img(MDApp):
    def build(self):
        screen = MDScreen()
        screen.add_widget(Image(source="logo.png")

        return screen


if __name__ == '__main__':
    img().run()

Here we have added a image.

Note: you have to create a file then save .py file to same folder and "logo.png" in same folder too.
