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
from Project_functions.check import *


# Connexion and Inscription screen creation
class ConnexionScreen(Screen):
    """
    ---> Assure la gestion des connexions au sein de l'application et de la Gui Kivy.

         Pre: /
         Post: /

    """
    email_input = ObjectProperty
    password_input = ObjectProperty

    def connexionButton(self):
        """
        ---> Fonction gestionnaire du bouton de connexion de l'utilisateur.

        Pre: l'email et le mot de passe choisis doivent au préalable éxister dans la base de données.
        Post: l'utilisateur doit pouvoir se loger au sein de l'application une fois la connexion validée.

        """
        try:
            mail = self.email_input.text
            hash_pswd = hashPassword(self.password_input.text)
            if connexion(mail=mail, password=hash_pswd):
                wm = App.get_running_app().root
                wm.current = 'programWindow'
            else:
                return False
        except Exception as e:
            print(e)


class InscriptionScreen(Screen):
    """
    ---> Assure la gestion des inscriptions au sein de l'application à travers différentes méthodes ainsi que
         la Gui Kivy.

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

    # variable contenant le nom de l'utilisateur
    nom = ""

    # préconditions du submit (test de validité des informations saisie au préalable avant un quelconque submit)
    submit_code = False
    submit_password = False
    submit_mail = False

    # variable tentative code validation
    count = 0

    def __init__(self, **kwargs):
        super(InscriptionScreen, self).__init__(**kwargs)

    def validPrenom(self, instance, value):
        """
        ---> Permet à l'utilisateur de rentrer son prénom et vérifier la validité de celui-ci.

             Pre: l'utilisateur doit rentrer un prénom valide (pas de caractères spéciaux et chiffres).
             Post: valide la saisie de l'utilisateur.
        """
        if not checkValidPrenomNom(value):
            instance.foreground_color = (1, 0, 0, 1)
        else:
            instance.foreground_color = (0, 255, 0, 1)
            self.prenom = value

    def validNom(self, instance, value):
        """
        ---> Permet à l'utilisateur de rentrer son nom et vérifier la validité de celui-ci.

             Pre: l'utilisateur doit rentrer un nom valide (pas de caractères spéciaux et chiffres).
             Post: valide la saisie de l'utilisateur.
        """
        if not checkValidPrenomNom(value):
            instance.foreground_color = (1, 0, 0, 1)
        else:
            instance.foreground_color = (0, 255, 0, 1)
            self.nom = value

    def getEmail(self, instance, value):
        """
        ---> Permet d'envoyer un code de validation par mail à l'utilisateur après une série de vérifications
             du format de l'adresse mail saisie.

             Pre: l'utilisateur doit au préalable avoir saisi un prénom et un nom valides.
             Post: renvoie un mail à l'adresse mail saisie avec un code de validation.
             Raise: IndexError si l'utilisateur valide un champ mail et que les champs prenom et noms sont vides.
        """
        prenom = self.prenom.lower()

        try:
            # check if the email format is ok
            if checkEmailValidation(prenom, value) and self.nom != "":
                if not checkAccount(self.email_input.text):
                    instance.foreground_color = (0, 255, 0, 1)

                    # envoi d'un code de validation à l'utilisateur
                    self.code_mail = get_email_validation(value)
                    self.code_input.disabled = False
                    self.code_validation_message.text = "Un code de validation vous a été envoyé"
                    self.email_input.disabled = True
                    self.prenom_input.disabled = True
                    self.nom_input.disabled = True
                else:
                    instance.foreground_color = (1, 0, 0, 1)
                    self.code_validation_message.text = "Adresse déja utilisée..."
            else:
                instance.foreground_color = (1, 0, 0, 1)

        except IndexError:
            self.code_validation_message.text = "Veuillez au préalable avoir rempli votre prenom et nom"

    def checkCode(self, instance, value):
        """
        ---> Permet de vérifier l'identité de l'utilisateur via le code reçu sur son adresse mail personnelle.

             Pre: l'utilisateur doit au préalable avoir validé son adresse mail.
             Post: valide la saisie du code de validation.
        """

        # la valeur du code envoyé précédement par mail lors de la validation de l'email
        code = self.code_mail
        self.count += 1
        # si le code correspond, ---> code validé
        if self.count < 3:
            if int(value) == code:
                instance.foreground_color = (0, 255, 0, 1)
                self.check_code.text = "code validé"
                self.submit_code = True
                self.submit_mail = True
                self.code_input.disabled = True
                self.count = 0

            else:
                self.code_input.text = ""
                self.check_code.text = "veuillez réessayer..."
        else:
            self.check_code.text = "Nombre de tentatives dépassées..."
            self.code_input.disabled = True
            self.password_input.disabled = True
            self.check_password_input.disabled = True

    def getPassword(self, instance, value):
        """
        ---> Permet la création d'un mot de passe pour le compte du nouvel utilisateur.

             Pre: le mot de passe doit respecter les règles de robustesses définies.
             Post: valide la saisie du mot de passe de l'utilisateur.
        """
        self.password_input_message.text = "Veuillez saisir un mot-de-pass avec au moins : (1 Maj, Chiffre et " \
                                           "1 caractère spécial) "
        if checkPassword(value):
            instance.foreground_color = (0, 255, 0, 1)
            self.password_input_message.text = "password assez robuste"
            self.password = value

        else:
            self.password_input_message.text = "Veuillez saisir un mot-de-pass avec au moins : (1 Maj, Chiffre et " \
                                               "1 caractère spécial) "

    def checkPassword(self, instance, value):
        """
        ---> Permet de confirmer le mot de passe saisi par l'utilisateur.

             Pre: un mot de passe valable doit au préalable avoir été crée.
             Post: valide la conformité des 2 mots de passe saisis dans les champs input adéquats.
        """
        if value == self.password:
            instance.foreground_color = (0, 255, 0, 1)
            self.check_password_message.text = "mot de passe confirmé"
            self.submit_password = True
            self.password_input.disabled = True
            self.check_password_input.disabled = True

        else:
            self.check_password_message.text = "Veuillez saisir le même mot de passe que celui choisi précédemment."

    def Submit(self):
        """
        ---> Fonction permettant de soumettre les données a la base de données pour achever l'inscription
             de l'utilisateur.

             Pre: l'email, le code de validation et le Mot de passe doivent au préalable avoir été vérifiés et validés.
             Post: crée une connexion avec le serveur de base de donnée et enregistre les données dans
             la collection adéquate.

        """
        if self.submit_code and self.submit_mail and self.submit_password:
            user_name = self.prenom_input.text[0] + "." + self.nom_input.text
            mail = self.email_input.text
            hash_pswd = hashPassword(self.password_input.text)
            submit_data_DB(mail=mail, password=hash_pswd, user_name=user_name)
            wm = App.get_running_app().root
            wm.current = 'programWindow'
        else:
            pass

    def clear(self):
        """
        ---> Fonction permettant de réinitialiser le formulaire d'inscription.

             Pre: -
             Post: Supprime le contenu des champs input.
        """

        self.email_input.text = ""
        self.prenom_input.text = ""
        self.nom_input.text = ""
        self.code_input.text = ""
        self.password_input.text = ""
        self.check_password_input.text = ""

        self.email_input.disabled = False
        self.prenom_input.disabled = False
        self.nom_input.disabled = False
        self.code_input.disabled = True
        self.password_input.disabled = False
        self.check_password_input.disabled = False

        self.code_validation_message.text = ""
        self.check_code.text = ""
        self.password_input_message.text = "Un mot de passe robuste (Maj, chiffre et caractère spécial)"
        self.check_password_message.text = ""


class programWindow(Screen):
    """
    ---> Fenêtre kivy contenant le programme après inscription ou connexion.

         Pre: -
         Post: -
    """
    pass


class WindowManager(ScreenManager):
    """
    ---> Permet la gestion des interactions entre les différentes fenêtres kivy du programme.

         Pre: -
         Post: -
    """
    Window.size = (1000, 700)


kv = Builder.load_file('Main.kv')


class MainApp(App):
    def build(self):
        return kv


if __name__ == '__main__':
    MainApp().run()
