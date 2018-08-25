import json
from core.Singleton import Singleton


class DBConfig(Singleton):

    DB_CONFIG_PATH = "db_config.json"
    MONGO_URI_KEY = "mongo_uri"

    DB_DEFAULTS_KEY = "db_defaults"
    DB_NAME_KEY = "db_name"
    MATCH_COLLECTION_KEY = "match_collection"
    CHAMP_COLLECTION_KEY = "champion_collection"

    def __init__(self):
        super().__init__()

        with open(self.DB_CONFIG_PATH, 'r') as cred_file:
            self.mongo_creds = json.load(cred_file)

    def get_mongo_uri(self):
        return self.mongo_creds[self.MONGO_URI_KEY]

    def get_db_defaults(self):
        return self.mongo_creds[self.DB_DEFAULTS_KEY]

    def get_db_name(self):
        return self.get_db_defaults()[self.DB_NAME_KEY]

    def get_match_collection_name(self):
        return self.get_db_defaults()[self.MATCH_COLLECTION_KEY]

    def get_champion_collection_name(self):
        return self.get_db_defaults()[self.CHAMP_COLLECTION_KEY]
