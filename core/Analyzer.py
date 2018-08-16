# TODO: Given list of champion matchups, count frequecy and other stats prior to analysis
# TODO: Calculate win percentage in matchups and general win rates for champions
# TODO: Build off win rate percentage vs different champions to imply counterpick
# TODO: Get itemization if possible
# TODO: Get runes if possible, calculate win rate of certain runes on champions
# TODO: Calculate popularity of runes on champions
from data import DivHarvester, MatchHarvester, SummHarvester


class Analyzer:

    def __init__(self):
        self.div_harvester = DivHarvester.DivHarvester()
        self.summ_harvester = SummHarvester.SummHarvester()
        self.match_harvester = MatchHarvester.MatchHarvester()
