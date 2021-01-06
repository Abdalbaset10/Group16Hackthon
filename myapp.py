from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.lang import Builder
from kivy.uix.label import Label
from association import screen_nav
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.dialog import MDDialog
from kivy.uix.textinput import TextInput
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
firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
auth = firebase.auth()
storage = firebase.storage()


def find_user(user):
    users = db.child("users").get()
    user_found = 0
    for i in users.each():
        if str(user) == str(i.key()):
            user_found += 1
    if user_found > 0:
        return 1
    else:
        return 0


def currentUser(username):
    user = db.child("users").get()
    for i in user.each():
        if i.val()['Username'] == str(username):
            return str(i.key())


def grantAccess(username, password):
    users = db.child("users").get()
    grant_Access = 0
    for i in users.each():
        if (str(username) == str(i.val()['Username'])) and (str(password) == str(i.val()['pass'])):
            grant_Access = 1
        if (str(username) == str(i.val()['Username'])) and (str(password) != str(i.val()['pass'])):
            grant_Access = 0
    return grant_Access


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

def namechanged():
    pop = Popup(title='Success!', content=Label(text='Name changed successfully reloggin to see the change'),
                size_hint=(None, None), size=(400, 400))
    pop.open()
def dobchanged():
    pop = Popup(title='Success!', content=Label(text='Date of birth changed successfully reloggin to see the change'),
                size_hint=(None, None), size=(400, 400))
    pop.open()


class MenuScreen(Screen):
    pass


class MangerLog(Screen):
    def home_button(self):
        self.manager.current = 'mangerlog'
        print(self.manager.screens[7].ids)

    pass


class MyProfile(Screen):

    def home_button(self):
        user_key = currentUser(str(self.manager.screens[2].ids.username.text))
        user = db.child("users").child(user_key).get()
        print(user_key)
        logto = 0
        if str('Teacher') == str(user.val()['Title']):
            logto = 1
        if str('Manager') == str(user.val()['Title']):
            logto = 2
        if logto == 1:
            self.manager.current = 'teacherlog'

        if logto == 2:
            self.manager.current = 'mangerlog'

    def change_dob_D(self):
        dialog=MDDialog(title='Change date of birth',text='test',size_hint=(0.5,0.5))
        ##dialog.open()

    pass


class TeacherLog(Screen):
    def home_button(self):
        self.manager.current = 'teacherlog'

    pass

class StudentPage(Screen):
    def home_button(self):
        user_key =self.manager.current = 'Spage'

    pass
class Sprofile(Screen):
    def build(self):
        user_key=currentUser(str(self.manager.screens[2].ids.username.text))
        print(user_key)

    def home_button(self):
        user_key =self.manager.current = 'Spage'



    def home_button(self):
        self.manager.current = 'Spage'

    pass


class MangerDuser(Screen):
    idnum = ObjectProperty(None)

    def deletebtn(self):
        print(str(self.idnum.text))
        if find_user(str(self.idnum.text)) == 0:
            no_user()
        else:
            db.child("users").child(str(self.idnum.text)).remove()
            deletedS()

    pass

class Change_Name(Screen):

    def change_name(self):
        user_key = currentUser(str(self.ids.username.text))
        db.child("users").child(user_key).update({'Name':str(self.ids.newname.text)})
        namechanged()
    def back_button(self):
        user_key = currentUser(str(self.ids.username.text))
        user = db.child("users").child(user_key).get()
        print(user_key)
        logto = 0
        if str('Teacher') == str(user.val()['Title']):
            logto = 1
        if str('Manager') == str(user.val()['Title']):
            logto = 2
        if logto == 1:
            self.manager.current = 'teacherlog'

        if logto == 2:
            self.manager.current = 'mangerlog'

    pass
class Change_DOB(Screen):

    def change_DOB(self):
        user_key = currentUser(str(self.ids.username.text))
        db.child("users").child(user_key).update({'DOB':str(self.ids.newdob.text)})
        dobchanged()
    def back_button(self):
        user_key = currentUser(str(self.ids.username.text))
        user = db.child("users").child(user_key).get()
        logto = 0
        if str('Teacher') == str(user.val()['Title']):
            logto = 1
        if str('Manager') == str(user.val()['Title']):
            logto = 2
        if logto == 1:
            self.manager.current = 'teacherlog'

        if logto == 2:
            self.manager.current = 'mangerlog'


    pass

