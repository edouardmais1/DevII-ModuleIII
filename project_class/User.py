from Email import *
from Password import *
from Permissions import *
class User:
    def __init__(self, email : Email, password : Password, permissions : Permissions):
        self.__email = email
        self.__password = password
        self.__role = permissions

    def getEmail(self):
        return self.__email.getEmail()

    def getPassword(self):
        return self.__password

    def getRole(self):
        return self.__role
