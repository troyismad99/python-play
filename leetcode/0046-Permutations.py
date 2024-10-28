"""
46. Permutations

Given an array nums of distinct integers, return all the possible permutations. 
You can return the answer in any order.

 

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]
 

Constraints:
1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.

"""

# Runtime:          0 ms Your runtime beats 100 % of python3 submissions.
# Memory Usage: 16.70 MB Your memory usage beats 79.89 % of python3 submissions.

from typing import List
from itertools import product, combinations, permutations
from collections import namedtuple
import math


class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:

        def dfs(path, used, res):
        
            if len(path) == len(nums):
                res.append(path[:]) # note [:] make a deep copy since otherwise we'd be append the same list over and over
                return

            for i, letter in enumerate(nums):

                # skip used letters
                if used[i]:
                    continue
                
                # add letter to permutation, mark letter as used
                path.append(letter)
                used[i] = True
                
                dfs(path, used, res)
                
                # remove letter from permutation, mark letter as unused
                path.pop()
                used[i] = False
            
        res = []
        dfs([], [False] * len(nums), res)
        return res

    def permute_easy(self, nums: List[int]) -> List[List[int]]:

        return [list(i) for i in permutations(nums)]


import unittest


class TestSolution(unittest.TestCase):

    def compare_lists(self, list1, list2):
        section = list(set(list1).intersection(list2))
        return not section, section

    def setUp(self):
        self.s = Solution()

    def test_ExampleOne(self):
        self.assertTrue(self.s.permute([1]), [[1]])

    def test_ExampleTwo(self):
        self.assertTrue(self.s.permute([1, 2, 3]), [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])


unittest.main()
