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

# Runtime:        43 ms Your runtime beats 96.53 % of python3 submissions.
# Memory Usage: 58.79 MB Your memory usage beats 89.89 % of python3 submissions.

from typing import List
from itertools import product, combinations, permutations
from collections import namedtuple
import math


class Solution:

    def combine(self, n: int, k: int) -> List[List[int]]:

        answer = []

        def backtrack(remain, comb, nex):

            # solution found
            if remain == 0:
                answer.append(comb.copy())

            else:
                # iterate through all possible candidates
                for i in range(nex, n + 1):
                    # add
                    comb.append(i)
                    # check
                    backtrack(remain - 1, comb, i + 1)
                    # remove
                    comb.pop()

        backtrack(k, [], 1)
        return answer

    def combine_easy(self, n: int, k: int) -> List[List[int]]:
        return [list(i) for i in combinations(range(1, n + 1), k)]


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
        self.assertTrue(self.compare_lists(self.s.combine(1, 1), [[1]]))

    def test_ExampleTwo(self):
        self.assertTrue(self.compare_lists(self.s.combine(4, 2), [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]))


unittest.main()
