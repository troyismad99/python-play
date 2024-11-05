"""
11. Container With Most Water

You are given an integer array height of length n. There are n vertical lines drawn such that the 
two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
 

Constraints:
n == height.length
2 <= n <= 10^5
0 <= height[i] <= 10^4
"""

# Runtime:        100 ms       our runtime beats 52.65 % of python3 submissions.
# Memory Usage: 27.95 MB Your memory usage beats 92.22 % of python3 submissions.

from itertools import product, permutations, combinations, zip_longest
from collections import namedtuple
from typing import List, Counter

import math


class Solution:

    def maxArea(self, height: List[int]) -> int:

        left = 0
        right = len(height) - 1

        max_area = 0

        while left < right:
            width = right - left

            max_area = max(max_area, min(height[left], height[right]) * width)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_ExampleOne(self):
        self.assertEqual(self.s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)

    def test_ExampleTwo(self):
        self.assertEqual(self.s.maxArea([1, 1]), 1)


unittest.main()
