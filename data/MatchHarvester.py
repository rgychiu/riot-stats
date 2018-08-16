from data.Harvester import Harvester
from data.SummHarvester import SummHarvester


class MatchHarvester(Harvester):

    def __init__(self):
        super().__init__()
        self.summ_harvester = SummHarvester()

    def list_player_matches(self, account_id):
        return self.make_request(self.get_match_path() + 'matchlists/by-account/' + str(account_id))

    def get_match_data(self, match_id):
        return self.make_request(self.get_match_path() + 'matches/' + str(match_id))

    def recurse_matches(self, starting_summ, matches, queried_matches, queried_players):
        if len(matches) == self.TOTAL_MATCHES:
            return matches

        root_id = self.summ_harvester.get_player_data_by_name(starting_summ)['accountId']
        queried_players.add(root_id)
        root_matches = self.list_player_matches(root_id)
        for match in root_matches:
            if match['gameId'] in queried_matches:
                continue
            matches.append(match)
            queried_matches.add(match['gameId'])
            players = self.get_match_data(match['gameId'])['participantIdentities']
            for player in players:
                if player['accountId'] in queried_players:
                    continue
                queried_players.add(player['accountId'])
                return self.recurse_matches(player['summonerName'], matches, queried_matches, queried_players)

    def get_all_tier_matches(self, starting_summ):
        """
        Gather all matches from every summoner that appears the given summoner's matches
        :param starting_summ: summoner to start getting match data from
        :return:
        """
        return self.recurse_matches(starting_summ, [], set(), set())
