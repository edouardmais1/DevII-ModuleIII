import re
import getpass
import hashlib
import sys


class Password:
    def __init__(self):
        self.__password = ""

    def getPassword(self):
        return self.__password

    def setPassword(self):
        self.__password = hashPassword(checkPassword())


def hashPassword(password):
    """
    ---> fonction permettant de hasher le mot de passe saisi par l'utilisateur pour augmenter la sécurité du système
    """
    return hashlib.md5(password.encode()).hexdigest()


def checkPassword():
    """
    ---> fonction permettant à l'utilisateur d'entrer un mot de passe et le valider
    """
    # path = chemin_main
    out_password = -1
    while out_password < 0:
        # pswd = getpass.getpass('Password (1 Maj., 1 chiffre, 1 caractère spécial, min. 9 caractères): ')

        pswd = input('Password (1 Maj., 1 chiffre, 1 caractère spécial, min. 9 caractères): ')

        if pswd == "exit":
            sys.exit(0)

        if re.search('[A-Z]', pswd) == None or re.search('[0-9]', pswd) == None or \
                not set('[~!@#$%^&*()_+{}":;\']+$').intersection(pswd) or len(pswd) < 9:
            out_password = -1

        else:
            out_check_password = -1
            while out_check_password < 0:
                # check_pswd = getpass.getpass("Vérifier votre password: ")
                check_pswd = input("Vérifier votre password: ")
                if check_pswd == "exit":
                    sys.exit(0)
                if check_pswd == pswd:
                    return pswd
