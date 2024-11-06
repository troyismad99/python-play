"""
643. Maximum Average Subarray I

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average 
value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

Example 1:
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:
Input: nums = [5], k = 1
Output: 5.00000

Constraints:
n == nums.length
1 <= k <= n <= 10^5
-10^4 <= nums[i] <= 10^4
"""

# Runtime:         92 ms       our runtime beats 40.83 % of python3 submissions.
# Memory Usage: 26.46 MB Your memory usage beats 79.05 % of python3 submissions.

from itertools import product, permutations, combinations, zip_longest
from collections import namedtuple
from typing import List, Counter

import math


class Solution:

    def findMaxAverage(self, nums: List[int], k: int) -> float:

        # sliding window

        # start with the first k elements
        max_sum = sum(nums[:k])
        slice_sum = max_sum

        for left in range(k, len(nums)):
            # add next element and remove the older element
            slice_sum += nums[left] - nums[left - k]
            max_sum = max(max_sum, slice_sum)

        #  return the average
        return max_sum / k

    def findMaxAverage_one(self, nums: List[int], k: int) -> float:
        # O(n*k)
        max_average = -math.inf

        for left in range(len(nums) - k + 1):
            slice_average = sum(nums[left : left + k]) / k
            max_average = max(max_average, slice_average)

        return max_average


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_ExampleOne(self):
        self.assertAlmostEqual(self.s.findMaxAverage([1, 12, -5, -6, 50, 3], 4), 12.750)

    def test_ExampleTwo(self):
        # self.assertEqual(self.s.findMaxAverage(123), 123)
        self.assertAlmostEqual(self.s.findMaxAverage([5], 1), 5.0000)


unittest.main()
