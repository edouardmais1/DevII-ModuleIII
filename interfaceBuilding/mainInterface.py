from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.config import Config
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget


# Connexion and Inscription screen creation
class ConnexionScreen(Screen):
    pass


class InscriptionScreen(Screen):
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file('Main.kv')


class MainApp(App):
    def build(self):
        return kv


MainApp().run()
