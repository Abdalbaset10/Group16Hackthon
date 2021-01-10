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
from kivymd.uix.list import OneLineListItem,TwoLineListItem
from kivymd.uix.button import MDFlatButton
import pyrebase
from datetime import datetime
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.dialog import MDDialog

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

def username_exist(user):
    users = db.child("users").get()
    user_found = 0
    for i in users.each():
        if str(user) == str(i.val()["Username"]):
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

    dialog=MDDialog(title='invalid Form')
    close_button = MDFlatButton(text='Close', on_release=dialog.dismiss())
    dialog.open()

def changedsucc():
    pop = Popup(title='Succeded', content=Label(text='Password changed successfully'),
                size_hint=(None, None), size=(400, 400))
    pop.open()


def invalidinFormation():
    dialog = MDDialog(title='invalid Form')
    close_button = MDFlatButton(text='Close', on_release=dialog.dismiss())
    dialog.open()


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


def gradechanged():
    pop = Popup(title='Success!', content=Label(text='grade has been changed'),
                size_hint=(None, None), size=(400, 400))
    pop.open()


class MenuScreen(Screen):
    pass


class MangerLog(Screen):
    def home_button(self):
        self.manager.current = 'mangerlog'
        print(self.manager.screens[7].ids)

    def my_profile(self):
        self.manager.screens[7].build()
        self.manager.current = 'myprofile'

    def manger_log(self):
        self.manager.screens[16].build()
        self.manager.current = 'manclass'

    def my_anno(self):
        self.manager.screens[18].build()
        self.manager.current = 'pageann'

    pass


class MyProfile(Screen):
    def build(self):
        user_key = currentUser(str(self.manager.screens[2].ids.username.text))
        user = db.child("users").child(user_key).get()
        self.manager.screens[7].ids.thisUser
        self.manager.screens[7].ids.name.text = 'Name:' + ' ' + user.val()['Name']
        self.manager.screens[7].ids.username.text = 'Username:' + ' ' + user.val()['Username']
        self.manager.screens[7].ids.idnum.text = 'ID Number:' + ' ' + user.val()['IDnum']
        self.manager.screens[7].ids.dob.text = 'Date of Birth:' + ' ' + user.val()['DOB']
        self.manager.screens[7].ids.subt.text = 'Title:' + ' ' + user.val()['Title']

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
        dialog = MDDialog(title='Change date of birth', text='test', size_hint=(0.5, 0.5))
        ##dialog.open()

    pass


class TeacherLog(Screen):
    def home_button(self):
        self.manager.current = 'teacherlog'

    def my_profile(self):
        self.manager.screens[7].build()
        self.manager.current = 'myprofile'

    def S_grades(self):
        self.manager.screens[14].build()
        self.manager.current = 'chgrades'

    def my_anno(self):
        self.manager.screens[18].build()
        self.manager.current = 'pageann'

    def studpress(self):
        self.manager.screens[20].build()
        self.manager.current = 'clssp'

    pass


class StudentPage(Screen):

    def home_button(self):
        self.manager.screens[13].ids.grades.clear_widgets()
        self.manager.current = 'Spage'

    def my_grades(self):
        self.manager.screens[13].build()
        self.manager.current = 'grades'

    def my_profile(self):
        self.manager.screens[12].build()
        self.manager.current = 'Sprofile'

    def my_anno(self):
        self.manager.screens[18].build()
        self.manager.current = 'pageann'

    def showsh(self):
        self.manager.screens[21].build()
        self.manager.current = 'clsh'

        pass


class Sprofile(Screen):
    def build(self):
        user_key = currentUser(str(self.manager.screens[2].ids.username.text))
        user = db.child("users").child(user_key).get()
        self.manager.screens[12].ids.name.text = 'Name:' + ' ' + user.val()['Name']
        self.manager.screens[12].ids.username.text = 'Username:' + ' ' + user.val()['Username']
        self.manager.screens[12].ids.idnum.text = 'ID Number:' + ' ' + user.val()['IDnum']
        self.manager.screens[12].ids.dob.text = 'Date of Birth:' + ' ' + user.val()['DOB']
        self.manager.screens[12].ids.subt.text = 'Title:' + ' ' + user.val()['Title']

    def home_button(self):
        self.manager.screens[13].ids.grades.clear_widgets()
        self.manager.current = 'Spage'

    pass


class GradesPage(Screen):
    def build(self):
        user_key = currentUser(str(self.manager.screens[2].ids.username.text))
        grades = db.child("users").child(user_key).child("Grades").get()
        user = db.child("users").child(user_key).get()
        self.manager.screens[13].ids.stdentgradebar.title = 'Grades Of ' + str(user.val()['Name'])
        for sub in grades.each():
            items = OneLineListItem(text=str(sub.key()) + ': ' + str(sub.val()))
            self.manager.screens[13].ids.grades.add_widget(items)

    def home_button(self):
        self.manager.screens[13].ids.grades.clear_widgets()
        self.manager.current = 'Spage'

    pass


