import logging
import unittest
from rt_with_exceptions import Runner, Tournament

logging.basicConfig(level=logging.INFO, filemode='w',
                    filename='runner_tests.log', encoding='utf-8',
                    format='%(asctime)s | %(levelname)s | %(message)s')


class RunnerTest(unittest.TestCase):
    is_frozen = False
    def test_walk(self):
        try:
            Runner("name", -1)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)

        runner = Runner("name")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        try:
            runner = Runner(3.14)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runner1 = Runner("name1")
        runner2 = Runner("name2")
        for _ in range(10):
            runner1.run()
        for _ in range(10):
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)

class TournamentTest(unittest.TestCase):
    is_frozen = True
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
