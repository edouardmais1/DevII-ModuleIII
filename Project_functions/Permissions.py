from mongo.mongoConnector import *
"""
- 0_Guest, 1_Member, 2_Admin --> [1,0,0,0,0,0,0], [1,1,1,0,0,0,0], [1,1,1,1,1,1,1]
- Crée un serveur, perm de ce serveur ADMIN
- [lire, écrire, "partage de fichier", ajouter membre, modifier role de qq, supprimer qq, modification de channel]
- Perm: def owner_server(), def can_read(), def can_write(), def can_join_file(), def can_add(), def can_change_role(), def can_ban(), def can_change_channel()
"""

def on_join(userID, serverID):
    try:
        with MongoConnector() as connector:
            collection = connector.db["role_user"]
            collection.insert_one({"server": serverID, "user": userID, "role": 0})
    except Exception as e:
        print(e)

def owner_server(userID, serverID):
    try:
        with MongoConnector() as connector:
            collection = connector.db["role_user"]
            collection.insert_one({"server": serverID, "user": userID, "role": 2})
    except Exception as e:
        print(e)

def can_read(userID, serverID):




def can_write(userID, serverID):


def can_join_file(userID, serverID):


def can_add(userID, serverID):


def can_change_role(userID, serverID):


def can_ban(userID, serverID):


def can_change_channel(userID, serverID):

def change_role(userID, serverID, roleID):
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

