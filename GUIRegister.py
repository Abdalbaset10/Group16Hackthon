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
New_User_list = ["Username", "Password","Full Name" ,"ID" , "Date of Birth"]

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
            New_User_list[0] = self.username.text

            if find_user(New_User_list[0]) == 0:
                New_User_list[0] = self.username.text
                New_User_list[1] = self.password.text
                New_User_list[4] = self.fullname.text
                New_User_list[3] = self.idn.text
                New_User_list[2] = self.dob.text

                new_user()
            print("True")

        else:
            print("False")
            invalidForm()


class Loginwindo(Screen):
    username = ObjectProperty(None)
    password = ObjectProperty(None)

    def logbtn(self):
        AccessGrant = 0
        x=self.username.text
        y=self.password.text
        print(x,y)


        with open('data.csv', 'r') as data_file:
            for line in data_file:
                data = line.split(",")
                if data[0] == str(x):
                     if data[1] == str(y):
                         AccessGrant = 1

        if AccessGrant == 1:
            print("Access Granted")
            if str(self.username.text)==str("Manager"):
                print("is Manager")
                AccessGrant = 0
                WM.current = "MangerLog"
            else:
                print("Normal User")
                AccessGrant = 0
                WM.current="Home"

        else:
            print("Access Denied")
            return False
        pass






class MangerLog(Screen):
    pass


class MangerDuser(Screen):
    userid = ObjectProperty(None)
    pass


class WindowManger(ScreenManager):
    pass


kv = Builder.load_file("mainapp.kv")
WM = WindowManger()
screens=[HomeWindo(name="Home"),RegiWindo(name="Register"),Loginwindo(name="Login"),MangerLog(name="MangerLog"),MangerDuser(name="MangerDuser")]
for screens in screens:
    WM.add_widget(screens)


def invalidForm():
    pop = Popup(title='Invalid Form', content=Label(text='Please fill in all inputs with valid information.'),
                size_hint=(None, None), size=(400, 400))
    pop.open()


class MyMainApp(App):
    def build(self):
        return WM


if __name__ == '__main__':
    MyMainApp().run()
