"""
53. Maximum Subarray
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

Constraints:
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
"""

# Runtime:         90 ms Your runtime beats 24.61 % of python3 submissions.
# Memory Usage: 30.87 MB Your memory usage beats 94.34 % of python3 submissions.

from typing import List
from itertools import product, combinations, permutations
from collections import namedtuple
import math


class Solution:

    def maxSubArray(self, nums: List[int]) -> int:

        max_sum = nums[0]
        current_sum = nums[0]

        # check each element
        for n in nums[1:]:

            # what happens when we add this element to our current total?
            current_sum = max(n, current_sum + n)

            # do we have a new max?
            max_sum = max(max_sum, current_sum)

        return max_sum


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
        self.assertEqual(self.s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)

    def test_ExampleTwo(self):
        self.assertEqual(self.s.maxSubArray([1]), 1)

    def test_ExampleThree(self):
        self.assertEqual(self.s.maxSubArray([5, 4, -1, 7, 8]), 23)

    def test_ExampleFour(self):
        self.assertEqual(self.s.maxSubArray([-1]), -1)

    def test_ExampleFive(self):
        self.assertEqual(self.s.maxSubArray([-2, 1]), 1)


unittest.main()
