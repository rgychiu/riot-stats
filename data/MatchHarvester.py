import time
from data.Harvester import Harvester
from data.SummHarvester import SummHarvester
from api.db.Database import Database
from api.db.DB_Config import DBConfig

"""
Harvester for the matches endpoint.
"""


class MatchHarvester(Harvester):

    def __init__(self):
        super().__init__()
        self.summ_harvester = SummHarvester()

    def list_player_matches(self, account_id):
        return self.make_request(self.get_match_path() + 'matchlists/by-account/' + str(account_id))

    def list_player_ranked_sr_matches(self, account_id):
        payload = {'queue': self.config_manager.get_defaults_queue_id()}
        return self.make_request(self.get_match_path() + 'matchlists/by-account/' + str(account_id), payload)

    def get_match_data(self, match_id):
        """
        Get specific data about a given match with the match_id.
        :param match_id: ID of match to fetch more data for
        :return:
        """
        return self.make_request(self.get_match_path() + 'matches/' + str(match_id))

    def recurse_ranked_sr_matches(self, match_id, matches, queried_matches, queried_players):
        """
        Helper method to fetch as many matches as specified with total matches in the base class.
        :param queried_matches: set of previously found matches
        :param queried_players: set of previously found players
        :return:
        """
        if len(matches) >= self.TOTAL_MATCHES:
            return matches

        try:
            data = self.get_match_data(match_id)
            time.sleep(2)
            for player in data['participantIdentities']:
                account_id = player['player']['accountId']
                if account_id in queried_players:
                    continue
                new_matches = self.list_player_ranked_sr_matches(account_id)['matches']
                matches |= set([match['gameId'] for match in new_matches])
                for match in new_matches:
                    if match['gameId'] in queried_matches:
                        continue
                    queried_matches.add(match['gameId'])
                    return self.recurse_ranked_sr_matches(match['gameId'], matches, queried_matches, queried_players)
        except TypeError:
            # Returned None from request as a result of error status
            return matches

    def get_all_tier_ranked_matches(self, starting_summ):
        """
        Gather all matches from every summoner that appears the given summoner's matches
        :param starting_summ: summoner to start getting match data from
        :return:
        """
        # Get starting points for recursion (challenger player, matches, and ids)
        root_id = self.summ_harvester.get_player_data_by_name(starting_summ)['accountId']
        root_matches = self.list_player_ranked_sr_matches(root_id)['matches']
        root_match_ids = set([match['gameId'] for match in root_matches])
        all_match_ids = set(root_match_ids)
        for ids in root_match_ids:
            all_match_ids |= self.recurse_ranked_sr_matches(ids, set(root_match_ids), set(), set())
        return all_match_ids

    def post_matches(self, match_ids):
        """
        Method to post match data to database
        :param match_ids: set of match_ids to post to database
        :return:
        """
        # Instantiate DB objects in method rather than constructor since not all instances will need DB connection
        # Only create DB connection when posting matches
        db_config = DBConfig()
        db_instance = Database()
        database = db_instance.get_database(db_config.get_db_name())
        collection = db_instance.get_collection(database, db_config.get_match_collection_name())

        # Can't do list comprehension here - avoid exceeding rate limits
        match_datas = []
        for game_id in match_ids:
            try:
                game_details = self.get_match_data(game_id)
                # Make gameId the unique ID in DB
                game_details['_id'] = game_details.pop('gameId')
                match_datas.append(game_details)
                time.sleep(1)
            except AttributeError:
                continue
        db_instance.post_bulk_documents(match_datas, collection)
