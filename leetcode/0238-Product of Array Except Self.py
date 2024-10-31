"""
238. Product of Array Except Self
Given an integer array nums, return an array answer such that answer[i] is equal 
to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:
2 <= nums.length <= 105
-30 <= nums[i] <= 30

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 
Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""

# Runtime:         18 ms       our runtime beats 89.59 % of python3 submissions.
# Memory Usage: 22.21 MB Your memory usage beats 97.02 % of python3 submissions.

from itertools import product, permutations, combinations, zip_longest
from collections import namedtuple
from typing import List, Counter

import math


class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        prefix_product = 1
        postfix_product = 1
        result = [0] * n

        # first calculate the product of every cell prior to i
        for i in range(n):
            result[i] = prefix_product
            prefix_product *= nums[i]

        # second multiply all the cells that come after i
        for i in range(n - 1, -1, -1):
            result[i] *= postfix_product
            postfix_product *= nums[i]

        return result


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
        self.assertEqual(self.s.productExceptSelf([1, 2, 3, 4]), [24, 12, 8, 6])

    def test_ExampleTwo(self):
        self.assertEqual(self.s.productExceptSelf([-1, 1, 0, -3, 3]), [0, 0, 9, 0, 0])


unittest.main()
