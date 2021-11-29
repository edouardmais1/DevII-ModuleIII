class Permissions:
    def __init__(self):
        self.__superAdmin = []
        self.__admin = []
        self.__member = []
        self.__visitor = []

    def getPermsSuperAdmin(self):
        return self.__superAdmin

    def getPermsAdmin(self):
        return self.__admin

    def getPermsMember(self):
        return self.__member

    def getPermsVisitor(self):
        return self.__visitor