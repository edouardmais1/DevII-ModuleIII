from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.config import Config
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget


# Connexion and Inscription screen creation
class ConnexionScreen(Screen):
    """
    ---> assure la gestion des inscriptions au sein de l'application
    """
    pass


class InscriptionScreen(Screen):
    """
    ---> assure la gestion des inscriptions au sein de l'application
    """
    prenom_input = ObjectProperty

    def __init__(self, **kwargs):
        super(InscriptionScreen, self).__init__(**kwargs)

    def validPrenom(self, instance, value):
        """
        ---> permet de vérifier la validité du prénom
        """
        if any(elem.isdigit() for elem in value):
            instance.foreground_color = (1, 0, 0, 1)

        elif set('[~!@#$%^&*()_+{}":;\']+$').intersection(value):
            instance.foreground_color = (1, 0, 0, 1)

        else:
            instance.foreground_color = (0, 255, 0, 1)

    def validNom(self, instance, value):
        """
        ---> permet de vérifier la validité du nom
        """
        if any(elem.isdigit() for elem in value):
            instance.foreground_color = (1, 0, 0, 1)

        elif set('[~!@#$%^&*()_+{}":;\']+$').intersection(value):
            instance.foreground_color = (1, 0, 0, 1)

        else:
            instance.foreground_color = (0, 255, 0, 1)

    def getEmail(self):
        pass

    def get_password(self):
        pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file('Main.kv')


class MainApp(App):
    def build(self):
        return kv


if __name__ == '__main__':
    MainApp().run()
