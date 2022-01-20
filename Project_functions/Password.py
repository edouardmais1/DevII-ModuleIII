import re
import hashlib


# ------------------Password Functions---------------------


def hashPassword(password):
    """
    ---> fonction permettant de hasher le mot de passe saisi par l'utilisateur pour augmenter la sécurité du système.

         Pre : /

         Post : /
    """
    return hashlib.md5(password.encode()).hexdigest()


def checkPassword(pswd):
    """
    ---> fonction permettant à l'utilisateur d'entrer un mot de passe et le valider.

         Pre : le mot de passe saisi doit contenir au moins une Majuscule, un caractère spécial, un chiffre et
         contenir au mois 9 caractères.

         Post : renvoi True si le mot de passe est valide et False dans le cas contraire.
    """

    if re.search('[A-Z]', pswd) is None or re.search('[0-9]', pswd) is None or \
            not set('[~!@#$%^&*()_+{}":;\']+$').intersection(pswd) or len(pswd) < 9:
        return False

    else:
        return True
