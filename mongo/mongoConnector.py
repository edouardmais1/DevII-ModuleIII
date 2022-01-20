from pymongo import MongoClient


class MongoConnector:
    """
    ---> Cette classe permet d'initialiser une connexion vers la base de données.

         Pre: -
         Post: -

    """

    def __init__(self):
        certificat_path = r"C:\Users\maxim\Documents\Maxime\EPHEC\BAC_2\2TL2-G1.pem"
        uri = "mongodb+srv://cluster0.5i6qo.gcp.mongodb.net/ephecom-2TL2?authSource=%24external&authMechanism=MONGODB" \
              "-X509&retryWrites=true&w=majority&ssl_cert_reqs=CERT_NONE "
        client = MongoClient(uri,
                             tls=True,
                             tlsCertificateKeyFile=certificat_path)
        self.db = client['ephecom-2TL2']

    def __enter__(self):
        return self

    def __exit__(self):
        self.db.close()


def testConnectionDB():
    """
    ---> Permet d'effectuer un test de connexion avec la DB et consulter son contenu.

         Pre: -
         Post: -
         Raise: Exception si la connexion avec la DB n'a pas pu aboutir.
    """
    try:
        with MongoConnector() as connector:
            collection = connector.db["users"]
            res = collection.find_one()
            print(res)
    except Exception as e:
        print(e)


def submit_data_DB(mail, password, user_name):
    """
    ---> Permet de soumettre les différentes données d'un nouvel utilisateur dans la base de données.

         Pre: les différents champs de données doivent au préalable avoir été complétés et vérifiés.
         Post: enregistre les données au sein de la base de données adéquate.
         Raise: Exception si une erreur se produit lors de la tentative de connexion à la base de données.
    """
    try:
        with MongoConnector() as connector:
            collection = connector.db["users"]
            collection.insert_one({"mail": mail, "password": password, "user_name": user_name})
    except Exception as e:
        print(e)


def connexion(mail, password):
    """
    ---> Permet d'effetuer une connexion d'un utilisateur en vérifiant que les données saisies
         éxistent au sein de la base de données.

         Pre: l'utilisateur doit au préalable éxister dans la base de données.
         Post: l'utilisateur est connecté.
         Raise: Exception si une erreur se produit lors de la tentative de connexion à la base de données.
    """
    exist = []
    try:
        with MongoConnector() as connector:
            collection = connector.db["users"]
            myDoc = collection.find_one({"mail": mail, "password": password})
            for user in myDoc:
                exist.append(user)

    except Exception as e:
        print(e)
    finally:
        if len(exist) == 0:
            return False
        else:
            return True


def checkAccount(email):
    """
    ---> Permet de vérifier si l'email d'un utilisateur éxiste déja au sein de la DB lors d'une tentative d'inscription.

         Pre: -
         Post: renvoie True si l'email saisie éxiste déja, sinon False.
         Raise: Exception si une erreur se produit lors d'une tentative de connexion à la base de données.
    """
    exist = []
    try:
        with MongoConnector() as connector:
            collection = connector.db["users"]
            myDoc = collection.find_one({"mail": email})
            for user in myDoc:
                exist.append(user)

    except Exception as e:
        print(e)
    finally:
        if len(exist) == 0:
            return False
        else:
            return True


if __name__ == '__main__':
    pass
