"""
334. Increasing Triplet Subsequence
Given an integer array nums, return true if there exists a triple of indices (i, j, k) 
such that i < j < k and nums[i] < nums[j] < nums[k]. 
If no such indices exists, return false.

Example 1:
Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.

Example 2:
Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.

Example 3:
Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.

Constraints:
1 <= nums.length <= 5 * 10^5
-2^31 <= nums[i] <= 2^31 - 1
 
Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?
"""

# Runtime:         14 ms       our runtime beats 84.62 % of python3 submissions.
# Memory Usage: 36.47 MB Your memory usage beats 14.04 % of python3 submissions.

from itertools import product, permutations, combinations, zip_longest
from collections import namedtuple
from typing import List, Counter

import math


class Solution:

    def increasingTriplet(self, nums: List[int]) -> bool:

        if len(nums) < 3:
            return False

        first = second = math.inf

        # confusing part is that this doesn't identify the three numbers:
        # ... just that there are three
        for num in nums:

            # if all numbers are in decreasing order we will never get past his one...
            # ... ie we will never compare the other numbers
            if num <= first:
                first = num

            # once we have a value that is larger than the 'first' we have a second
            elif num <= second:
                second = num

            # to get here num must be larger than both first and second
            else:
                return True

        return False

        # contiguous answer
        # return any(nums[i] < nums[i + 1] < nums[i + 2] for i in range(len(nums) - 2))


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
        self.assertEqual(self.s.increasingTriplet([1, 2, 3, 4, 5]), True)

    def test_ExampleTwo(self):
        self.assertEqual(self.s.increasingTriplet([5, 4, 3, 2, 1]), False)

    def test_ExampleThree(self):
        self.assertEqual(self.s.increasingTriplet([2, 1, 5, 0, 4, 6]), True)

    def test_ExampleFour(self):
        self.assertEqual(self.s.increasingTriplet([20, 100, 10, 12, 5, 13]), True)


# self.assertFalse(function_name(123))
# self.assertTrue(function_name(123))
# self.assertIn(self.s.function_name(123), [1, 2])
# self.assertTrue(self.compare_lists(self.s.function_name([2, 5, 2, 1, 2], 5), [[1, 2, 2], [5]]))

unittest.main()
