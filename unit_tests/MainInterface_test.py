import unittest
from Project_functions.check import *
from Project_functions.Email import *
from Project_functions.Password import *
from mongo.mongoConnector import *


class test_checkValidPrenomNom(unittest.TestCase):
    def test_checkValidPrenomNom(self):
        self.assertEqual(checkValidPrenomNom("Maxime"), True, "Maxime est valide")
        self.assertEqual(checkValidPrenomNom("Edouard"), True, "Edouard est valide")
        self.assertEqual(checkValidPrenomNom("Max5"), False, "Présence d'un chiffre, non valide")
        self.assertEqual(checkValidPrenomNom("E"), False, "prenom ou nom trop court")
        self.assertEqual(checkValidPrenomNom("zdq*"), False, "présence d'un caractère spécial")


class test_checkEmailValidation(unittest.TestCase):
    def test_checkEmailValidation(self):
        self.assertEqual(checkEmailValidation("maxime", "m.momin@students.ephec.be"), True, "l'adresse est valide et "
                                                                                            "correspond au prénom")
        self.assertEqual(checkEmailValidation("edouard", "m.momin@students.ephec.be"), False, "le prenom et l'adresse "
                                                                                              "ne correspondent pas")
        self.assertEqual(checkEmailValidation("maxime", "m.momin@students.be"), False, "le format de l'adresse saisie "
                                                                                       "est invalide")


class test_checkPassword(unittest.TestCase):
    def test_checkPassword(self):
        self.assertEqual(checkPassword("Azerty1234*"), True, "le mot de passe est valide")
        self.assertEqual(checkPassword("Azerty"), False, "le mot de passe ne contient pas de caractère spécial")
        self.assertEqual(checkPassword("1234"), False, "le mot de passe n'est pas valide (taille, caractères)")
        self.assertEqual(checkPassword("123*azerty"), False, "le mot de passe ne contient pas de majuscule")


class test_checkAccount(unittest.TestCase):
    def test_checkAccount(self):
        self.assertEqual(checkAccount("m.momin@students.ephec.be"), True, "l'email éxiste dans la db")
        self.assertEqual(checkAccount("Edouard"), False, "l'utilisateur n'éxiste pas dans la db")
        self.assertEqual(checkAccount("Edouard@students.ephec"), False, "l'utilisateur n'éxiste pas dans la db")

    def test_raises_connexion(self):
        self.assertRaises(Exception, checkAccount(""), "Exception")


class test_connexion(unittest.TestCase):
    def test_connexion(self):
        self.assertEqual(connexion("m.momin@students.ephec.be", hashPassword("Azerty123*")), True, "le compte et le "
                                                                                                   "mot de passe "
                                                                                                   "associé sont "
                                                                                                   "valides et "
                                                                                                   "éxistent dans la "
                                                                                                   "db")

        self.assertEqual(connexion("lou@students.ephec.be", hashPassword("Azerty123*")), False, "le compte et le mot "
                                                                                                "de passe associé "
                                                                                                "n'éxistent pas dans "
                                                                                                "la db")

        self.assertEqual(connexion("lou@ephec.be", hashPassword("Azerty123*")), False, "le compte et le mot de passe "
                                                                                       "associé n'existent pas dans "
                                                                                       "la db")

    def test_raises_connexion(self):
        self.assertRaises(Exception, connexion("", hashPassword("")), "Exception")


if __name__ == '__main__':
    unittest.main()
