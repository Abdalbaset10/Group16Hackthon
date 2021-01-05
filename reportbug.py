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
from kivy.uix.recycleview import RecycleView
import pyrebase
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from firebase import firebase
from kivymd.app import MDApp
import json
import firebase_admin
from firebase_admin import  credentials
from firebase_admin import db
from datetime import datetime
###firebase=firebase.FirebaseApplication("https://myschoolproject-72b52-default-rtdb.firebaseio.com/", None)

cred = credentials.Certificate('myschoolproject.json')
firebase_admin.initialize_app(cred,{
    'databaseURL':'https://myschoolproject-72b52-default-rtdb.firebaseio.com/'
})


class WindowManger(ScreenManager):
    pass


class ViewWindo(BoxLayout):
    msgtxt=ObjectProperty(None)
    emailtxt=ObjectProperty(None)
    tnow = datetime.now()
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
    def printtxt(self):
        email=str(self.emailtxt.text)
        data= {'report':self.msgtxt.text,'Email':self.emailtxt.text,'Date':self.tnow.strftime("%m/%d/%Y, %H:%M:%S")}
        ref=db.reference('Report')
        ref.child('report').child(email.split("@")[0]).set(data)




kv = Builder.load_file("view.kv")

###WM=ScreenManager()
###screens=[ViewWindo(name="Viewus")]
##for screens in screens:
  ###  WM.add_widget(screens)

class SchoolApp(MDApp):
    def build(self):
        return ViewWindo()


if __name__ == '__main__':
    SchoolApp().run()
