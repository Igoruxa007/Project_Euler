import os
import sys
import unittest

sys.path.append(os.getcwd())
from main import *


class TestProblem_1(unittest.TestCase):
    def test_prob_one_result(self):
        self.assertEqual(problem1(10), 23)


if __name__ == '__main__':
    unittest.main()
