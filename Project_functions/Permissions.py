from mongo.mongoConnector import *
"""
- 0_Guest, 1_Member, 2_Admin --> [1,0,0,0,0,0,0], [1,1,1,0,0,0,0], [1,1,1,1,1,1,1]
- Crée un serveur, perm de ce serveur ADMIN
- [lire, écrire, "partage de fichier", ajouter membre, modifier role de qq, supprimer qq, modification de channel]
"""

def on_join(userID, serverID):
    """
        ---> Permet de définir le rôle d'un nouveau membre sur un serveur à invité.

             Pre: Adresse email d'un utilisateur spécifique. (string)
             Post: Identifiant d'un serveur spécifique. (string)
             Raise: ?
        """
    try:
        with MongoConnector() as connector:
            collection = connector.db["role_user"]
            collection.insert_one({"server": serverID, "user": userID, "role": 0})
    except Exception as e:
        print(e)

def owner_server(userID, serverID):
    """
        ---> Permet de définir le rôle du créateur du serveur à admin.

             Pre: Adresse email d'un utilisateur spécifique. (string)
             Post: Identifiant d'un serveur spécifique. (string)
             Raise: ?
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
        Admin : True

        ---> Autorise la lecture. Pas utile pour le moment, mais dans le futur, peut permettre d'ajouter un groupe muet, et d'interdire à certaines personnes de communiquer.

             Pre: Adresse email d'un utilisateur spécifique. (string)
             Post: Identifiant d'un serveur spécifique. (string)
             Raise: ?
    """
    return True

def can_write(userID, serverID):
    """
        Guest : False
        Member : True
        Admin : True

        ---> Autorise l'écriture au membre si son groupe est l'un des groupes autorisés.

             Pre: Adresse email d'un utilisateur spécifique. (string)
             Post: Identifiant d'un serveur spécifique. (string)
             Raise: ?
    """
    try:
        with MongoConnector() as connector:
            collection = connector.db["role_user"]
            user = collection.find_one({"server": serverID, "user": userID})
    except Exception as e:
        print(e)

    if 0 < user["role"] < 3:
        return True
    else:
        return False

def can_join_file(userID, serverID):
    """
        Guest : False
        Member : True
        Admin : True

        ---> Autorise l'envoie de fichier au membre si son groupe est l'un des groupes autorisés.

             Pre: Adresse email d'un utilisateur spécifique. (string)
             Post: Identifiant d'un serveur spécifique. (string)
             Raise: ?
    """
    try:
        with MongoConnector() as connector:
            collection = connector.db["role_user"]
            user = collection.find_one({"server": serverID, "user": userID})
    except Exception as e:
        print(e)

    if 0 < user["role"] < 3:
        return True
    else:
        return False



def can_add(userID, serverID):
    """
        Guest : True
        Member : True
        Admin : True

        ---> Autorise un membre à ajouter des membres au serveur si son groupe y est autorisé.

             Pre: Adresse email d'un utilisateur spécifique. (string)
             Post: Identifiant d'un serveur spécifique. (string)
             Raise: ?
    """
    try:
        with MongoConnector() as connector:
            collection = connector.db["role_user"]
            user = collection.find_one({"server": serverID, "user": userID})
    except Exception as e:
        print(e)

    if user["role"] == 2:
        return True
    else:
        return False

def can_change_role(userID, serverID):
    """
        Guest : True
        Member : True
        Admin : True

        ---> Autorise un membre à changer le rôles des membres si son groupe y est autorisé.

             Pre: Adresse email d'un utilisateur spécifique. (string)
             Post: Identifiant d'un serveur spécifique. (string)
             Raise: ?
    """
    try:
        with MongoConnector() as connector:
            collection = connector.db["role_user"]
            user = collection.find_one({"server": serverID, "user": userID})
    except Exception as e:
        print(e)

    if user["role"] == 2:
        return True
    else:
        return False

def can_ban(userID, serverID):
    """
        Guest : True
        Member : True
        Admin : True

        ---> Autorise un membre à bannir des membres du serveur si son groupe y est autorisé.

             Pre: Adresse email d'un utilisateur spécifique. (string)
             Post: Identifiant d'un serveur spécifique. (string)
             Raise: ?
    """
    try:
        with MongoConnector() as connector:
            collection = connector.db["role_user"]
            user = collection.find_one({"server": serverID, "user": userID})
    except Exception as e:
        print(e)

    if user["role"] == 2:
        return True
    else:
        return False

def can_change_channel(userID, serverID):
    """
        Guest : True
        Member : True
        Admin : True

        ---> Autorise un membre à modifier un canal du serveur si son groupe y est autorisé.

             Pre: Adresse email d'un utilisateur spécifique. (string)
             Post: Identifiant d'un serveur spécifique. (string)
             Raise: ?
    """
    try:
        with MongoConnector() as connector:
            collection = connector.db["role_user"]
            user = collection.find_one({"server": serverID, "user": userID})
    except Exception as e:
        print(e)

    if user["role"] == 2:
        return True
    else:
        return False

def change_role(userID, serverID, roleID):
    """
        Guest : False
        Member : False
        Admin : False

        ---> Permet de changer le groupe d'un membre si il y est aurotisé.

             Pre: Adresse email d'un utilisateur spécifique. (string)
             Post: Identifiant d'un serveur spécifique. (string)
             Raise: ?
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

