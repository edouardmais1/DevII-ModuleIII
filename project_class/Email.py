from random import randint
import smtplib
import sys


class Email:
    def __init__(self):
        self.__userName = ""
        self.__emailEphec = ""

    def getEmail(self):
        """
        ---> retourne le mail de l'utilisateur
        """
        return self.__emailEphec

    def setEmail(self):
        """
        ---> méthode permettant d'obtenir l'adresse mail de l'utilisateur
        """
        self.__emailEphec = checkEmailValidation()

    def setUserName(self):
        """
        ---> méthode permettant d'obtenir les coordonées de l'utlisateur (nom et prénom)
        """
        prenom = get_prenom()
        nom = get_nom()
        self.__userName = prenom[0] + "." + nom

    def getUserName(self):
        return self.__userName


# ------------------Email Functions---------------------

def get_prenom():
    """
    ---> fonction permettant d'obtenir le prénom du nouvel utilisateur
    """
    out_input = -1

    while out_input < 0:
        prenom = input("Veuillez rentrer votre prenom: ")

        if any(elem.isdigit() for elem in prenom):
            print("Veuillez saisir un prénom valide ...")
            out_input = -1

        elif set('[~!@#$%^&*()_+{}":;\']+$').intersection(prenom):
            print("Veuillez saisir un prénom valide ...")
            out_input = -1

        else:
            out_validation = -1
            while out_validation < 0:
                validation_prenom = input("Veuillez valider le prénom saisi: ")

                if prenom == validation_prenom:
                    return validation_prenom.lower()

                else:
                    print("Veuillez réessayer ...")
                    out_validation = -1


def get_nom():
    """
    ---> fonction permettant d'obtenir le nom du nouvel utilisateur
    """
    out_input = -1

    while out_input < 0:
        nom = input("Veuillez rentrer votre nom: ")

        if any(elem.isdigit() for elem in nom):
            print("Veuillez saisir un nom valide ...")
            out_input = -1

        elif set('[~!@#$%^&*()_+{}":;\']+$').intersection(nom):
            print("Veuillez saisir un prénom valide ...")
            out_input = -1

        else:
            out_validation = -1
            while out_validation < 0:
                validation_nom = input("Veuillez valider le nom saisi: ")

                if nom == validation_nom:
                    return validation_nom.lower()

                else:
                    print("veuillez réessayer...")
                    out_validation = -1


def get_email_validation(email):
    """
    ---> fonction permettant d'envoyer un mail à l'utilisateur muni d'un code de vérification de l'email afin de
         de vérifier l'identité de l'utilisateur.
    """
    validation_code = randint(1000, 9999)

    sender_address = "noreply@revosta.com"
    receiver_address = email
    account_password = "xso4%J91"
    subject = "Email verification"
    body = "Salut poto!\n\nEntre ce code pour verifier ton compte : {}!\nWith regards,\n\tDeveloper".format(
        validation_code)

    with smtplib.SMTP_SSL("smtp.revosta.com", 465) as smtp_server:
        smtp_server.login(sender_address, account_password)
        message = f"Subject: {subject}\n\n{body}"

        smtp_server.sendmail(sender_address, receiver_address, message)
        return validation_code


def checkEmailValidation():
    """
    --->fonction permettant de vérifier le code envoyer par mail
    """
    email_prof = "@ephec.be"
    email_students = "@students.ephec.be"
    out_while = -1

    while out_while < 0:
        email = input(
            "veuillez saisir votre adresse ephec personnelle (élève : InitialePrenom.nom@students.ephec.be),"
            " (exit pour quitter) :")

        if email_prof in email or email_students in email:

            for i in range(2):
                print("un code vous à été envoyé par mail")
                code = get_email_validation(email)

                for j in range(3):
                    input_user = input("veuillez saisir le code recu par mail (4 chiffres), (exit pour quitter) :")

                    if input_user == "exit":
                        sys.exit()

                    elif int(input_user) == code:
                        return email

                    else:
                        pass
            print("Vous avez dépassé les tentatives autorisées...")
            sys.exit()

        elif email == "exit":
            sys.exit()

        else:
            print("Veuillez saisir une adresse valide...")
            out_while = -1
