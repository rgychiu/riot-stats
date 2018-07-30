import requests
from core.Config import Config


class MatchHarvester:

    BASE_URL_PATH = 'https://na1.api.riotgames.com/lol'
    LEAGUE_PATH = BASE_URL_PATH + '/league/v3'
    MATCH_PATH = BASE_URL_PATH + '/match/v3/matches'
    SUMMONER_PATH = BASE_URL_PATH + '/summoner/v3/summoners'
    CHAMPION_PATH = BASE_URL_PATH + '/platform/v3/champions'

    def __init__(self):
        # Load config for defaults & key
        self.config_manager = Config()
        self.api_key = self.config_manager.get_api_key()

    def make_request(self, path, payload=None):
        return None
