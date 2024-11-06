"""
1679. Max Number of K-Sum Pairs

You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.

Example 1:
Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.

Example 2:
Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.
 

Constraints:
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
1 <= k <= 10^9
"""

# Runtime:         xx ms       our runtime beats xxxxx % of python3 submissions.
# Memory Usage: xxxxx MB Your memory usage beats xxxxx % of python3 submissions.

from itertools import product, permutations, combinations, zip_longest
from collections import namedtuple, Counter
from typing import List, Counter

import math


class Solution:

    def maxOperations(self, nums: List[int], k: int) -> int:
        # Runtime:        471 ms       our runtime beats 96.17 % of python3 submissions.
        # Memory Usage: 29.70 MB Your memory usage beats 20.20 % of python3 submissions.
        pairs = 0

        count = Counter(nums)

        for i in count:
            complement = k - i
            if complement in count:
                pairs += count[i] // 2 if i == complement else min(count[i], count[complement])
                count[i] = 0
                count[complement] = 0

        return pairs

    def maxOperations_one(self, nums: List[int], k: int) -> int:
        # Runtime:        481 ms       our runtime beats 87.85 % of python3 submissions.
        # Memory Usage: 28.97 MB Your memory usage beats 51.52 % of python3 submissions.
        pairs = 0

        # two pointers requires a sorted array
        nums.sort()

        left = 0
        right = len(nums) - 1

        while left < right:

            pair_sum = nums[left] + nums[right]

            if pair_sum == k:
                pairs += 1
                left += 1
                right -= 1

            elif pair_sum < k:
                left += 1

            else:
                right -= 1

        return pairs


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_ExampleOne(self):
        self.assertEqual(self.s.maxOperations([1, 2, 3, 4], 5), 2)

    def test_ExampleTwo(self):
        self.assertEqual(self.s.maxOperations([3, 1, 3, 4, 3], 6), 1)


unittest.main()
