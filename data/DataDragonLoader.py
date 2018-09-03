import urllib.request
import json
from api.db.Database import Database
from api.db.DB_Config import DBConfig


"""
Harvester for champion data.
"""


class DataDragonLoader:

    # Riot Data Dragon champion json data url
    _BASE_URL = 'http://ddragon.leagueoflegends.com/cdn/6.24.1/data/en_US/'
    _CHAMPION_URL = _BASE_URL + 'champion.json'
    _RUNE_URL = _BASE_URL + 'mastery.json'

    def __init__(self):
        # Instantiate DB connection and get champion collection
        self.db_config = DBConfig()
        self.db_instance = Database()
        self.database = self.db_instance.get_database(self.db_config.get_db_name())
        self.champ_collection = self.db_instance.get_collection(self.database,
                                                                self.db_config.get_champion_collection_name())

    def get_data(self, path):
        """
        Get champion json data from url.
        :return: champion json
        """
        with urllib.request.urlopen(path) as url:
            data = json.loads(url.read().decode())
        return data

    def get_rune_data(self):
        data = self.get_data(self._RUNE_URL)
        return data

    def post_champions(self):
        data = self.get_data(self._CHAMPION_URL)['data']
        champ_array = []
        for champ_key in data.keys():
            # Format dictionary keys before pushing to DB
            champion = data[champ_key]
            champion['_id'] = champion.pop('key')
            champion.pop('id')
            champ_array.append(champion)
        self.db_instance.post_bulk_documents(champ_array, self.champ_collection)

