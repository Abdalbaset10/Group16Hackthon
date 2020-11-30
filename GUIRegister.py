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
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty




class HomeWindo(Screen):
    pass

class RegiWindo(Screen):
    idn = ObjectProperty(None)
    fullname = ObjectProperty(None)
    dob = ObjectProperty(None)
    username = ObjectProperty(None)
    password = ObjectProperty(None)

    def regibtn(self):
        if self.idn.text !='' and self.fullname.text !='' and self.dob.text !='' and self.username.text !='' and self.password.text !='':
            print("Done")
        else:
            print("HEY")
            invalidForm()





class Loginwindo(Screen):
    pass


class MangerLog(Screen):
    pass

class WindowManger(ScreenManager):
    pass
kv=Builder.load_file("mainapp.kv")
WM=WindowManger()


def invalidForm():
    pop = Popup(title='Invalid Form', content=Label(text='Please fill in all inputs with valid information.'),size_hint=(None, None), size=(400, 400))
    pop.open()










class MyMainApp(App):
    def build(self):

       return kv





if __name__ == '__main__':
    MyMainApp().run()
