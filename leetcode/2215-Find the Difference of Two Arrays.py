"""
2215. Find the Difference of Two Arrays

Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order.

Example 1:
Input: nums1 = [1,2,3], nums2 = [2,4,6]
Output: [[1,3],[4,6]]
Explanation:
For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].
For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums2. Therefore, answer[1] = [4,6].

Example 2:
Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
Output: [[3],[]]
Explanation:
For nums1, nums1[2] and nums1[3] are not present in nums2. Since nums1[2] == nums1[3], their value is only included once and answer[0] = [3].
Every integer in nums2 is present in nums1. Therefore, answer[1] = [].

Constraints:
1 <= nums1.length, nums2.length <= 1000
-1000 <= nums1[i], nums2[i] <= 1000
"""

# Runtime:          9 ms      your runtime beats 46.35 % of python3 submissions.
# Memory Usage: 16.75 MB Your memory usage beats 99.07 % of python3 submissions.

from itertools import product, permutations, combinations, zip_longest
from collections import namedtuple
from typing import List, Counter

import math


class Solution:


    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        nums1 = set(nums1)
        nums2 = set(nums2)
        uniq_nums1 = list(nums1 - nums2)
        uniq_nums2 = list(nums2 - nums1)
        return [uniq_nums1, uniq_nums2]


    def findDifference_one(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        answer1 = set()
        answer2 = set()

        for i in nums1:
            if i not in nums2:
                answer1.add(i)

        for i in nums2:
            if i not in nums1:
                answer2.add(i)

        return [list(answer1), list(answer2)]


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_ExampleOne(self):
        self.assertEqual(self.s.findDifference([1, 2, 3], [2, 4, 6]), [[1, 3], [4, 6]])

    def test_ExampleTwo(self):
        self.assertEqual(self.s.findDifference([1, 2, 3, 3], [1, 1, 2, 2]), [[3], []])


unittest.main()
