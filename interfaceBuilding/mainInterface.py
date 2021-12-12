from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.config import Config
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.core.window import Window

from Project_functions.Email import *
from Project_functions.Password import *


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
    nom_input = ObjectProperty
    email_input = ObjectProperty
    code_input = ObjectProperty
    password_input = ObjectProperty

    # message d'envoi de code de validation
    code_validation_message = ObjectProperty

    # message lors du check du code de validation dans code_input
    check_code = ObjectProperty

    # message d'information lors de la saisie du mot de passe
    check_password = ObjectProperty

    # variable contenant le code de validation de mail
    code_mail = ""

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

    def getEmail(self, instance, value):
        """
        ---> permet d'envoyer un code de validation à l'utilisateur apres une série de procédés
             visants à valider le format de l'adresse mail de l'utilisateur saisie
        """
        prenom = self.prenom_input.text

        # check if the email format is ok
        if checkEmailValidation(prenom, value):
            instance.foreground_color = (0, 255, 0, 1)

            # envoi d'un code de validation à l'utilisateur
            self.code_mail = get_email_validation(value)
            self.code_validation_message.text = "un code de validation vous a été envoyé"

        # laisse la saisie de l'utilisateur en rouge
        else:
            instance.foreground_color = (1, 0, 0, 1)

    def checkCode(self, instance, value):
        """
        ---> permet de vérifier l'authenticité du code envoyé par mail à l'utilisateur
        """

        # la valeur du code envoyé précédement par mail lors de la validation de l'email
        code = self.code_mail

        # si le code correspond, ---> code validé
        if int(value) == code:
            instance.foreground_color = (0, 255, 0, 1)
            self.check_code.text = "code validé"

        else:
            self.check_code.text = "veuillez réessayer..."

    def getPassword(self,instance, value):
        """
        ---> permet la création d'un mot de passe pour le compte du nouvel utilisateur.
        """
        self.check_password.text = "veuillez saisir un mdp avec au moins : "
        if checkPassword(value):
            instance.foreground_color = (0, 255, 0, 1)
            self.check_password.text = "password assez robuste"

        else:
            self.check_password.text = "password pas assez robuste, réessayez..."


    def checkPassword(self, instance, value):
        pass


class WindowManager(ScreenManager):
    Window.size = (1200, 900)


kv = Builder.load_file('Main.kv')


class MainApp(App):
    def build(self):
        return kv


if __name__ == '__main__':
    MainApp().run()
