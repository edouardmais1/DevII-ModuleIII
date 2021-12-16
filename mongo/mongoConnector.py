from pymongo import MongoClient


class MongoConnector:
    """
        Cette classe permet de créer une connexion vers la base de données.
        Veuillez modifier la variable 'certificat_path' avec le chemin vers l'endroit ou se trouve votre certificat.
        Exemple d'utilisation dans votre code :

    """

    def __init__(self):
        certificat_path = r"C:\Users\User\Desktop\coursBac2\DevBac2\certificatMongo\2TL2-G1.pem"
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
    try:
        with MongoConnector() as connector:
            collection = connector.db["users"]
            res = collection.find_one()
            print(res)
    except Exception as e:
        print(e)


def submit_data_DB(mail, password):
    try:
        with MongoConnector() as connector:
            collection = connector.db["users"]
            collection.insert_one({"mail": mail, "password": password})

    except Exception as e:
        print(e)


def connexion(mail, password):
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


if __name__ == '__main__':
    # submit_data_DB("max", "test")
    testConnectionDB()

