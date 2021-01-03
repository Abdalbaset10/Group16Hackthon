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


firebase=firebase.FirebaseApplication("https://myschoolproject-72b52-default-rtdb.firebaseio.com/", None)


class WindowManger(ScreenManager):
    pass

class ViewWindo(BoxLayout):
    msgtxt=ObjectProperty(None)
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
    def printtxt(self):
        result= firebase.post('msg',self.msgtxt.text)


kv = Builder.load_file("view.kv")

###WM=ScreenManager()
###screens=[ViewWindo(name="Viewus")]
##for screens in screens:
  ###  WM.add_widget(screens)

class SchoolApp(App):
    def build(self):
        return ViewWindo()


if __name__ == '__main__':
    SchoolApp().run()