import requests
from core.Config import Config


class Harvester:

    _BASE_URL_PATH = 'https://na1.api.riotgames.com/lol'
    _CHALLENGER_PATH = _BASE_URL_PATH + '/league/v3/challengerleagues/by-queue/'
    _MATCH_PATH = _BASE_URL_PATH + '/match/v3/'
    _SUMMONER_PATH = _BASE_URL_PATH + '/summoner/v3/summoners/'
    _CHAMPION_PATH = _BASE_URL_PATH + '/platform/v3/champions/'

    TOTAL_MATCHES = 1000000

    def __init__(self):
        # Load config for defaults & key
        self.config_manager = Config()
        self.api_key = self.config_manager.get_api_key()

    def make_request(self, path):
        """
        Make request to Riot API Developer endpoint with optional data
        :param path: endpoint to query
        :return:
        """
        payload = {'api_key': self.config_manager.get_api_key()}
        return requests.get(path, params=payload).json()

    def get_challenger_path(self):
        return self._CHALLENGER_PATH

    def get_match_path(self):
        return self._MATCH_PATH

    def get_summoner_path(self):
        return self._SUMMONER_PATH

    def get_champion_path(self):
        return self._CHAMPION_PATH

    def get_total_matches(self):
        return self.TOTAL_MATCHES

    # TODO: Get champion matchups from match histories
