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
import pyrebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

cred = credentials.Certificate("C:/Users/Morad teaha/Downloads/project16-f346d-firebase-adminsdk-rav4x-1d4397cf7b.json")
firebaseConfig = {
    'apiKey': "AIzaSyAxS1KDjH4OQrbw-k050yGJHQ8giCuyFDU",
    'authDomain': "project16-f346d.firebaseapp.com",
    'databaseURL': "https://project16-f346d-default-rtdb.firebaseio.com",
    'projectId': "project16-f346d",
    'storageBucket': "project16-f346d.appspot.com",
    'messagingSenderId': "237946682699",
    'appId': "1:237946682699:web:59b0610e150f5c42b7bcce",
    'measurementId': "G-W8TSC422XT"}
firebase=pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()



New_User_list = ["Username", "Password", "Full Name", "ID", "Date of Birth"]

delete_User_list = [-1, -1, -1, -1, -1, -1]


# this function to add new user to data base(csv file)


# this function check if user is already in data base
class HomeWindo(Screen):
    pass


# class of the main screen see kv file

class RegiWindo(Screen):
    idn = ObjectProperty(None)
    fullname = ObjectProperty(None)
    dob = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def regibtn(self):
        if self.idn.text != '' and self.fullname.text != '' and self.dob.text != '' and self.email.text != '' and self.password.text != '':
            try:
                New_User_list[0] = self.email.text
                New_User_list[1] = self.password.text
                New_User_list[2] = self.fullname.text
                New_User_list[3] = self.idn.text
                New_User_list[4] = self.dob.text
                user=auth.create_user_with_email_and_password(self.email.text,self.password.text)
                print("account created successfully")
            except:
                invalidForm()

        pass


# register screen take user input and check if its empty or in data base then store it

class Loginwindo(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def logbtn(self):
        try:
            login = auth.sign_in_with_email_and_password(self.email.text, self.password.text)
            if str(self.email.text) == str("morad@test.com"):
                print("is Manager")
                AccessGrant = 0
                WM.current = "MangerLog"
            else:
                print("Normal User")
                AccessGrant = 0
                WM.current = "UserPage"
        except:
            invalidinFormation()

            pass


# login screen recive user input and verfy it


class MangerLog(Screen):
    pass


# Manger screen unfinshed bulid in kv file

class MangerDuser(Screen):
    userid = ObjectProperty(None)
    pass


# delete user screen unfinshed

class WindowManger(ScreenManager):
    pass


# page Manger
class UserPage(Screen):
    pass


kv = Builder.load_file("mainapp.kv")
WM = WindowManger()
screens = [HomeWindo(name="Home"), RegiWindo(name="Register"), Loginwindo(name="Login"), MangerLog(name="MangerLog"),
           MangerDuser(name="MangerDuser"), UserPage(name="UserPage")]
for screens in screens:
    WM.add_widget(screens)


# List of screens in kv file

def invalidForm():
    pop = Popup(title='Invalid Form', content=Label(text='This Email already exist'),
                size_hint=(None, None), size=(400, 400))
    pop.open()


def invalidinFormation():
    pop = Popup(title='Invalid info', content=Label(text='invalid email or password'),
                size_hint=(None, None), size=(400, 400))
    pop.open()


# pop up massage for ivalid input

class SchoolApp(App):
    def build(self):
        return WM


if __name__ == '__main__':
    SchoolApp().run()
