import kivy
from  kivy.app import App
from  kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.config import Config
from kivy.uix.relativelayout import RelativeLayout








class MyApp(App):
    def build(self):

        r1 = RelativeLayout(size=(10, 10))
        t1 = Label(text="Welcome to School App",pos_hint ={'center_x':.5, 'center_y':.8},size_hint=(1, 1))
        b1 = Button(size_hint=(.1,.1),pos_hint ={'center_x':.9, 'center_y':.6},text="Register")
        b2 = Button(size_hint=(.1, .1), pos_hint={'center_x': .9, 'center_y': .4}, text="Login")
        r1.add_widget(t1)
        r1.add_widget(b1)
        r1.add_widget(b2)
        return r1






if __name__ == '__main__':
    MyApp().run()