"""
283. Move Zeroes

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]

Constraints:
1 <= nums.length <= 10^4
-2^31 <= nums[i] <= 2^31 - 1
"""

# Runtime:         11 ms       our runtime beats 25.18 % of python3 submissions.
# Memory Usage: 17.72 MB Your memory usage beats 87.75 % of python3 submissions.

from itertools import product, permutations, combinations, zip_longest
from collections import namedtuple
from typing import List, Counter

import math


class Solution:

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Two pointer:
        # - fast pointer iterates the list 
        # - slow pointer for the zero elements

        slow = 0
        
        for fast in range(len(nums)):
        
            if nums[fast] != 0 and nums[slow] == 0:

                # swap a zero with the next non zero
                nums[slow], nums[fast] = nums[fast], nums[slow]

            # move slow to next position
            if nums[slow] != 0:
                slow += 1

        # for testing only
        return nums


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_ExampleOne(self):
        self.assertEqual(self.s.moveZeroes([0, 1, 0, 3, 12]), [1, 3, 12, 0, 0])

    def test_ExampleTwo(self):
        self.assertEqual(self.s.moveZeroes([0]), [0])

    def test_ExampleThree(self):
        self.assertEqual(self.s.moveZeroes([0, 0, 0, 1, 5, 0, 0, 4, 0]), [1, 5, 4, 0, 0, 0, 0, 0, 0])


unittest.main()
