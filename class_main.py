import hashlib
from easygui import passwordbox
from gestion_files import *
import sys


def login():
    '''
    ---> main function : lance le programme principal.
    ---> demande a l'utilisateur de se connecter ou s'inscrire et lance des appels aux fonctions adéquates.

    Pre :   - user_input doit valoir I/inscription ou C/connexion.
    Post :  -
    '''

    while True:
        user_input = input("Inscription/Connexion: ")
        if user_input == "Inscription" or user_input == "inscription":
            inscription()

        if user_input == "Connexion" or user_input == "connexion":
            connexion()


def inscription():
    '''
    ---> gère l'inscription de l'utilisateur
    ---> appel fonction check_email_validation -> vérifier si le champ saisi est de type mail.
    ---> appel fonction check_email_exist -> vérifier si l'email saisi éxiste ou non.
    ---> appel fonction inscription_pswd -> créer un mdp pour l'utilisteur lors de son inscription.

    Pre :   1) l'utilisateur doit respecter les conditions demandées lors de l'input.
            2) l'email saisi doit etre sous un format 'email'.

    Post : -
    '''
    sortir_inscription = -1

    while sortir_inscription < 0:
        email = input("veuillez saisir une adresse email valide (@ephec) :")

        if check_email_validation(email):

            if not check_email_exist(file="DataBase", email=email):
                check_inscription_pswd = inscription_pswd()
                if check_inscription_pswd:
                    write_file(file="DataBase", email=email, password=check_inscription_pswd.hexdigest())
                    print("Votre inscription a bien été enregistrée ! \n")
                    sortir_inscription = 1

            else:
                print("l'adresse saisie éxiste déja... veuillez réessayer :")
                sortir_inscription = -1

        else:
            print("veuillez saisir une adresse mail valide...")
            sortir_inscription = -1


def inscription_pswd():
    '''
    ---> fonction permettant a l'utilisateur de créer son mot de passe pour s'identifier par la suite

    :return: le mot de passe saisi hashé si les conditions de remplissage sont respectées.

    Pre :   1) le mot de passe != None
            2) les 2 mots de passe saisis doivent etre identiques.

    Post : renvoi le mot de passe si hash_pswd == hash__pswd
    '''

    out_password = -1

    while out_password < 0:
        try:
            pswd = passwordbox('Password: ')
            hash_pswd = hashlib.md5(pswd.encode())
            check_pswd = passwordbox('Check Password: ')
            hash_check_pswd = hashlib.md5(check_pswd.encode())
            if hash_check_pswd.hexdigest() == hash_pswd.hexdigest():
                out_password = 1
                return hash_pswd
            else:
                print("veuillez saisir 2 fois le meme mot de passe")
                out_password = -1

        except AttributeError:
            print("vous avez quitté la saisie du mot de passe")
            login()
            out_password = 1

        except IOError:
            print("une erreur s'est produite...")


def connexion():
    '''
    ---> fonction qui permet à, l'utilisateur de se loguer.
    ---> appel fonction check_email_exist pour vérifier si l'email saisi est valide.
    ---> si l'email est valide, série de test pour vérifier si le mot de passe correspond.
         s'il correspond, l'utilisateur est logué, sinon il doit réessayer jusqu'a fournir le mdp correct.

    Pre :   1) le champs saisi doit se trouver dans la base de données (DataBase).

    Post : -
    '''
    tab = []
    dict = {}

    try:
        with open("DataBase") as file:
            for line in file:
                tab.append(line.rstrip().split())

            for elem in tab:
                dict[elem[0]] = elem[1]

    except FileNotFoundError:
        print('fichier introuvable')

    except IOError:
        print("impossible d'ouvrir le fichier...")

    except IndexError:
        pass

    out_connexion = -1
    while out_connexion < 1:

        email = input("veuillez saisir une adresse valide :")

        if check_email_exist(file="DataBase", email=email):

            email_valide = email

            out_password = -1
            while out_password < 0:
                try:
                    password = passwordbox('Password :')

                    if hashlib.md5(password.encode()).hexdigest() == dict[email_valide]:
                        print("vous etes connectés")
                        out_password = 1
                        out_connexion = 1

                        sys.exit()

                    else:
                        print("mot de passe ou email invalide...")
                        out_password = -1

                except AttributeError:
                    print("vous avez quitté la saisie de mot de passe")
                    out_password = -1

                except IOError:
                    print("une erreur s'est produite")

        else:
            print("adresse email introuvable... veuillez réessayer")
            out_connexion = -1