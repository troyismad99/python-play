"""
1207. Unique Number of Occurrences

Given an array of integers arr, return true if the number of occurrences of each 
value in the array is unique or false otherwise.

Example 1:
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

Example 2:
Input: arr = [1,2]
Output: false

Example 3:
Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true

Constraints:
1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000
"""

# Runtime:          0 ms      your runtime beats   100 % of python3 submissions.
# Memory Usage: 16.72 MB Your memory usage beats 32.06 % of python3 submissions.

from itertools import product, permutations, combinations, zip_longest
from collections import namedtuple
from typing import List, Counter

import math


class Solution:

    def uniqueOccurrences(self, arr: List[int]) -> bool:

        c = Counter(arr)
        unique = set(c.values())

        return len(unique) == len(c)

        # hash_map = {}
        # for i in range(len(arr)):
        #     if arr[i] in hash_map:
        #         hash_map[arr[i]]+=1
        #     else:
        #         hash_map[arr[i]]=1
        # return len(set(hash_map.values()))==len(hash_map.values())


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_ExampleOne(self):
        self.assertTrue(self.s.uniqueOccurrences([1, 2, 2, 1, 1, 3]))

    def test_ExampleTwo(self):
        self.assertFalse(self.s.uniqueOccurrences([1, 2]))

    def test_ExampleThree(self):
        self.assertTrue(self.s.uniqueOccurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]))


unittest.main()
