import requests
from core.Config import Config


class MatchHarvester:

    BASE_URL_PATH = 'https://na1.api.riotgames.com/lol'
    CHALLENGER_PATH = BASE_URL_PATH + '/league/v3/challengerleagues/by-queue/'
    MATCH_PATH = BASE_URL_PATH + '/match/v3/matches/'
    SUMMONER_PATH = BASE_URL_PATH + '/summoner/v3/summoners/'
    CHAMPION_PATH = BASE_URL_PATH + '/platform/v3/champions/'

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

    def get_top_challenger(self):
        """
        Get top challenger player based on LP.
        :return: Player JSON data with highest LP
        """
        challenger_list = self.get_sr_challenger_league()
        max_LP = 0
        player_json = None
        for player in challenger_list:
            if player['leaguePoints'] > max_LP:
                max_LP = player['leaguePoints']
                player_json = player
        return player_json

    def get_player_data_by_name(self, player_name):
        return self.make_request(self.SUMMONER_PATH + 'by-name/' + player_name)

    def get_player_data_by_id(self, player_id):
        return self.make_request(self.SUMMONER_PATH + player_id)

    # TODO: Get match histories starting with the top challenger player
    # TODO: Get champion matchups from match histories
