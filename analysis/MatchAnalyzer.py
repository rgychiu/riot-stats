from analysis.Analyzer import Analyzer

"""
Class for analysis relating to matches
"""


class MatchAnalyzer(Analyzer):

    def __init__(self):
        super().__init__()

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
