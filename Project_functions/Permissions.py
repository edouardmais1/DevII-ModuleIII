# -*- coding: utf-8 -*-
from mongo.mongoConnector import *


def on_join(userID, serverID):
    """
        ---> Permet de définir le rôle d'un nouveau membre sur un serveur à invité.

             Pre: Adresse email d'un utilisateur spécifique. (string)
             Post: Identifiant d'un serveur spécifique. (string)
        """
    try:
        with MongoConnector() as connector:
            collection = connector.db["role_user"]
            collection.insert_one({"server": serverID, "user": userID, "role": 0})
    except Exception as e:
        print(e)


def owner_server(user_id, server_id):
    """
        ---> Permet de définir le rôle du créateur du serveur à admin.

             Pre: Adresse email d'un utilisateur spécifique. (string)
             Post: Identifiant d'un serveur spécifique. (string)
    """
    try:
        with MongoConnector() as connector:
            collection = connector.db["role_user"]
            collection.insert_one({"server": server_id, "user": user_id, "role": 2})
    except Exception as e:
        print(e)


def can_read(user_id, server_id):
    """
        Guest : True
        Member : True
        Admin : True

        ---> Autorise la lecture. Pas utile pour le moment, mais dans le futur, peut permettre d'ajouter un groupe muet,
         et d'interdire à certaines personnes de communiquer.

             Pre: Adresse email d'un utilisateur spécifique. (string)
             Post: Identifiant d'un serveur spécifique. (string)
    """
    try:
        with MongoConnector() as connector:
            collection = connector.db["role_user"]
            user = collection.find_one({"server": server_id, "user": user_id})

    except Exception as e:
        print(e)

    if user is not None:
        return True
    else:
        return False


def can_write(user_id, server_id):
    """
        Guest : False
        Member : True
        Admin : True

        ---> Autorise l'écriture au user si son groupe est l'un des groupes autorisés.

             Pre: Adresse email d'un utilisateur spécifique. (string)
             Post: Identifiant d'un serveur spécifique. (string)
    """
    try:
        with MongoConnector() as connector:
            collection = connector.db["role_user"]
            user = collection.find_one({"server": server_id, "user": user_id})
    except Exception as e:
        print(e)

    if user is not None:
        if 0 < user["role"] < 3:
            return True
        else:
            return False
    else:
        return False


def can_join_file(user_id, server_id):
    """
        Guest : False
        Member : True
        Admin : True

        ---> Autorise l'envoie de fichier au user si son groupe est l'un des groupes autorisés.

             Pre: Adresse email d'un utilisateur spécifique. (string)
             Post: Identifiant d'un serveur spécifique. (string)
    """
    try:
        with MongoConnector() as connector:
            collection = connector.db["role_user"]
            user = collection.find_one({"server": server_id, "user": user_id})
    except Exception as e:
        print(e)

    if user is not None:
        if 0 < user["role"] < 3:
            return True
        else:
            return False
    else:
        return False


def can_add(user_id, server_id):
    """
        Guest : False
        Member : False
        Admin : True

        ---> Autorise un user à ajouter des membres au serveur si son groupe y est autorisé.

             Pre: Adresse email d'un utilisateur spécifique. (string)
             Post: Identifiant d'un serveur spécifique. (string)
    """
    try:
        with MongoConnector() as connector:
            collection = connector.db["role_user"]
            user = collection.find_one({"server": server_id, "user": user_id})
    except Exception as e:
        print(e)

    if user is not None:
        if user["role"] == 2:
            return True
        else:
            return False
    else:
        return False


def can_change_role(user_id, server_id):
    """
        Guest : False
        Member : False
        Admin : True

        ---> Autorise un user à changer le rôles des membres si son groupe y est autorisé.

             Pre: Adresse email d'un utilisateur spécifique. (string)
             Post: Identifiant d'un serveur spécifique. (string)
    """
    try:
        with MongoConnector() as connector:
            collection = connector.db["role_user"]
            user = collection.find_one({"server": server_id, "user": user_id})
    except Exception as e:
        print(e)

    if user is not None:
        if user["role"] == 2:
            return True
        else:
            return False
    else:
        return False


def can_ban(user_id, server_id):
    """
        Guest : False
        Member : False
        Admin : True

        ---> Autorise un user à bannir des membres du serveur si son groupe y est autorisé.

             Pre: Adresse email d'un utilisateur spécifique. (string)
             Post: Identifiant d'un serveur spécifique. (string)
    """
    try:
        with MongoConnector() as connector:
            collection = connector.db["role_user"]
            user = collection.find_one({"server": server_id, "user": user_id})
    except Exception as e:
        print(e)

    if user is not None:
        if user["role"] == 2:
            return True
        else:
            return False
    else:
        return False


def can_change_channel(user_id, server_id):
    """
        Guest : False
        Member : False
        Admin : True

        ---> Autorise un user à modifier un canal du serveur si son groupe y est autorisé.

             Pre: Adresse email d'un utilisateur spécifique. (string)
             Post: Identifiant d'un serveur spécifique. (string)
    """
    try:
        with MongoConnector() as connector:
            collection = connector.db["role_user"]
            user = collection.find_one({"server": server_id, "user": user_id})
    except Exception as e:
        print(e)

    if user is not None:
        if user["role"] == 2:
            return True
        else:
            return False
    else:
        return False


def change_role(user_id, server_id, role_id):
    """
        Guest : False
        Member : False
        Admin : True

        ---> Permet de changer le groupe d'un user si il y est aurotisé.

             Pre: Adresse email d'un utilisateur spécifique. (string)
             Post: Identifiant d'un serveur spécifique. (string)
    """
    if can_change_role(user_id, server_id):
        try:
            with MongoConnector() as connector:
                collection = connector.db["role_user"]
                collection.replace_one(
                    {"server": server_id, "user": user_id},
                    {"server": server_id, "user": user_id, "role": role_id}
                )
        except Exception as e:
            print(e)
    else:
        print("Erreur. Vous n'avez pas l'autorisation nécessaire afin de changer un rôle.")
        return 1
