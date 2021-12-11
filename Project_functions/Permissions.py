class Permissions:
    def __init__(self):
        self.__superAdmin = [1,1,1,1]
        self.__admin = [1,1,1,0]
        self.__member = [1,1,0,0]
        self.__visitor = [1,0,0,0]

    def get_role (self, rang):
        if rang == 3:
            return self.__superAdmin
        if rang == 2:
            return self.__admin
        if rang == 1:
            return self.__member
        if rang == 0:
            return self.__visitor