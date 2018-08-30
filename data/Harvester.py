import requests
from core.Config import Config
from core.Logger import Logger

"""
Base class for each Harvester to inherit from. Contains all the endpoints, making a request,
and other constants/variables.
"""


class Harvester:

    # API Endpoints
    _BASE_URL_PATH = 'https://na1.api.riotgames.com/lol'
    _CHALLENGER_PATH = _BASE_URL_PATH + '/league/v3/challengerleagues/by-queue/'
    _MATCH_PATH = _BASE_URL_PATH + '/match/v3/'
    _SUMMONER_PATH = _BASE_URL_PATH + '/summoner/v3/summoners/'

    # Total matches to fetch
    TOTAL_MATCHES = 1000

    def __init__(self):
        # Load config for defaults & key
        self.config_manager = Config().get_instance()
        self.api_key = self.config_manager.get_api_key()
        self.logger = Logger()

    def make_request(self, path, payload=None):
        """
        Make request to Riot API Developer endpoint with optional data
        :param path: endpoint to query
        :param payload: optional parameters to send with the request
        :return:
        """
        try:
            if payload is None:
                payload = {'api_key': self.api_key}
            else:
                payload['api_key'] = self.api_key
            response = requests.get(path, params=payload)
            self.logger.info(path + str(response))
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return None

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
