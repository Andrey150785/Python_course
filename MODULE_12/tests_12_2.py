import unittest
from runner_and_tournament import Runner, Tournament


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner("Usain", 10)
        self.andrey = Runner("Andrey", 9)
        self.nick = Runner("Nick", 3)

    @classmethod
    def tearDownClass(cls):
        for test_name, result in cls.all_results.items():
            print(result)

    def test_tournament_usain_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        results = tournament.start()
        self.__class__.all_results["test1_usain_nick"] = {k: str(v) for k, v in results.items()}
        last_place = max(results)
        self.assertTrue(results[last_place] == "Nick")

    def test_tournament_andrey_nick(self):
        tournament = Tournament(90, self.andrey, self.nick)
        results = tournament.start()
        self.__class__.all_results["test2_andrey_nick"] = {k: str(v) for k, v in results.items()}
        last_place = max(results)
        self.assertTrue(results[last_place] == "Nick")

    def test_tournament_usain_andrey_nick(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        results = tournament.start()
        self.__class__.all_results["test3_usain_andrey_nick"] = {k: str(v) for k, v in results.items()}
        last_place = max(results)
        self.assertTrue(results[last_place] == "Nick")


if __name__ == "__main__":
    unittest.main()
