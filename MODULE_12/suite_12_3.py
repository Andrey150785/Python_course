import unittest
from MODULE_12.tests_12_3 import RunnerTest, TournamentTest


runners_case = unittest.TestSuite()
runners_case.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
runners_case.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(runners_case)