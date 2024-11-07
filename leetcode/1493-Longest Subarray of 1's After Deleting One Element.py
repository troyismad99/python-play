"""
1493. Longest Subarray of 1's After Deleting One Element

Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. 
Return 0 if there is no such subarray.

Example 1:
Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.

Example 2:
Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].

Example 3:
Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.

Constraints:
1 <= nums.length <= 10^5
nums[i] is either 0 or 1.
"""

# Runtime:         75 ms       our runtime beats 33.89 % of python3 submissions.
# Memory Usage: 25.34 MB Your memory usage beats  5.99 % of python3 submissions.

from itertools import product, permutations, combinations, zip_longest
from collections import namedtuple
from typing import List, Counter

import math


class Solution:

    def longestSubarray(self, nums: List[int]) -> int:

        #  guard against a list of all 1
        c = Counter(nums)

        if c[1] == len(nums):
            return c[1] - 1

        n = len(nums)

        # track ones to the left of an index
        left_ones_count = [0] * n

        #  track ones to the right of the index
        right_ones_count = [0] * n

        # Calculate the consecutive ones to the left of each index
        for i in range(1, n):
            if nums[i - 1] == 1:
                left_ones_count[i] = left_ones_count[i - 1] + 1

        # Calculate the consecutive ones to the right of each index
        for i in range(n - 2, -1, -1):
            if nums[i + 1] == 1:
                right_ones_count[i] = right_ones_count[i + 1] + 1

        # Find the maximum length subarray formed by summing up counts of left and right ones.
        # Note that the question assumes we can remove one zero to maximize the length.
        # So, connecting two streaks of ones effectively means removing one zero between them.
        return max(a + b for a, b in zip(left_ones_count, right_ones_count))


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_ExampleOne(self):
        self.assertEqual(self.s.longestSubarray([1, 1, 0, 1]), 3)

    def test_ExampleTwo(self):
        self.assertEqual(self.s.longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1]), 5)

    def test_ExampleThree(self):
        self.assertEqual(self.s.longestSubarray([1, 1, 1]), 2)


unittest.main()
