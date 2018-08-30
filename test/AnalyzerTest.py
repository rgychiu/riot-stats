import unittest
from core.Analyzer import Analyzer


class AnalyzerTest(unittest.TestCase):

    def setUp(self):
        self.analyzer = Analyzer()

    # Test getting data from database
    # Not rigorous since DB fetching decently reliable, making sure parameters and queries are correct
    def test_get_match_count(self):
        self.assertTrue(self.analyzer.get_total_matches() > 0)

    def test_get_matches(self):
        self.assertTrue(len(self.analyzer.get_matches()) > 0)

    def test_get_champion(self):
        self.assertTrue(self.analyzer.get_champion('Aatrox') is not None)

    def test_get_champion_id(self):
        self.assertTrue(self.analyzer.get_champion_id('Aatrox') == 266)

    if __name__ == '__main__':
        unittest.main()
