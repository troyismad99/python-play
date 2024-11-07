"""
1732. Find the Highest Altitude

There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. 
The biker starts his trip on point 0 with altitude equal 0.

You are given an integer array gain of length n where gain[i] is the net gain in altitude between 
points i and i + 1 for all (0 <= i < n). 

Return the highest altitude of a point.

Example 1:
Input: gain = [-5,1,5,0,-7]
Output: 1
Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.

Example 2:
Input: gain = [-4,-3,-2,-1,4,3,2]
Output: 0
Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.

Constraints:
n == gain.length
1 <= n <= 100
-100 <= gain[i] <= 100
"""

# Runtime:          0 ms        your runtime beats 100 % of python3 submissions.
# Memory Usage: 16.60 MB Your memory usage beats 49.06 % of python3 submissions.

from itertools import product, permutations, combinations, zip_longest
from collections import namedtuple
from typing import List, Counter

import math


class Solution:

    def largestAltitude(self, gain: List[int]) -> int:

        current = 0
        highest = 0

        for g in gain:
            current += g
            highest = max(highest, current)

        return highest


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_ExampleOne(self):
        self.assertEqual(self.s.largestAltitude([-5, 1, 5, 0, -7]), 1)

    def test_ExampleTwo(self):
        self.assertEqual(self.s.largestAltitude([-4, -3, -2, -1, 4, 3, 2]), 0)


unittest.main()
