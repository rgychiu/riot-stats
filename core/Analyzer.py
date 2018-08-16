# TODO: Given list of champion matchups, count frequecy and other stats prior to analysis
# TODO: Calculate win percentage in matchups and general win rates for champions
# TODO: Get itemization if possible
from data import DivHarvester, MatchHarvester, SummHarvester


class Analyzer:

    def __init__(self):
        self.div_harvester = DivHarvester.DivHarvester()
        self.summ_harvester = SummHarvester.SummHarvester()
        self.match_harvester = MatchHarvester.MatchHarvester()

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

    def recurse_matches(self, starting_summ, matches, queried_matches, queried_players):
        if len(matches) == self.TOTAL_MATCHES:
            return matches

        root_id = self.get_player_data_by_name(starting_summ)['accountId']
        queried_players.add(root_id)
        root_matches = self.list_player_matches(root_id)

    def get_all_tier_matches(self, starting_summ):
        """
        Gather all matches from every summoner that appears the given summoner's matches
        :param starting_summ: summoner to start getting match data from
        :return:
        """
        while len(all_matches) < self.TOTAL_MATCHES:
            for match in root_matches:
                if match['gameId'] in prev_matches:
                    continue
                all_matches.append(match)
                prev_matches.add(match['gameId'])
                players = self.get_match_data(match['gameId'])['participantIdentities']
                for player in players:
                    if player['accountId'] in prev_players:
                        continue