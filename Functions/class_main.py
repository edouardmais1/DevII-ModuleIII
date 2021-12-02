from Functions.gestion_files import *
from project_class.Email import *
from project_class.Password import *


def inscription(chemin_main):
    '''
    ---> gère l'inscription de l'utilisateur
    ---> appel fonction check_email_validation -> vérifier si le champ saisi est de type mail.
    ---> appel fonction check_email_exist -> vérifier si l'email saisi éxiste ou non.
    ---> appel fonction inscription_pswd -> créer un mdp pour l'utilisteur lors de son inscription.

    Pre :   1) l'utilisateur doit respecter les conditions demandées lors de l'input.
            2) l'email saisi doit etre sous un format 'email'.

    Post : -
    '''
    path = chemin_main
    new_email = Email()
    new_email.setUserName()
    email = new_email.setEmail()
    if not check_email_exist(path, 'Data', file="DataBase", email=email):
        new_password = Password()
        new_password.setPassword()
        print(new_email.getEmail())
        print(str(new_password.getPassword()))
        write_file(path, 'Data', file="DataBase", email=new_email.getEmail(),
                   password=new_password.getPassword())
        print("Votre inscription a bien été enregistrée !\n")

def connexion(chemin_main):
    pass