from random import randint
import smtplib


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

    def setUserName(self, nom, prenom):
        """
        ---> méthode permettant d'obtenir les coordonées de l'utlisateur (nom et prénom)
        """
        self.__userName = prenom[0] + "." + nom

    def getUserName(self):
        return self.__userName


# ------------------Email Functions---------------------


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


def checkEmailValidation(prenom, mail):
    """
    --->fonction permettant de vérifier le format de l'adresse mail saisie par l'utilisateur
    """
    email_prof = "@ephec.be"
    email_students = "@students.ephec.be"

    if prenom[0] == mail[0]:
        if email_prof in mail or email_students in mail:
            return True

        else:
            return False

    else:
        return False




