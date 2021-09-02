import os
import sys
import unittest

sys.path.append(os.getcwd())
from main import *


class TestProblem_1(unittest.TestCase):
    def test_prob_one_result(self):
        self.assertEqual(problem1(10), 23)

    def test_prob_forty_eight_result(self):
        self.assertEqual(problem48(), '9110846700')


if __name__ == '__main__':
    unittest.main()