class ChangeSgrade(Screen):
    def build(self):

        user_key = currentUser(str(self.manager.screens[2].ids.username.text))
        teacherid = db.child("users").child(user_key).get()

        teachersubject = teacherid.val()['Subject']
        user = db.child("users").get()
        for sub in user.each():
            if str(sub.val()['Title']) == str('Student'):
                student = db.child("users").child(sub.key()).child("Grades").get()
                items = OneLineListItem(text='Student ID: ' + str(sub.key()) + '  Student Name: ' + str(
                    sub.val()['Name']) + '   Subject: ' + str(teachersubject) + ':   ' + str(
                    student.val()[teachersubject]))
                self.manager.screens[14].ids.grades.add_widget(items)

    def home_button(self):
        self.manager.screens[14].ids.grades.clear_widgets()
        self.manager.current = 'teacherlog'

    def change_grade(self):
        user_key = currentUser(str(self.manager.screens[2].ids.username.text))
        teacherid = db.child("users").child(user_key).get()

        teachersubject = teacherid.val()['Subject']

        if find_user(self.ids.studentid.text) == 0:
            no_user()
        else:
            db.child("users").child(self.ids.studentid.text).child("Grades").update(
                {teachersubject: self.ids.newgrade.text})
            gradechanged()


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
        db.child("users").child(user_key).update({'Name': str(self.ids.newname.text)})
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
        db.child("users").child(user_key).update({'DOB': str(self.ids.newdob.text)})
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


##aa
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
            if find_user(str(self.id_box.text)) == 0 and username_exist(self.ids.username.text) == 0:
                GradeData={'Math':'None','Arabic':'None','Sport':'None','ComputerS':'None'}
                users_data = {'Name': self.fullname_box.text, 'IDnum': self.id_box.text,
                              'Username': self.username_box.text, 'DOB': self.dob.text, 'pass': self.password_box.text,'Grades':GradeData,'Class':'11',
                              'Title': str('Student')}
                db.child("users").child(str(self.id_box.text)).set(users_data)
                if str(self.id_box.text) == ("315198564"):
                    db.child("users").child("315198564").update({'Title': 'Manager'})
                print("account created successfully")
            else:
                self.sameuser()

        else:

           self.empty()


    def empty(self):
        dialog=MDDialog(title='you forgot to fill one of the boxes')
        dialog.open()
    def sameuser(self):
        dialog=MDDialog(title='you enterd an Existing ID or Username')
        dialog.open()
    pass
class PassReset(Screen):
    def resetPass(self):
        if find_user(str(self.ids.IDnum.text)) == 0:
            no_user()
        else:
            users = db.child("users").get()
            for i in users.each():
                if (str(self.ids.IDnum.text) == str(i.val()['IDnum'])) and (
                        str(self.ids.dob.text) == str(i.val()['DOB'])):
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
            ###init Tool bar names in whole logging in##
            self.manager.screens[3].ids.managertoolbar.title = 'Welcome' + ' ' + user.val()['Name']

            self.manager.screens[4].ids.teachername.title = 'Welcome' + ' ' + user.val()['Name']

            print(self.manager.screens[16].ids)
            ###Page 9 change name ###
            self.manager.screens[9].ids.username.text = user.val()['Username']

            ###Page 10 change DOB ###
            self.manager.screens[10].ids.username.text = user.val()['Username']
            ###page 11 Student page ###
            self.manager.screens[11].ids.studenttoolbar.title = 'Welcome' + ' ' + user.val()['Name']
            self.manager.screens[11].ids.username.text = user.val()['Username']

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

        else:
            self.invalid()


    def invalid(self):
        dialog = MDDialog(title='Wrong Username or password')
        dialog.open()



    pass
###if grantAccess(str(self.username_box.text), str(self.password_box.text)) == 0:

class reportprob(Screen):
    msgtxt = ObjectProperty(None)
    emailtxt = ObjectProperty(None)
    tnow = datetime.now()

    def printtxt(self):
        email = str(self.emailtxt.text)
        data = {'report': self.msgtxt.text, 'Email': self.emailtxt.text,
                'Date': self.tnow.strftime("%m/%d/%Y, %H:%M:%S")}
        db.child('Report').child(email.split("@")[0]).set(data)

    pass


