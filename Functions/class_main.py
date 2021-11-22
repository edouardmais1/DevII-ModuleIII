import hashlib
from easygui import passwordbox
from Functions.gestion_files import *
import sys
import os


def login(chemin_main):
    '''
    ---> main function : lance le programme principal.
    ---> demande a l'utilisateur de se connecter ou s'inscrire et lance des appels aux fonctions adéquates.

    Pre :   - user_input doit valoir I/inscription ou C/connexion.
    Post :  -
    '''
    path = chemin_main
    while True:
        user_input = input("Inscription/Connexion: ")
        if user_input == "Inscription" or user_input == "inscription":
            inscription(path)

        if user_input == "Connexion" or user_input == "connexion":
            connexion(path)
        if user_input == "exit()":
            break


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
    sortir_inscription = -1

    while sortir_inscription < 0:
        email = input("Veuillez saisir une adresse email valide (@ephec): ")
        if (email == "exit()"):
            break
        if check_email_validation(email):
            if not check_email_exist(path, 'Data', file="DataBase", email=email):
                check_inscription_pswd = inscription_pswd(chemin_main)
                if check_inscription_pswd:
                    write_file(path, 'Data', file="DataBase", email=email, password=check_inscription_pswd.hexdigest())
                    print("Votre inscription a bien été enregistrée !\n")
                    sortir_inscription = 1

            else:
                print("L'adresse saisie éxiste déja...\nVeuillez réessayer: ")
                sortir_inscription = -1

        else:
            print("Veuillez saisir une adresse mail valide...")
            sortir_inscription = -1


def inscription_pswd(chemin_main):  #optimiser le check du password (caractères spéciaux, Maj, taille du mdp)
    '''
    ---> fonction permettant a l'utilisateur de créer son mot de passe pour s'identifier par la suite

    :return: le mot de passe saisi hashé si les conditions de remplissage sont respectées.

    Pre :   1) le mot de passe != None
            2) les 2 mots de passe saisis doivent etre identiques.

    Post : renvoi le mot de passe si hash_pswd == hash__pswd
    '''
    path = chemin_main
    out_password = -1

    while out_password < 0:
        try:
            pswd = passwordbox('Password: ')
            if pswd == "exit()":
                break
            hash_pswd = hashlib.md5(pswd.encode())
            check_pswd = passwordbox('Check Password: ')
            if check_pswd == "exit()":
                break
            hash_check_pswd = hashlib.md5(check_pswd.encode())
            if hash_check_pswd.hexdigest() == hash_pswd.hexdigest():
                out_password = 1
                return hash_pswd
            else:
                print("Veuillez saisir 2 fois le même mot de passe: ")
                out_password = -1

        except AttributeError:
            print("Vous avez quitté la saisie du mot de passe.")
            login(path)
            out_password = 1

        except IOError:
            print("Une erreur s'est produite...")


def connexion(chemin_main):
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
    path = chemin_main + "\\" + 'Data' + "\\" + 'DataBase'
    try:
        with open(path) as file:
            for line in file:
                tab.append(line.rstrip().split())

            for elem in tab:
                dict[elem[0]] = elem[1]

    except FileNotFoundError:
        print('Fichier introuvable')

    except IOError:
        print("Impossible d'ouvrir le fichier...")

    except IndexError:
        pass

    out_connexion = -1
    while out_connexion < 1:

        email = input("Veuillez saisir une adresse valide: ")
        if email == "exit()":
            break
        if check_email_exist(chemin_main, 'Data', file="DataBase", email=email):

            email_valide = email

            out_password = -1
            while out_password < 0:
                try:
                    password = passwordbox('Password: ')

                    if hashlib.md5(password.encode()).hexdigest() == dict[email_valide]:
                        print("Vous êtes connectés !")
                        out_password = 1
                        out_connexion = 1

                        sys.exit()

                    else:
                        print("Mot de passe ou adresse email invalide...")
                        out_password = -1

                except AttributeError:
                    print("Vous avez quitté la saisie de mot de passe.")
                    out_password = -1

                except IOError:
                    print("Une erreur s'est produite.")

        else:
            print("Adresse email introuvable...")
            out_connexion = -1
