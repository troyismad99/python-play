"""

"""

# Runtime:         xx ms      your runtime beats xxxxx % of python3 submissions.
# Memory Usage: xxxxx MB Your memory usage beats xxxxx % of python3 submissions.

from itertools import product, permutations, combinations, zip_longest
from collections import namedtuple
from typing import List, Counter

import math


class Solution:

    def function_name(self) -> bool:

        return False


import unittest


class TestSolution(unittest.TestCase):

    def compare_lists(self, list1, list2):

        if len(list1) != len(list2):
            return False

        if list1 == list2:
            return True

        return sorted(map(sorted, list1)) == sorted(map(sorted, list2))

    def setUp(self):
        self.s = Solution()

    def test_ExampleOne(self):
        self.assertEqual(self.s.function_name(123), 123)

    def test_ExampleTwo(self):
        self.assertEqual(self.s.function_name(123), 123)

    def test_ExampleThree(self):
        self.assertEqual(self.s.function_name(123), 123)


# self.assertFalse(function_name(123))
# self.assertTrue(function_name(123))
# self.assertIn(self.s.function_name(123), [1, 2])
# self.assertTrue(self.compare_lists(self.s.function_name([2, 5, 2, 1, 2], 5), [[1, 2, 2], [5]]))

unittest.main()
