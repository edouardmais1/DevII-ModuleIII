from pymongo import MongoClient

from src.config import config


class MongoConnector:
    """
    ---> permet de se connecter à une base de donnée mongoDb
    """

    def __init__(self):
        certificat_path = config.ROOT_DIR + "/certif_mongo.pem"
        uri = "mongodb+srv://cluster0.5i6qo.gcp.mongodb.net/ephecom?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority&ssl_cert_reqs=CERT_NONE"
        client = MongoClient(uri,
                             tls=True,
                             tlsCertificateKeyFile=certificat_path)
        self.db = client['ephecom']

    def __enter__(self):
        return self

    def __exit__(self):
        self.db.close()