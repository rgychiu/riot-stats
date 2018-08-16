from data.Harvester import Harvester


class MatchHarvester(Harvester):

    def __init__(self):
        super().__init__()

    def list_player_matches(self, account_id):
        return self.make_request(self.get_match_path() + 'matchlists/by-account/' + str(account_id))

    def get_match_data(self, match_id):
        return self.make_request(self.get_match_path() + 'matches/' + str(match_id))