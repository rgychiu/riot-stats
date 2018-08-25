import pymongo
from api.db import DB_Config


class DatabaseUtils:

    def __init__(self):
        self.mongo_config = DB_Config.DBConfig()
        self.client = pymongo.MongoClient(self.mongo_config.get_mongo_uri())
