# -*- coding: utf-8 -*-
def checkValidPrenomNom(value):
    """
        ---> Permet de vérifier la validité d'un nom/prénom.

        Pre: l'utilisateur doit rentrer un nom valide (pas de caractères spéciaux et chiffres).
        Post: valide (True) ou non (False) la saisie de l'utilisateur.
    """
    if any(elem.isdigit() for elem in value):
        return False
    elif set('[~!@#$%^&*()_+{}":;\']+$').intersection(value):
        return False
    elif len(value) < 2:
        return False
    elif len(value) >= 20:
        return False
    else:
        return True

