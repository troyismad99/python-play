"""
724. Find Pivot Index

Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the 
left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. 
This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

Example 1:
Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11

Example 2:
Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.

Example 3:
Input: nums = [2,1,-1]
Output: 0
Explanation:
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + -1 = 0
 
Constraints:

1 <= nums.length <= 10^4
-1000 <= nums[i] <= 1000
"""

# Runtime:         14 ms      your runtime beats 24.41 % of python3 submissions.
# Memory Usage: 18.04 MB Your memory usage beats  5.49 % of python3 submissions.

from itertools import product, permutations, combinations, zip_longest
from collections import namedtuple
from typing import List, Counter

import math


class Solution:

    def pivotIndex(self, nums: List[int]) -> int:

        '''
            for i in range(len(nums)):
                if sum(nums[:i])==sum(nums[i+1:]):
                    return i
        
            return -1
        '''

        n = len(nums)

        sum_left = [0] * n
        sum_right = [0] * n

        #  populate the lefts
        for i in range(1, n):
            sum_left[i] = sum_left[i - 1] + nums[i - 1]

        #  populate the rights
        for i in range(n - 2, -1, -1):
            sum_right[i] = sum_right[i + 1] + nums[i + 1]


        return next((i for i in range(n) if sum_left[i] == sum_right[i]), -1)

        # for i in range(n):
        #     if sum_left[i] == sum_right[i]:
        #         return i

        # return -1


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_ExampleOne(self):
        self.assertEqual(self.s.pivotIndex([1, 7, 3, 6, 5, 6]), 3)

    def test_ExampleTwo(self):
        self.assertEqual(self.s.pivotIndex([1, 2, 3]), -1)

    def test_ExampleThree(self):
        self.assertEqual(self.s.pivotIndex([2, 1, -1]), 0)


unittest.main()
