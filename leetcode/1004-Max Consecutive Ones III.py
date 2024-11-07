"""
1004. Max Consecutive Ones III

Given a binary array nums and an integer k, return the maximum number of 
consecutive 1's in the array if you can flip at most k 0's.

Example 1:
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
                         *         *
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
                        ___________  
Bolded * were flipped from 0 to 1. The longest subarray is underlined.

Example 2:
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
                       * *       *
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
                  ___________________
Bolded * were flipped from 0 to 1. The longest subarray is underlined.

Constraints:
1 <= nums.length <= 10^5
nums[i] is either 0 or 1.
0 <= k <= nums.length
"""

# Runtime:         19 ms       our runtime beats 96.19 % of python3 submissions.
# Memory Usage: 17.27 MB Your memory usage beats 39.67 % of python3 submissions.

from itertools import product, permutations, combinations, zip_longest
from collections import namedtuple
from typing import List, Counter

import math


class Solution:

    def longestOnes(self, nums: List[int], k: int) -> int:

        left = 0
        
        for right in range(len(nums)):
        
            if nums[right] == 0:
                k -= 1
        
            if k < 0:
                if nums[left] == 0:
                    k += 1
                    
                left += 1
        
        return right - left + 1


    def longestOnes_one(self, nums: List[int], k: int) -> int:

        # sliding window left and right
        left = right = -1

        # Slide the window to the right until the end of the list is reached
        while right < len(nums) - 1:

            right += 1

            # Flip a zero and decrement the counter
            if nums[right] == 0:
                k -= 1

            #  Maximum number of flips ?
            if k < 0:
                left += 1

                # Unflip this one
                if nums[left] == 0:
                    k += 1

        return right - left


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_ExampleOne(self):
        self.assertEqual(self.s.longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2), 6)

    def test_ExampleTwo(self):
        self.assertEqual(self.s.longestOnes([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3), 10)


unittest.main()
