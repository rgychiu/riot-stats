import unittest
from core.Analyzer import Analyzer


class AnalyzerTest(unittest.TestCase):

    def setUp(self):
        self.analyzer = Analyzer()

    def test_get_match_count(self):
        self.assertTrue(self.analyzer.get_total_matches() > 0)

    def test_get_matches(self):
        self.assertTrue(len(self.analyzer.get_matches()) > 0)

    def test_get_champion(self):
        self.assertTrue(self.analyzer.get_champion('Aatrox') is not None)

    def test_get_champion_id(self):
        self.assertTrue(self.analyzer.get_champion_id('Aatrox') == 266)
