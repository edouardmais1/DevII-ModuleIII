class User:
    def __init__(self, email, password):
        self.__email = email
        self.__password = password

    def getEmail(self):
        return self.__email

    def getPassword(self):
        return self.__password
