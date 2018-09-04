from analysis.Analyzer import Analyzer

"""
Class for analysis related to champions.
"""


class ChampionAnalyzer(Analyzer):

    def __init__(self):
        super().__init__()

    def general_winrate_list(self):
        """
        Rank champions in descending order based on win rate.
        :return: array of champions sorted by win rate.
        """

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
