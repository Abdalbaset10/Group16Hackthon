import kivy
from  kivy.app import App
from  kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.config import Config
from kivy.uix.relativelayout import RelativeLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen

class HomeWindo(Screen):
    pass

class RegiWindo(Screen):
    pass

class Loginwindo(Screen):
    pass

class WindowManger(ScreenManager):
    pass
kv=Builder.load_file("mainapp.kv")










class MyMainApp(App):
    def build(self):

       return kv





if __name__ == '__main__':
    MyMainApp().run()