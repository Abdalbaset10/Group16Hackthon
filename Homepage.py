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

class Grids(GridLayout):
    def __init__(self, **kwargs):
        super(Grids, self).__init__(**kwargs)

        self.cols = 1
        self.add_widget(Label(text="Full Name: "))
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)

        self.add_widget(Label(text="ID: "))
        self.ID = TextInput(multiline=False)
        self.add_widget(self.ID)

        self.add_widget(Label(text="Date of birth dd/mm/yyyy: "))
        self.date_of_birth = TextInput(multiline=False)
        self.add_widget(self.date_of_birth)

        self.add_widget(Label(text="Username: "))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)

        self.add_widget(Label(text="Password: "))
        self.password = TextInput(multiline=False)
        self.add_widget(self.password)

        self.submit = Button(text="Register", font_size=25)
       # self.submit.bind(on_press=self.create_user)
        self.add_widget(self.submit)



class Register(App):
    def build(self):
        return Grids()


def regis():
    Register().run()

