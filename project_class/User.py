from Email import *
from Password import *
from Permissions import *
class User:

    def __init__(self, email : Email, password : Password):
        self.__email = email
        self.__password = password

    def getEmail(self):
        return self.__email.getEmail()

    def getPassword(self):
        return self.__password
