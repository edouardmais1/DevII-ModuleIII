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
from mongo.mongoConnector import *


# Connexion and Inscription screen creation
class ConnexionScreen(Screen):
    """
    ---> assure la gestion des inscriptions au sein de l'application
    """
    email_input = ObjectProperty
    password_input = ObjectProperty

    def connexionButton(self):
        mail = self.email_input.text
        hash_pswd = hashPassword(self.password_input.text)
        if connexion(mail=mail, password=hash_pswd):
            wm = App.get_running_app().root
            print("CONNECTE")
            wm.current = 'programWindow'

        else:
            print("ERROR 404")
            return False


class InscriptionScreen(Screen):
    """
    ---> assure la gestion des inscriptions au sein de l'application à travers différentes méthodes.

    """
    # les 6 champs principaux lors de l'inscription de l'utilisateur
    prenom_input = ObjectProperty
    nom_input = ObjectProperty
    email_input = ObjectProperty
    code_input = ObjectProperty
    password_input = ObjectProperty
    check_password_input = ObjectProperty

    # message d'envoi de code de validation
    code_validation_message = ObjectProperty

    # message lors du check du code de validation dans code_input
    check_code = ObjectProperty

    # message d'information lors de la saisie du mot de passe
    password_input_message = ObjectProperty

    # message d'information lors de la validation du mot de passe
    check_password_message = ObjectProperty

    # variable contenant le code de validation de mail
    code_mail = ""

    # variable contenant le mot de passe une fois celui ci initilaisé
    password = ""

    # variable contenant le prénom de l'utilisateur
    prenom = ""

    # préconditions du submit
    submit_code = False
    submit_password = False
    submit_mail = False

    def __init__(self, **kwargs):
        super(InscriptionScreen, self).__init__(**kwargs)

    def validPrenom(self, instance, value):
        """
        ---> permet à l'utilisateur de rentrer son prénom et vérifier la validité du prénom

             Pre: -

             Post: valide la saisie de l'utilisateur
        """
        if any(elem.isdigit() for elem in value):
            instance.foreground_color = (1, 0, 0, 1)

        elif set('[~!@#$%^&*()_+{}":;\']+$').intersection(value):
            instance.foreground_color = (1, 0, 0, 1)

        elif len(value) <= 3:
            instance.foreground_color = (1, 0, 0, 1)

        elif len(value) >= 20:
            instance.foreground_color = (1, 0, 0, 1)

        else:
            instance.foreground_color = (0, 255, 0, 1)
            self.prenom = value

    def validNom(self, instance, value):
        """
        ---> permet à l'utilisateur de rentrer son prénom et vérifier la validité du prénom

             Pre: -

             Post: valide la saisie de l'utilisateur
        """
        if any(elem.isdigit() for elem in value):
            instance.foreground_color = (1, 0, 0, 1)

        elif set('[~!@#$%^&*()_+{}":;\']+$').intersection(value):
            instance.foreground_color = (1, 0, 0, 1)

        elif len(value) <= 3:
            instance.foreground_color = (1, 0, 0, 1)

        elif len(value) >= 20:
            instance.foreground_color = (1, 0, 0, 1)

        else:
            instance.foreground_color = (0, 255, 0, 1)

    def getEmail(self, instance, value):
        """
        ---> permet d'envoyer un code de validation à l'utilisateur apres une série de procédés
             visants à valider le format de l'adresse mail de l'utilisateur saisie

             Pre: l'utilisateur doit au préalable avoir saisi un prénom et nom valide

             Post: renvoi un mail à l'adresse mail saisie avec un code de validation

             Raise: IndexError si l'utilisateur valide un champ d'input vide
        """
        prenom = self.prenom

        try:
            # check if the email format is ok
            if checkEmailValidation(prenom, value):
                instance.foreground_color = (0, 255, 0, 1)

                # envoi d'un code de validation à l'utilisateur
                self.code_mail = get_email_validation(value)
                self.code_validation_message.text = "un code de validation vous a été envoyé"

            else:
                instance.foreground_color = (1, 0, 0, 1)

        except IndexError:
            self.code_validation_message.text = "veuillez au préalable avoir rempli votre prenom et nom"

    def checkCode(self, instance, value):
        """
        ---> permet de vérifier l'authenticité du code envoyé par mail à l'utilisateur

             Pre: -

             Post: valide la saisie du code de validation
        """

        # la valeur du code envoyé précédement par mail lors de la validation de l'email
        code = self.code_mail

        # si le code correspond, ---> code validé
        if int(value) == code:
            instance.foreground_color = (0, 255, 0, 1)
            self.check_code.text = "code validé"
            self.submit_code = True
            self.submit_mail = True

        else:
            self.check_code.text = "veuillez réessayer..."

    def getPassword(self, instance, value):
        """
        ---> permet la création d'un mot de passe pour le compte du nouvel utilisateur.
        """
        self.password_input_message.text = "veuillez saisir un mdp avec au moins : "
        if checkPassword(value):
            instance.foreground_color = (0, 255, 0, 1)
            self.password_input_message.text = "password assez robuste"
            self.password = value

        else:
            self.password_input_message.text = "password pas assez robuste, réessayez..."

    def checkPassword(self, instance, value):
        if value == self.password:
            instance.foreground_color = (0, 255, 0, 1)
            self.check_password_message.text = "mot de passe confirmé"
            self.submit_password = True

        else:
            self.check_password_message.text = "veuillez saisir le meme mot de passe que celui choisi"

    def Submit(self):
        if self.submit_code and self.submit_mail and self.submit_password:
            mail = self.email_input.text
            hash_pswd = hashPassword(self.password_input.text)
            submit_data_DB(mail=mail, password=hash_pswd)
            wm = App.get_running_app().root
            wm.current = 'programWindow'
        else:
            pass

class programWindow(Screen):
    pass


class WindowManager(ScreenManager):
    Window.size = (1000, 700)


kv = Builder.load_file('Main.kv')


class MainApp(App):
    def build(self):
        return kv


if __name__ == '__main__':
    MainApp().run()
