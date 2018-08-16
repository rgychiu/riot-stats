# TODO: Given list of champion matchups, count frequecy and other stats prior to analysis
# TODO: Calculate win percentage in matchups and general win rates for champions
# TODO: Get itemization if possible
from data import DivHarvester, MatchHarvester, SummHarvester


class Analyzer:

    def __init__(self):
        self.div_harvester = DivHarvester.DivHarvester()
        self.summ_harvester = SummHarvester.SummHarvester()
        self.match_harvester = MatchHarvester.MatchHarvester()
