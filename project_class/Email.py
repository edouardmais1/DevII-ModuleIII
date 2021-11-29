class Email:
    def __init__(self):
        self.__userName = ''
        self.__emailEphec = ''

    def getEmail(self):
        return self.__emailEphec

    def getUserName(self):
        return self.__userName

    def setEmail(self):
        pass


    def setUserName(self):
        prenom = get_prenom()
        nom = get_nom()
        self.__userName = prenom[0] + "." + nom

    def checkEmail(self, emailEphec):
        pass



#comment vérifier si le prenom et le nom appartiennent à un éleve ?

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
                    return validation_prenom

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
                    return validation_nom

                else:
                    print("veuillez réessayer...")
                    out_validation = -1

test = Email()
test.setUserName()
print(test.getUserName())