class ManagClass(Screen):
    menu=ObjectProperty(None)
    def build(self):
        print("we arrived")
        daylist = ["sunday", "monday", "tuesday", "wednesday", "thursday"]
        timelist = ["8:00", "8:45", "9:30", "10:15", "11:30", "12:45", "13:30"]
        for i in daylist:
            items = OneLineListItem(text=str(i))
            items.bind(on_release=self.manager.screens[16].set_itemday)
            self.manager.screens[16].ids.menuday.add_widget(items)

        for i in timelist:
            items = OneLineListItem(text=str(i))
            items.bind(on_release=self.manager.screens[16].set_itemtime)
            self.manager.screens[16].ids.menutime.add_widget(items)

    def set_itemtime(self, text_of_the_option):
        self.manager.screens[16].ids.timepicked.text=text_of_the_option.text
    def set_itemday(self,text_of_the_option):
        self.manager.screens[16].ids.daypicked.text = text_of_the_option.text
    def data_submit(self):
        teachersub=db.child("users").child(self.manager.screens[16].ids.idt.text).get()
        print(teachersub.val()['Subject'])
        db.child("Class").child(self.manager.screens[16].ids.classid.text).child("Schedule").child(str(self.manager.screens[16].ids.daypicked.text)).child(str(self.manager.screens[16].ids.timepicked.text)).set(teachersub.val()['Subject'])



class annonman(Screen):
    anntext = ObjectProperty(None)
    tnow = datetime.now()

    def send_anno(self):
        data = {'text': self.anntext.text, 'Date': self.tnow.strftime("%m/%d/%Y, %H:%M:%S")}
        db.child('announcement').child(self.tnow.strftime("%m")).set(data)


class pageann(Screen):
    time = datetime.now()

    def build(self):
        anno = db.child('announcement').child(self.time.strftime("%m")).get()
        self.manager.screens[18].ids.reanno.text = 'From' + 'School principal:" ' + anno.val()['text'] + '"'
        self.manager.screens[18].ids.retime.text = anno.val()['Date']


class viewsch(Screen):

    pass


class clsspress(Screen):
    tnow = datetime.now()

    def build(self):
        students = db.child("Class").child("11").child("Students").get()

        for sub in students.each():
            stud = db.child('users').child(sub.key()).get()
            items = OneLineListItem(text=str(stud.val()['Username']))
            items.bind(on_release=self.manager.screens[20].present)
            self.manager.screens[20].ids.studlist.add_widget(items)

    def present(self, text):
        thisuser=db.child("users").get()
        for u in thisuser.each():
            if u.val()["Username"] == str(text.text):
                db.child("users").child(str(u.key())).child("present").child(self.tnow.strftime("%d,%m,%Y, %H:%M:%S")).set("checked")

    pass

class clsch(Screen):
    def build(self):
        thisstudent=currentUser(self.manager.screens[2].ids.username.text)
        currentS=db.child("users").child(thisstudent).get()

        day1=db.child("Class").child(currentS.val()['Class']).child("Schedule").child("sunday").get()
        day2=db.child("Class").child(currentS.val()['Class']).child("Schedule").child("monday").get()
        day3=db.child("Class").child(currentS.val()['Class']).child("Schedule").child("tuesday").get()
        day4=db.child("Class").child(currentS.val()['Class']).child("Schedule").child("wednesday").get()
        day5=db.child("Class").child(currentS.val()['Class']).child("Schedule").child("thursday").get()
        sunday=OneLineListItem(text=str("(Sunday)"))
        self.manager.screens[21].ids.sun.add_widget(sunday)
        monday=OneLineListItem(text=str("(monday)"))
        self.manager.screens[21].ids.mon.add_widget(monday)
        tuesday=OneLineListItem(text=str("(tuesday)"))
        self.manager.screens[21].ids.tue.add_widget(tuesday)
        wednesday=OneLineListItem(text=str("(wednesday)"))
        self.manager.screens[21].ids.wed.add_widget(wednesday)
        thursday=OneLineListItem(text=str("(thursday)"))
        self.manager.screens[21].ids.thu.add_widget(thursday)

        for i in day1.each():
            items = TwoLineListItem(text=str(i.val()),secondary_text=str(i.key()))
            self.manager.screens[21].ids.sun.add_widget(items)
        for i in day2.each():
            items = TwoLineListItem(text=str(i.val()),secondary_text=str(i.key()))
            self.manager.screens[21].ids.mon.add_widget(items)
        for i in day3.each():
            items = TwoLineListItem(text=str(i.val()),secondary_text=str(i.key()))
            self.manager.screens[21].ids.tue.add_widget(items)
        for i in day4.each():
            items = TwoLineListItem(text=str(i.val()),secondary_text=str(i.key()))
            self.manager.screens[21].ids.wed.add_widget(items)
        for i in day5.each():
            items = TwoLineListItem(text=str(i.val()),secondary_text=str(i.key()))
            self.manager.screens[21].ids.thu.add_widget(items)

    def home_button(self):
        self.manager.screens[21].ids.sun.clear_widgets()
        self.manager.screens[21].ids.mon.clear_widgets()
        self.manager.screens[21].ids.tue.clear_widgets()
        self.manager.screens[21].ids.wed.clear_widgets()
        self.manager.screens[21].ids.thu.clear_widgets()
        self.manager.current = 'Spage'

    pass

class school(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Blue'
        screen = Builder.load_string(screen_nav)
        return screen

    def navigation_draw(self):
        print("navigation")


school().run()
