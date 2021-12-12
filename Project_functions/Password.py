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


def checkPassword(pswd):
    """
    ---> fonction permettant à l'utilisateur d'entrer un mot de passe et le valider
    """

    if re.search('[A-Z]', pswd) == None or re.search('[0-9]', pswd) == None or \
            not set('[~!@#$%^&*()_+{}":;\']+$').intersection(pswd) or len(pswd) < 9:
        return False

    else:
        return True
