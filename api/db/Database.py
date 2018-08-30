import pymongo
from api.db.DB_Config import DBConfig
from core.Singleton import Singleton


class Database(Singleton):

    def __init__(self):
        super().__init__()

        # Get database config manager and initiate connection to the database
        self.mongo_config = DBConfig()
        self.client = pymongo.MongoClient(self.mongo_config.get_mongo_uri())

    def list_db_names(self):
        return self.client.list_database_names()

    def get_database(self, db_name):
        return self.client[db_name]

    def get_collection(self, database, collection_name):
        """
        Method to get a collection from the mongo lab instance.
        :param database: Database object to use for getting a collection
        :param collection_name: name of collection to retrieve
        :return: mongoclient collection item
        """
        return database[collection_name]

    def post_single_document(self, data, collection):
        """
        Method to post a row of data to the mongo lab instance.
        :param data: data to post
        :param collection: target collection object to post data into
        :return:
        """
        collection.insert_one(data)

    def get_single_document(self, collection, query=None):
        """
        Method to get a single document that matches the given query.
        :param collection: collection object to retrieve data from
        :param query: data to match documents on
        :return: single found document or None if not found
        """
        return collection.find_one(query)

    def post_bulk_documents(self, data, collection):
        """
        Method to post a row of data to the mongo lab instance.
        :param data: array of data to post
        :param collection: target collection object to post data into
        :return:
        """
        collection.insert_many(data)

    def get_bulk_documents(self, collection, query=None):
        """
        Method to get multiple documents that match the given query.
        :param collection: collection object to retrieve data from
        :param query: data to match documents on
        :return: Cursor instance, an iterable
        """
        return collection.find(query)

    def get_num_documents(self, collection):
        return collection.count()
