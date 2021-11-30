from random import randint

class Email:
    def __init__(self):
        self.__userName = ""
        self.__emailEphec = ""

    def getEmail(self):
        return self.__emailEphec

    def setEmail(self):
        correct_mail = str(self.__userName) + "@students.ephec.be"
        out_input = -1
        while out_input < 0:
            email = input("veuillez saisir votre adresse mail ephec personnelle (InitialePrenom.Nom@students.ephec.be :")

            if email == correct_mail:
                return True

            else:
                print("email saisi non conforme aux données rentrées")
                out_input = -1


    def setUserName(self):
        prenom = get_prenom()
        nom = get_nom()
        self.__userName = prenom[0] + "." + nom

    def getUserName(self):
        return self.__userName




#------------------Email Functions---------------------

def get_prenom():
    """
    ---> fonction permettant d'obtenir le prénom du nouvel utilisateur
    """
    out_input = -1

    while out_input < 0:
        prenom = input("veuillez rentrer votre prenom :")

        if any(elem.isdigit() for elem in prenom):
            print("veuillez saisir un prénom valide...")
            out_input = -1

        else:
            out_validation = -1
            while out_validation < 0:
                validation_prenom = input("veuillez valider le prénom saisi :")

                if prenom == validation_prenom:
                    return validation_prenom.lower()

                else:
                    print("veuillez réessayer...")
                    out_validation = -1


def get_nom():
    """
    ---> fonction permettant d'obtenir le nom du nouvel utilisateur
    """
    out_input = -1

    while out_input < 0:
        nom = input("veuillez rentrer votre nom :")

        if any(elem.isdigit() for elem in nom):
            print("veuillez saisir un nom valide...")
            out_input = -1

        else:
            out_validation = -1
            while out_validation < 0:
                validation_nom = input("veuillez valider le nom saisi :")

                if nom == validation_nom:
                    return validation_nom.lower()

                else:
                    print("veuillez réessayer...")
                    out_validation = -1


def get_email_validation():

    validation_code = randint(1000, 9999)
    return validation_code


print(get_email_validation())