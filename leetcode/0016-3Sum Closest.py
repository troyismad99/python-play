"""
16. 3Sum Closest

Given an integer array nums of length n and an integer target, find three integers in nums 
such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2:
Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 

Constraints:
3 <= nums.length <= 500
-1000 <= nums[i] <= 1000
-104 <= target <= 104

"""

# Runtime:        344 ms Your runtime beats 55.70 % of python3 submissions.
# Memory Usage: 16.59 MB Your memory usage beats 86.25 % of python3 submissions.

from typing import List
from itertools import product, combinations
from collections import namedtuple
import math


class Solution:


    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()
        closest_sum = float('inf')

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if abs(target - current_sum) < abs(target - closest_sum):
                    closest_sum = current_sum

                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return current_sum

        return closest_sum




    def threeSumClosest_slow(self, nums: List[int], target: int) -> int:

        candidate = 0
        delta = math.inf

        for i, j, k in combinations(nums, 3):

            c = i + j + k

            d = abs(target - c)

            if d < delta:
                candidate = c
                delta = d

        return candidate


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_ExampleOne(self):
        self.assertEqual(self.s.threeSumClosest([-1, 2, 1, -4], 1), 2)

    def test_ExampleTwo(self):
        self.assertEqual(self.s.threeSumClosest([0, 0, 0], 1), 0)


unittest.main()