class MangerMakeTeacher(Screen):
    identity = ObjectProperty(None)
    subject = ObjectProperty(None)

    def MkTeacher(self):
        if find_user(str(self.identity.text)) == 0:
            no_user()
        else:
            db.child("users").child(str(self.identity.text)).update({'Title': 'Teacher'})
            db.child("users").child(str(self.identity.text)).update({'Subject': str(self.subject.text)})
            IsnowTeacher()

    pass


class RegiWindo(Screen):
    id_box = ObjectProperty(None)
    fullname_box = ObjectProperty(None)
    dob = ObjectProperty(None)
    username_box = ObjectProperty(None)
    password_box = ObjectProperty(None)

    def regibtn(self):
        print(self.id_box.text)
        print(find_user(str(self.id_box.text)))
        if self.id_box.text != '' and self.fullname_box.text != '' and self.dob.text != '' and self.username_box.text != '' and self.password_box.text != '':
            if find_user(str(self.id_box.text)) == 0:
                users_data = {'Name': self.fullname_box.text, 'IDnum': self.id_box.text,
                              'Username': self.username_box.text, 'DOB': self.dob.text, 'pass': self.password_box.text,
                              'Title': str('Student')}
                db.child("users").child(str(self.id_box.text)).set(users_data)
                if str(self.id_box.text) == ("315198564"):
                    db.child("users").child("315198564").update({'Title': 'Manager'})
                print("account created successfully")
            else:
                invalidForm()

        else:

            invalidForm()

    pass

class PassReset(Screen):
    def resetPass(self):
        if find_user(str(self.ids.IDnum.text))==0:
            no_user()
        else:
            users = db.child("users").get()
            for i in users.each():
                if (str(self.ids.IDnum.text) == str(i.val()['IDnum'])) and (str(self.ids.dob.text) == str(i.val()['DOB'])):
                    db.child("users").child(str(self.ids.IDnum.text)).update({'pass': str(self.ids.newpass.text)})
                    changedsucc()
                    self.manager.current = 'menu'
    pass
class Loginwindo(Screen):
    username_box = ObjectProperty(None)
    password_box = ObjectProperty(None)

    def logbtn(self):

        logto = 0

        if grantAccess(str(self.username_box.text), str(self.password_box.text)) == 1:

            user_key = currentUser(str(self.username_box.text))
            user = db.child("users").child(user_key).get()
            ###init names for logged in##
            self.manager.screens[3].ids.managertoolbar.title = 'Welcome' + ' ' + user.val()['Name']

            self.manager.screens[4].ids.teachername.title = 'Welcome' + ' ' + user.val()['Name']

            self.manager.screens[7].ids.thisUser = user_key
            ###initializing for profile page 7 ##
            self.manager.screens[7].ids.thisUser
            self.manager.screens[7].ids.name.text='Name:' + ' ' + user.val()['Name']
            self.manager.screens[7].ids.username.text = 'Username:' + ' ' + user.val()['Username']
            self.manager.screens[7].ids.idnum.text = 'ID Number:' + ' ' + user.val()['IDnum']
            self.manager.screens[7].ids.dob.text = 'Date of Birth:' + ' ' + user.val()['DOB']
            self.manager.screens[7].ids.subt.text = 'Title:' + ' ' + user.val()['Title']

            print(self.manager.screens[2].ids)
            ###Page 9 change name ###
            self.manager.screens[9].ids.username.text = user.val()['Username']

            ###Page 10 change DOB ###
            self.manager.screens[10].ids.username.text = user.val()['Username']

            db.child("Online").child(self.username_box.text).set("ok")

            if str('Teacher') == str(user.val()['Title']):
                logto = 1
            if str('Manager') == str(user.val()['Title']):
                logto = 2
            if logto == 1:
                self.manager.current = 'teacherlog'

            if logto == 2:
                self.manager.current = 'mangerlog'

            if logto == 0:
                self.manager.current = 'Spage'

        if grantAccess(str(self.username_box.text), str(self.password_box.text)) == 0:
            invalidinFormation()

    pass


class school(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Red'
        screen = Builder.load_string(screen_nav)
        return screen

    def navigation_draw(self):
        print("navigation")


school().run()
