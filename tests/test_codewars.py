import os
import sys
import unittest

sys.path.append(os.getcwd())
from codewars import *


class TestProblem_1(unittest.TestCase):
    def test_high(self):
        self.assertEqual(high("GJ jsd fsd"), "jsd")


if __name__ == '__main__':
    unittest.main()
