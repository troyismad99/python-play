"""
2239. Find Closest Number to Zero

Given an integer array nums of size n, return the number with the value closest to 0 in nums. 
If there are multiple answers, return the number with the largest value.

 

Example 1:
Input: nums = [-4,-2,1,4,8]
Output: 1
Explanation:
The distance from -4 to 0 is |-4| = 4.
The distance from -2 to 0 is |-2| = 2.
The distance from 1 to 0 is |1| = 1.
The distance from 4 to 0 is |4| = 4.
The distance from 8 to 0 is |8| = 8.
Thus, the closest number to 0 in the array is 1.

Example 2:
Input: nums = [2,-1,1]
Output: 1
Explanation: 1 and -1 are both the closest numbers to 0, so 1 being larger is returned.
 

Constraints:
1 <= n <= 1000
-105 <= nums[i] <= 105
"""

# Runtime:          7 ms Your runtime beats 58.62 % of python3 submissions.
# Memory Usage: 16.81 MB Your memory usage beats 28.45 % of python3 submissions.

from typing import List
from itertools import product, combinations, permutations
from collections import namedtuple
import math


class Solution:

    def findClosestNumber(self, nums: List[int]) -> int:

        return min(nums, key=lambda x: (abs(x), -x))

        # closest = math.inf

        # for i in nums:
        #     if abs(i) < closest:
        #         closest = abs(i)
        #         result = i

        # return abs(result) if result <0 and abs(result) in nums else result


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
        self.assertEqual(self.s.findClosestNumber([-4, -2, 1, 4, 8]), 1)

    def test_ExampleTwo(self):
        self.assertEqual(self.s.findClosestNumber([2, -1, 1]), 1)


unittest.main()
