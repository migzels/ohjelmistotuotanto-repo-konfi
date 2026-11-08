import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_true(self):
        val = self.stats.search("Yzerman")
        correct_player = Player("Yzerman", "DET", 42, 56)
        self.assertEqual(val.name, correct_player.name)
    
    def test_search_false(self):
        val = self.stats.search("Joulupukki")
        self.assertAlmostEqual(val, None)

    def test_team_found(self):
        val = self.stats.team("EDM")
        correct_team = [
            Player("Semenko", "EDM", 4, 12),
            Player("Kurri",   "EDM", 37, 53),
            Player("Gretzky", "EDM", 35, 89)
        ]

        for correct_player in correct_team:
            found = False
            for player in val:
                if correct_player.name in player.name:
                    found = True
                    break
            self.assertEqual(found, True)
            found = False

    def test_team_not_found(self):
        val = self.stats.team("Jokerit")
        self.assertEqual(val, [])

    def test_top_5_sorted_correctly(self):
        val = self.stats.top(5)
        correctly_sorted = [
            Player("Gretzky", "EDM", 35, 89),#124
            Player("Lemieux", "PIT", 45, 54),#99
            Player("Yzerman", "DET", 42, 56),#98
            Player("Kurri",   "EDM", 37, 53),#90
            Player("Semenko", "EDM", 4, 12)#16
        ]
        self.assertEqual(val[0].goals, correctly_sorted[0].goals)
        self.assertEqual(val[1].goals, correctly_sorted[1].goals)
        self.assertEqual(val[2].assists, correctly_sorted[2].assists)
        self.assertEqual(val[3].assists, correctly_sorted[3].assists)
        self.assertEqual(val[4].name, correctly_sorted[4].name)

    
    def test_top_3_sorted_correctly(self):
        val = self.stats.top(5)
        correctly_sorted = [
            Player("Gretzky", "EDM", 35, 89),#124
            Player("Lemieux", "PIT", 45, 54),#99
            Player("Yzerman", "DET", 42, 56),#98
        ]
        self.assertEqual(val[0].name, correctly_sorted[0].name)
        self.assertEqual(val[1].name, correctly_sorted[1].name)
        self.assertEqual(val[2].name, correctly_sorted[2].name)
