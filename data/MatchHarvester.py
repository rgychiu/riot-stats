import time
import requests
from data.Harvester import Harvester
from data.SummHarvester import SummHarvester

"""
Harvester for the matches endpoint.
"""


class MatchHarvester(Harvester):

    def __init__(self):
        super().__init__()
        self.summ_harvester = SummHarvester()

    def make_request(self, path):
        """
        Overwritten make request method that ignores unfound summoner or match data
        :param path: path to make request to
        :return:
        """
        try:
            payload = {'api_key': self.api_key}
            response = requests.get(path, params=payload)
            print(path + str(response))
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError:
            return None

    def list_player_matches(self, account_id):
        return self.make_request(self.get_match_path() + 'matchlists/by-account/' + str(account_id))

    def get_match_data(self, match_id):
        """
        Get specific data about a given match with the match_id.
        :param match_id: ID of match to fetch more data for
        :return:
        """
        return self.make_request(self.get_match_path() + 'matches/' + str(match_id))

    def recurse_matches(self, starting_summ, matches, queried_matches, queried_players):
        """
        Helper method to fetch as many matches as specified with total matches in the base class.
        :param starting_summ: starting summoner name to start recursion from
        :param matches: list of fetched matches
        :param queried_matches: set of previously found matches
        :param queried_players: set of previously found players
        :return:
        """
        if len(matches) == self.TOTAL_MATCHES:
            return len(matches)

        root_id = self.summ_harvester.get_player_data_by_name(starting_summ)['accountId']
        queried_players.add(root_id)
        root_matches = self.list_player_matches(root_id)
        # Prevent going over rate limit by sleeping the function in key spots
        time.sleep(3)
        for match in root_matches['matches']:
            # Check if match has already been queried or continue to next iteration if error in API occurred
            if match['gameId'] in queried_matches or match['queue'] != 420:
                continue
            elif root_id is None or root_matches is None:
                continue
            matches.append(match)
            queried_matches.add(match['gameId'])
            players = self.get_match_data(match['gameId'])['participantIdentities']
            time.sleep(3)
            for player in players:
                if player['player']['accountId'] in queried_players:
                    continue
                elif players is None:
                    continue
                queried_players.add(player['player']['accountId'])
                return self.recurse_matches(player['player']['summonerName'], matches, queried_matches, queried_players)

    def get_all_tier_matches(self, starting_summ):
        """
        Gather all matches from every summoner that appears the given summoner's matches
        :param starting_summ: summoner to start getting match data from
        :return:
        """
        return self.recurse_matches(starting_summ, [], set(), set())
