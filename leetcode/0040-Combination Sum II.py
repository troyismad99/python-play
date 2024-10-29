"""
40. Combination Sum II

Given a collection of candidate numbers (candidates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
 

Constraints:
1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
"""

# Runtime:         22 ms Your runtime beats 58.62 % of python3 submissions.
# Memory Usage: 16.80 MB Your memory usage beats 18.92 % of python3 submissions.

from typing import List
from itertools import product, combinations, permutations
from collections import namedtuple
import math


class Solution:

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)

        return [list(tup) for tup in {tuple(sublist) for sublist in res}]

    def dfs(self, nums, target, index, path, res):

        if target < 0:
            return

        if target == 0:
            res.append(path)
            return

        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue

            self.dfs(nums, target - nums[i], i + 1, path + [nums[i]], res)


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
        self.assertTrue(
            self.compare_lists(
                self.s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8), [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
            )
        )

    def test_ExampleTwo(self):
        self.assertTrue(self.compare_lists(self.s.combinationSum2([2, 5, 2, 1, 2], 5), [[1, 2, 2], [5]]))


unittest.main()
