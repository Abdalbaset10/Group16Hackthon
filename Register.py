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

New_User_list = ["ID", "Username", "Password", "Title"]





delete_User_list = [-1, -1, -1, -1]


def new_user():
    with open('data.csv', 'a') as data_file:
        writer = csv.writer(data_file)
        writer.writerow(New_User_list)
        data_file.flush()


def find_user(person):
    find_user_flag = 0
    with open('data.csv', 'r') as data_file:
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
        self.add_widget(Label(text="ID: "))
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)

        self.add_widget(Label(text="Username: "))
        self.Username = TextInput(multiline=False)
        self.add_widget(self.Username)

        self.add_widget(Label(text="Password: "))
        self.Password = TextInput(multiline=False)
        self.add_widget(self.Password)

        self.add_widget(Label(text="Title: "))
        self.Title = TextInput(multiline=False)
        self.add_widget(self.Title)

        self.submit = Button(text="Register", font_size=25)
        self.submit.bind(on_press=self.create_user)
        self.add_widget(self.submit)

    def create_user(self,instance):

        New_User_list[0] = self.name.text

        if find_user(New_User_list[0]) == 0:

            New_User_list[1] = self.Username.text

            New_User_list[2] = self.Password.text

            New_User_list[3] = self.Title.text

            new_user()
        else:
            print("already registered")


class MyWidget(App):
    def build(self):
        return Grids()


MyWidget().run()

New_User_list = [1, 2, 3, 4]

delete_User_list = [-1, -1, -1, -1]
