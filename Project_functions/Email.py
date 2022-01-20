from random import randint
import smtplib


# ------------------Email Functions---------------------


def get_email_validation(email):
    """
    ---> Fonction permettant d'envoyer un mail à l'utilisateur muni d'un code de vérification afin de
         de vérifier l'identité de l'utilisateur.

         Pre : l'email doit au préalable avoir été valider par la fonction checkEmailValidation().
         Post : renvoie un code de validation à l'adresse email saisie.
    """
    # nombre aléatoire entre 1000 et 9999
    validation_code = randint(1000, 9999)
    sender_address = "noreply@revosta.com"
    receiver_address = email
    account_password = "3Il1r@c921yrfW9$"
    subject = "Email verification"
    body = "Bonjour !\n\nEntrez ce code pour verifier votre compte : {}!\nRemerciemments,\n\tDevelopers".format(
        validation_code)

    with smtplib.SMTP_SSL("smtp.revosta.com", 465) as smtp_server:
        smtp_server.login(sender_address, account_password)
        message = f"Subject: {subject}\n\n{body}"
        smtp_server.sendmail(sender_address, receiver_address, message)
        return validation_code


def checkEmailValidation(prenom, mail):
    """
    ---> Fonction permettant de vérifier le format de l'adresse mail saisie par l'utilisateur

        Pre: -
        Post: renvoie True si le format de l'adresse mail saisie respecte le format demandé, sinon False.
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
