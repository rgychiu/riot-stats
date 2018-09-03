# TODO: Given list of champion matchups, count frequecy and other stats prior to analysis
# TODO: Build off win rate percentage vs different champions to imply counterpick
# TODO: Get itemization if possible
# TODO: Rune data and popularity on champions (Haven't reached the API)
from api.db.Database import Database
from api.db.DB_Config import DBConfig


class Analyzer:

    def __init__(self):
        # Instantiate connection to DB for data and get default collection
        self.db_config = DBConfig()
        self.db_instance = Database()
        self.database = self.db_instance.get_database(self.db_config.get_db_name())
        self.match_collection = self.db_instance.get_collection(self.database,
                                                                self.db_config.get_match_collection_name())
        self.champ_collection = self.db_instance.get_collection(self.database,
                                                                self.db_config.get_champion_collection_name())

    def get_total_matches(self):
        """
        Get total matches to be analyzed.
        :return: num matches in db collection
        """
        return self.db_instance.get_num_documents(self.match_collection)

    def get_matches(self):
        """
        Getter method to retrieve matches for stats.
        :return: array with match details
        """
        return self.db_instance.get_bulk_documents(self.match_collection)

    def get_matches_by_query(self, query):
        """
        Overloaded method to get matches using specific query
        :param query: query to use to fetch matches from DB
        :return: iterable with matched documents
        """
        return self.db_instance.get_bulk_documents(self.match_collection, query)

    def get_champion(self, champion_name):
        """
        Get data for specified champion.
        :param champion_name: name of champion
        :return: json data for champion
        """
        return self.db_instance.get_single_document(self.champ_collection, {"name": champion_name})

    def get_champions(self):
        """
        Get all champions from db.
        :return: cursor object with all champions
        """
        return self.db_instance.get_bulk_documents(self.champ_collection)

    def get_champion_id(self, champion_name):
        """
        Get champion id for specified champion
        :param champion_name: name of champion
        :return: id of champion
        """
        return self.db_instance.get_single_document(self.champ_collection, {"name": champion_name})['_id']

    def get_winrate(self, champion_id, cursor_matches):
        """
        Helper method to get winrate of a champion from an iterable of match data.
        :param champion_id: id of champion
        :param cursor_matches: cursor object of match data
        :return: winrate percentage
        """
        total_matches = cursor_matches.count()
        win_count = 0
        for match in cursor_matches:
            participants = match['participants']
            team_id = 0

            for players in participants:
                if players['championId'] == champion_id:
                    team_id = players['teamId']
            for team in match['teams']:
                if team['teamId'] == team_id and team['win'] == 'Win':
                    win_count += 1
        return (win_count / total_matches) * 100

    def champion_winrate(self, champion_name):
        """
        Calculate the champion win rate percentage from gathered matches.
        :param champion_name: name of champion to calculate winrate for
        :return: None if champion not found, float percentage otherwise
        """
        # Champion id returns as string
        champion_id = int(self.get_champion_id(champion_name.title()))
        seen_matches = self.get_matches_by_query({"participants.championId": champion_id})
        return self.get_winrate(champion_id, seen_matches)

    def matchup_winrate(self, champion1_name, champion2_name):
        """
        Calculate the matchup win rate percentage from gathered matches.
        :param champion1_name: first champ in matchup
        :param champion2_name: second champ in matchup
        :return: tuple of win percentages for matchup
        """
        # TODO: Ensure matchup is in the same lane and champions are not on the same team
        champion1_id = int(self.get_champion_id(champion1_name.title()))
        champion2_id = int(self.get_champion_id(champion2_name.title()))
        seen_matches = self.get_matches_by_query({
            "$and": [{"participants.championId": champion1_id}, {"participants.championId": champion2_id}]
        })
        champion1_winrate = self.get_winrate(champion1_id, seen_matches)
        return champion1_winrate, 100 - champion1_winrate
