from data.Harvester import Harvester


class SummHarvester(Harvester):

    def __init__(self):
        super().__init__()

    def get_player_data_by_name(self, player_name):
        return self.make_request(self.get_summoner_path() + 'by-name/' + player_name)

    def get_player_data_by_id(self, player_id):
        return self.make_request(self.get_summoner_path() + player_id)