import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.config import Config
from kivy.uix.relativelayout import RelativeLayout

import Register

class Widgets(GridLayout):
    def __init__(self):
        self.submit = Button(text="Register", font_size=25)
        self.submit.bind(on_press= Register.register)
        self.add_widget(self.submit)






class HomePage(App):
    def build(self):
        return Widgets()



HomePage().run()