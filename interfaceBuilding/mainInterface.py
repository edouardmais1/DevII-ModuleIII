from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen

#type kyprops anytime you need to declare ObjectProperty
class MyGridLayout(Widget):

    def press_login(self):
        print("Login pressed")

    def press_signin(self):
        print("Signin pressed")

class MainInterface(App):
    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    MainInterface().run()
