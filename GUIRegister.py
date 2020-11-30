import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.config import Config
from kivy.uix.relativelayout import RelativeLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
import csv

New_User_list = ["ID", "Full Name", "Date of Birth", "Username", "Password"]

delete_User_list = [-1, -1, -1, -1, -1, -1]


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


class HomeWindo(Screen):
    pass


class RegiWindo(Screen):
    idn = ObjectProperty(None)
    fullname = ObjectProperty(None)
    dob = ObjectProperty(None)
    username = ObjectProperty(None)
    password = ObjectProperty(None)

    def regibtn(self):
        if self.idn.text != '' and self.fullname.text != '' and self.dob.text != '' and self.username.text != '' and self.password.text != '':
            New_User_list[0] = self.idn.text

            if find_user(New_User_list[0]) == 0:
                New_User_list[0] = self.idn.text
                New_User_list[1] = self.fullname.text
                New_User_list[2] = self.dob.text
                New_User_list[3] = self.username.text
                New_User_list[4] = self.password.text

                new_user()
            print("True")

        else:
            print("False")
            invalidForm()


class Loginwindo(Screen):
    username = ObjectProperty(None)
    password = ObjectProperty(None)

    def logbtn(self):
        grant_access=0
        with open('data.csv', 'r') as data_file:
            usercheck = 0
            passcheck = 0
            for line in data_file:
                data = line.split(",")
                usercheck+=1
                passcheck = usercheck
                if data[3] == str(self.username) and data[4]==str(self.password):
                    grant_access=1
        if grant_access==1:
            pass
        else:
            print("false")




class MangerLog(Screen):
    pass


class MangerDuser(Screen):
    userid = ObjectProperty(None)
    pass


class WindowManger(ScreenManager):
    pass


kv = Builder.load_file("mainapp.kv")
WM = WindowManger()


def invalidForm():
    pop = Popup(title='Invalid Form', content=Label(text='Please fill in all inputs with valid information.'),
                size_hint=(None, None), size=(400, 400))
    pop.open()


class MyMainApp(App):
    def build(self):
        return kv


if __name__ == '__main__':
    MyMainApp().run()
