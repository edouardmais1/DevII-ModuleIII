from mongo.mongoConnector import *
"""
- 0_Guest, 1_Member, 2_Admin --> [1,0,0,0,0,0,0], [1,1,1,0,0,0,0], [1,1,1,1,1,1,1]
- Crée un serveur, perm de ce serveur ADMIN
- [lire, écrire, "partage de fichier", ajouter membre, modifier role de qq, supprimer qq, modification de channel]
"""

def on_join(userID, serverID):
    """
        Set role to Guest
        PRE :
            userID : string -> Email address of a specific user
            serverID : string -> ID of a specific server
        POST :
            return 0
    """
    try:
        with MongoConnector() as connector:
            collection = connector.db["role_user"]
            collection.insert_one({"server": serverID, "user": userID, "role": 0})
    except Exception as e:
        print(e)
    return 0

def owner_server(userID, serverID):
    """
        Guest : True
        Member : True
        Admin : True,
    """
    try:
        with MongoConnector() as connector:
            collection = connector.db["role_user"]
            collection.insert_one({"server": serverID, "user": userID, "role": 2})
    except Exception as e:
        print(e)

def can_read(userID, serverID):
    """
        Guest : True
        Member : True
        Admin : True,
    """
    return True

def can_write(userID, serverID):
    """
        Guest : True
        Member : True
        Admin : True,
    """
    try:
        with MongoConnector() as connector:
            collection = connector.db["role_user"]
            user = collection.find_one({"server": serverID, "user": userID})
    except Exception as e:
        print(e)

    if user["role"] > 0:
        return True
    else
        return False


def can_join_file(userID, serverID):
    """
        Guest : True
        Member : True
        Admin : True,
    """


def can_add(userID, serverID):
    """
        Guest : True
        Member : True
        Admin : True,
    """


def can_change_role(userID, serverID):
    """
        Guest : True
        Member : True
        Admin : True,
    """


def can_ban(userID, serverID):
    """
        Guest : True
        Member : True
        Admin : True,
    """


def can_change_channel(userID, serverID):
    """
        Guest : True
        Member : True
        Admin : True,
    """

def change_role(userID, serverID, roleID):
    """
        Guest : True
        Member : True
        Admin : True,
    """
    if can_change_role(userID, serverID):
        try:
            with MongoConnector() as connector:
                collection = connector.db["role_user"]
                collection.replace_one(
                    {"server": serverID, "user": userID},
                    {"server": serverID, "user": userID, "role": roleID}
                )
        except Exception as e:
            print(e)
    else:
        print("Erreur. Vous n'avez pas l'autorisation nécessaire afin de changer un rôle.")
        return 1

