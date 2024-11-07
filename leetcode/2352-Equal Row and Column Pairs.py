"""
2352. Equal Row and Column Pairs

Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) 
such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements 
in the same order (i.e., an equal array).

Example 1:
Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]

Example 2:
Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]

Constraints:
n == grid.length == grid[i].length
1 <= n <= 200
1 <= grid[i][j] <= 10^5
"""

# Runtime:        155 ms      your runtime beats 23.62 % of python3 submissions.
# Memory Usage: 21.22 MB Your memory usage beats 83.84 % of python3 submissions.

from itertools import product, permutations, combinations, zip_longest
from collections import namedtuple
from typing import List, Counter

import math


class Solution:

    def equalPairs(self, grid: List[List[int]]) -> int:

        grid2 = [list(col) for col in zip(*grid)]
        return sum(row == col for row, col in product(grid, grid2))


    def equalPairs_working(self, grid: List[List[int]]) -> int:

        grid2 = []

        for i in range(len(grid[0])):
            # col = []

            # for ii in range(len(grid)):
            #     col.append(grid[ii][i])
            
            col = [item[i] for item in grid]
            grid2.append(col)

        a = 0

        for row, col in product(grid, grid2):
            if row == col:
                a += 1

        return a




import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_ExampleOne(self):
        self.assertEqual(self.s.equalPairs([[3, 2, 1], [1, 7, 6], [2, 7, 7]]), 1)

    def test_ExampleTwo(self):
        self.assertEqual(self.s.equalPairs([[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]), 3)

    def test_ExampleThree(self):
        self.assertEqual(self.s.equalPairs([[13, 13], [13, 13]]), 4)

    def test_ExampleFour(self):
        self.assertEqual(self.s.equalPairs([[2, 1], [1, 34]]), 2)


unittest.main()
