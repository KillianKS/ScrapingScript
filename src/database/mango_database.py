from datetime import datetime
from pymongo import MongoClient

from src.database.database import Database
from src.helpers.configuration_helper import ConfigurationHelper
from src.helpers.singleton_helper import SingletonHelper


class MangoDatabase(Database):
    def __init__(self, service_builder: SingletonHelper):
        service_builder.has_singleton_or_exeption(ConfigurationHelper)
        config = service_builder.get_singleton(ConfigurationHelper)

        client = MongoClient(**self.__get_mongo_client_config(config), serverSelectionTimeoutMS=10000)

        self.db = client.prod if config.get("ENV_NAME") == "prod" else client.dev


    def __get_mongo_client_config(config: ConfigurationHelper):
        base_url = f"mongodb+srv://{{}}{config.get('MONGO_URI')}/myFirstDatabase?retryWrites=true&w=majority{{}}"

        if config.getConfig("MONGO_CERT") != None:
            return {
                "host": base_url.format("", "&authSource=%24external&authMechanism=MONGODB-X509"),
                "tls": True,
                "tlsCertificateKeyFile": f"./cred/{config.getConfig('MONGO_CERT')}"
            }
        else:
            return {
                "host": base_url.format(f"{config.getConfig('MONGO_USER')}:{config.getConfig('MONGO_PASSWORD')}@", "")
            }

    def upsert_event(self, event):
        result = self.db.match.update_one(
            {'bookmaker': event["bookmaker"], 'event': event["event"] },
            {'$set': event},
            upsert=True
        )


    def event_is_notify(self, eventId):
        self.colec.update_one(
            { 'event': eventId },
            {
                '$set': { 'notify' : datetime.now() }
            }
        )


    def get_actives_books_config(self):
        return self.db["bot-config"].find({"isActive": True})


    def get_not_notify_events(self):
        return self.db.match.find({'notify': None})