"""
User registeration :
"""
import kivy
import csv
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button

New_User_list = ["ID", "Full Name", "Date of Birth", "Username", "Password"]

delete_User_list = [-1, -1, -1, -1, -1, -1]


def new_user():
    with open('../Newgithub/Group16Hackthon-Morad_Hackthon/data.csv', 'a') as data_file:
        writer = csv.writer(data_file)
        writer.writerow(New_User_list)
        data_file.flush()


def find_user(person):
    find_user_flag = 0
    with open('../Newgithub/Group16Hackthon-Morad_Hackthon/data.csv', 'r') as data_file:
        for line in data_file:
            data = line.split(",")
            if data[0] == str(person):
                find_user_flag = 1
    if find_user_flag == 1:
        return 1
    else:
        return 0


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
        self.submit.bind(on_press=self.create_user)
        self.add_widget(self.submit)

    def create_user(self, instance):

        New_User_list[0] = self.ID.text

        if find_user(New_User_list[0]) == 0:
            New_User_list[0] = self.ID.text
            New_User_list[1] = self.name.text
            New_User_list[2] = self.date_of_birth.text
            New_User_list[3] = self.username.text
            New_User_list[4] = self.password.text

            new_user()
        else:
            pop = Popup(title='already existing', content=Label(text="already existing user"), size=(200, 170))
            pop.open()


class Register(App):
    def build(self):
        return Grids()


def register():
    Register().run()
