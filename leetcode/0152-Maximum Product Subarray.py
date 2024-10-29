"""
152. Maximum Product Subarray

Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 

Constraints:
1 <= nums.length <= 2 * 10^4
-10 <= nums[i] <= 10
The product of any subarray of nums is guaranteed to fit in a 32-bit integer.
"""

# Runtime:          7 ms Your runtime beats 90.43 % of python3 submissions.
# Memory Usage: 17.26 MB Your memory usage beats 163.77 % of python3 submissions.

from typing import List
from itertools import product, combinations, permutations
from collections import namedtuple
import math


class Solution:

    def maxProduct(self, nums: List[int]) -> int:

        # Also keep track of smallest value:
        # .. negative list values can be multiplied togethor
        current_max, current_minimum = 1, 1

        max_product = nums[0]

        for n in nums:
            # three possible cases to consider
            candidates = (n, n * current_max, n * current_minimum)

            current_max = max(candidates)
            current_minimum = min(candidates)

            max_product = max(max_product, current_max)

        return max_product


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
        self.assertEqual(self.s.maxProduct([2, 3, -2, 4]), 6)

    def test_ExampleTwo(self):
        self.assertEqual(self.s.maxProduct([-2, 0, -1]), 0)

    def test_ExampleThree(self):
        self.assertEqual(self.s.maxProduct([-2, 3, -4]), 24)

unittest.main()
