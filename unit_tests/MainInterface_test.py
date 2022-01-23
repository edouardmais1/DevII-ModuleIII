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
        self.assertEqual(checkValidPrenomNom("E"), False, "False")
        self.assertEqual(checkValidPrenomNom("zdq*"), False, "False")


class test_checkEmailValidation(unittest.TestCase):
    def test_checkEmailValidation(self):
        self.assertEqual(checkEmailValidation("maxime", "m.momin@students.ephec.be"), True, "True")
        self.assertEqual(checkEmailValidation("edouard", "m.momin@students.ephec.be"), False, "False")
        self.assertEqual(checkEmailValidation("maxime", "m.momin@students.be"), False, "False")


class test_checkPassword(unittest.TestCase):
    def test_checkPassword(self):
        self.assertEqual(checkPassword("Azerty1234*"), True, "True")
        self.assertEqual(checkPassword("Azerty"), False, "False")
        self.assertEqual(checkPassword("1234"), False, "False")
        self.assertEqual(checkPassword("123*azerty"), False, "False")


class test_checkAccount(unittest.TestCase):
    def test_checkAccount(self):
        self.assertEqual(checkAccount("m.momin@students.ephec.be"), True, "True")
        self.assertEqual(checkAccount("Edouard"), False, "False")
        self.assertEqual(checkAccount("Edouard@students.ephec"), False, "False")

    def test_raises_connexion(self):
        self.assertRaises(Exception, checkAccount(""), "Exception")


class test_connexion(unittest.TestCase):
    def test_connexion(self):
        self.assertEqual(connexion("m.momin@students.ephec.be", hashPassword("Azerty123*")), True, "True")
        self.assertEqual(connexion("lou@students.ephec.be", hashPassword("Azerty123*")), False, "False")
        self.assertEqual(connexion("lou@ephec.be", hashPassword("Azerty123*")), False, "False")

    def test_raises_connexion(self):
        self.assertRaises(Exception, connexion("", hashPassword("")), "Exception")




if __name__ == '__main__':
    unittest.main()
