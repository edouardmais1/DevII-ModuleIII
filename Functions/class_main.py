from Functions.gestion_files import *
from project_class.User import *
from project_class.Email import *
from project_class.Password import *


def inscription():
    '''
    ---> gère l'inscription de l'utilisateur
    ---> pour l'instant, les utilisateur sont stockés dans un fichier texte car MongoDB n'est pas implémenté
    '''
    new_email = Email()
    new_email.setUserName()
    email = new_email.setEmail()

    if not check_email_exist(path, 'Data', file="DataBase", email=email):
        new_password = Password()
        new_password.setPassword()
        print(new_email.getEmail())
        print(str(new_password.getPassword()))

        utilisateur = User(new_email.getEmail(), new_password.getPassword())
        write_file(path, 'Data', file="DataBase", email=utilisateur.getEmail(),
                   password=utilisateur.getPassword())

        print("Votre inscription a bien été enregistrée !\n")


def connexion():
    pass
