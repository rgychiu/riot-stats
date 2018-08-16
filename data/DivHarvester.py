from data.Harvester import Harvester


class DivHarvester(Harvester):

    def __init__(self):
        super().__init__()

    def get_sr_challenger_league(self):
        """
        Get list of all challenger tier players.
        :return: API JSON response for challenger players
        """
        return self.make_request(self.get_challenger_path() + self.config_manager.get_defaults_queue_id())

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
