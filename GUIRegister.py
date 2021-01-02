import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.config import Config
from kivy.uix.scrollview import ScrollView
from kivy.uix.relativelayout import RelativeLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from kivymd.uix.list import MDList,OneLineListItem
import pyrebase



firebaseConfig = {
    'apiKey': "AIzaSyAxS1KDjH4OQrbw-k050yGJHQ8giCuyFDU",
    'authDomain': "project16-f346d.firebaseapp.com",
    'databaseURL': "https://project16-f346d-default-rtdb.firebaseio.com/",
    'projectId': "project16-f346d",
    'storageBucket': "project16-f346d.appspot.com",
    'messagingSenderId': "237946682699",
    'appId': "1:237946682699:web:59b0610e150f5c42b7bcce",
    'measurementId': "G-W8TSC422XT"}
firebase=pyrebase.initialize_app(firebaseConfig)
db=firebase.database()
auth = firebase.auth()
storage=firebase.storage()





def find_user(user):
    users=db.child("users").get()
    userfound=0
    for i in users.each():
        print(str(i.key()))
        if str(user)==str(i.key()):
            userfound=1
    if userfound==1:
        return 1
    else:
        return 0


def grantAccess(username,password):
    users=db.child("users").get()
    grant_Access=0
    for i in users.each():
        if (str(username)==str(i.val()['Username']))and(str(password)==str(i.val()['pass'])):
            grant_Access=1
        if (str(username)==str(i.val()['Username']))and(str(password)!=str(i.val()['pass'])):
            grant_Access=0
    return grant_Access









# this function check if user is already in data base
class HomeWindo(Screen):
    pass


# class of the main screen see kv file

class RegiWindo(Screen):
    idn = ObjectProperty(None)
    fullname = ObjectProperty(None)
    dob = ObjectProperty(None)
    username = ObjectProperty(None)
    password = ObjectProperty(None)

    def regibtn(self):
        if self.idn.text != '' and self.fullname.text != '' and self.dob.text != '' and self.username.text != '' and self.password.text != '':
            if find_user(str(self.idn.text))==0:
                users_data={'Name':self.fullname.text,'IDnum':self.idn.text,'Username':self.username.text,'DOB':self.dob.text,'pass':self.password.text}
                db.child("users").child(str(self.idn.text)).set(users_data)
                if str(self.idn.text) == ("315198564"):
                    db.child("users").child("315198564").update({'Title':'Manager'})
                print("account created successfully")
            else:
                invalidForm()

        pass


# register screen take user input and check if its empty or in data base then store it

class Loginwindo(Screen):
    username = ObjectProperty(None)
    password = ObjectProperty(None)

    def logbtn(self):

        if grantAccess(str(self.username.text),str(self.password.text))==1:
            if str(self.username.text) == str("moradM"):
                print("is Manager")
                AccessGrant = 0
                WM.current = "MangerLog"
            else:
                print("Normal User")
                AccessGrant = 0
                WM.current = "UserPage"
        if grantAccess(str(self.username.text),str(self.password.text))==0 :
            invalidinFormation()

            pass


# login screen recive user input and verfy it


class MangerLog(Screen):
    pass


# Manger screen unfinshed bulid in kv file

class MangerDuser(Screen):
    identity = ObjectProperty(None)
    def deletebtn(self):
        if find_user(str(self.identity.text))==0:
            no_user()
        else:
            db.child("users").child(str(self.identity.text)).remove()
            deletedS()
            WM.current = "MangerLog"
    pass

class MangerMakeTeacher(Screen):
    identity = ObjectProperty(None)
    subject = ObjectProperty(None)
    def MkTeacher(self):
        if find_user(str(self.identity.text))==0:
            no_user()
        else:
            db.child("users").child(str(self.identity.text)).update({'Title':'Teacher'})
            db.child("users").child(str(self.identity.text)).update({'Subject': str(self.subject.text)})
            IsnowTeacher()
            WM.current = "MangerLog"
    pass


class PassReset(Screen):
    identity = ObjectProperty(None)
    dob = ObjectProperty(None)
    newp = ObjectProperty(None)
    def resetPass(self):
        if find_user(str(self.identity.text))==0:
            no_user()
        else:
            users = db.child("users").get()
            for i in users.each():
                if (str(self.identity.text) == str(i.val()['IDnum'])) and (str(self.dob.text) == str(i.val()['DOB'])):
                    db.child("users").child(str(self.identity.text)).update({'pass': str(self.newp.text)})
                    changedsucc()
                    WM.current = "Home"
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
           MangerDuser(name="MangerDuser"), UserPage(name="UserPage"),MangerMakeTeacher(name="MangerMakeTeacher"),PassReset(name="PassReset")]
for screens in screens:
    WM.add_widget(screens)


# List of screens in kv file

def invalidForm():
    pop = Popup(title='Invalid Form', content=Label(text='This Email already exist'),
                size_hint=(None, None), size=(400, 400))
    pop.open()
def changedsucc():
    pop = Popup(title='Succeded', content=Label(text='Password changed successfully'),
                size_hint=(None, None), size=(400, 400))
    pop.open()


def invalidinFormation():
    pop = Popup(title='Invalid info', content=Label(text='invalid information'),
                size_hint=(None, None), size=(400, 400))
    pop.open()

def no_user():
    pop = Popup(title='Error!', content=Label(text='This user does not exist'),
                size_hint=(None, None), size=(400, 400))
    pop.open()

def deletedS():
    pop = Popup(title='Success!', content=Label(text='This user has been deleted'),
                size_hint=(None, None), size=(400, 400))
    pop.open()

def IsnowTeacher():
    pop = Popup(title='Success!', content=Label(text='This user has promoted to teacher'),
                size_hint=(None, None), size=(400, 400))
    pop.open()
# pop up massage for ivalid input

class SchoolApp(App):
    def build(self):
        return WM


if __name__ == '__main__':
    SchoolApp().run()
