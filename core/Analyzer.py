# TODO: Given list of champion matchups, count frequecy and other stats prior to analysis
# TODO: Build off win rate percentage vs different champions to imply counterpick
# TODO: Get itemization if possible
# TODO: Get runes if possible, calculate win rate of certain runes on champions
# TODO: Calculate popularity of runes on champions
from api.db.Database import Database
from api.db.DB_Config import DBConfig


class Analyzer:

    def __init__(self):
        # Instantiate connection to DB for data and get default collection
        self.db_config = DBConfig()
        self.db_instance = Database()
        self.database = self.db_instance.get_database(self.db_config.get_db_name())
        self.match_collection = self.db_instance.get_collection(self.database, self.db_config.get_match_collection_name())

    def get_total_matches(self):
        """
        Get total matches to be analyzed.
        :return: num matches in db collection
        """
        return self.db_instance.get_num_documents(self.match_collection)

    def get_matches(self):
        """
        Getter method to retrieve matches for stats.
        :return: array with match details
        """
        return self.db_instance.get_bulk_documents(self.match_collection)

