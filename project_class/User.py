class User:
    def __init__(self, email, pswd):
        self.__email = email
        self.__pswd = pswd

    @property
    def get_email(self):
        return self.__email

    @property
    def get_pswd(self):
        return self.__pswd

