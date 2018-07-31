import requests
from core.Config import Config


class MatchHarvester:

    BASE_URL_PATH = 'https://na1.api.riotgames.com/lol'
    CHALLENGER_PATH = BASE_URL_PATH + '/league/v3/challengerleagues/by-queue/'
    MATCH_PATH = BASE_URL_PATH + '/match/v3/matches'
    SUMMONER_PATH = BASE_URL_PATH + '/summoner/v3/summoners'
    CHAMPION_PATH = BASE_URL_PATH + '/platform/v3/champions'

    def __init__(self):
        # Load config for defaults & key
        self.config_manager = Config()
        self.api_key = self.config_manager.get_api_key()

    def make_request(self, path):
        """
        Make request to Riot API Developer endpoint with optional data
        :param path: endpoint to query
        :param api_key: api key included in query string
        :return:
        """
        payload = {'api_key': self.config_manager.get_api_key()}
        return requests.get(path, params=payload).json()

    def get_sr_challenger_league(self):
        """
        Get list of all challenger tier players.
        :return: API JSON response for challenger players
        """
        return self.make_request(self.CHALLENGER_PATH + self.config_manager.get_defaults_queue_id())

    # TODO: Get match histories starting with the top challenger player
