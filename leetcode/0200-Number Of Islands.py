"""
200. Number of Islands
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), 
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

 

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

Output: 3


Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""

# Runtime:       244 ms Your runtime beats 57.55 % of python3 submissions.
# Memory Usage: 19.3 MB Your memory usage beats 45.01 % of python3 submissions.

from typing import Counter, List
from itertools import product


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        m, n = len(grid), len(grid[0])

        # checks for each cell when looking for neighbours
        neighbour_checks = [[1, 0], [-1, 0], [0, -1], [0, 1]]

        # each island found is marked with a unique 'marker'
        # marker starts at two since 0 and 1 are already used
        marker = 2

        # depth first search to find and mark all the islands
        # we re-use grid for this
        def dfs(t, i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j] == "1":
                grid[i][j] = t
                for x, y in neighbour_checks:
                    dfs(t, x + i, y + j)

        # find and mark all the islands in the grid, each with a unique number
        for x, y in product(range(m), range(n)):
            if grid[x][y] == "1":
                dfs(marker, x, y)
                marker += 1

        # where did marker end up from its start at 2?
        return marker - 2


def numIslands_old(self, grid: List[List[str]]) -> int:

    m, n = len(grid), len(grid[0])
    result = 0

    # checks for each cell when looking for neighbours
    neighbour_checks = [[1, 0], [-1, 0], [0, -1], [0, 1]]

    # each island found is marked with a unique 'marker'
    # marker starts at two since 0 and 1 are already used
    islands, marker = Counter(), 2

    # depth first search to find and mark all the islands
    # we re-use grid for this
    def dfs(t, i, j):
        if not 0 <= i < m or not 0 <= j < n or grid[i][j] != "1":
            return
        islands[t] += 1
        grid[i][j] = t
        for x, y in neighbour_checks:
            dfs(t, x + i, y + j)

    # find and mark all the islands in the grid, each with a unique number
    for x, y in product(range(m), range(n)):
        if grid[x][y] == "1":
            dfs(marker, x, y)
            marker += 1

    # print(grid)
    # print(islands)

    # where did marker end up?
    return marker - 2


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_ExampleOne(self):
        self.assertEqual(
            self.s.numIslands(
                [
                    ["1", "1", "1", "1", "0"],
                    ["1", "1", "0", "1", "0"],
                    ["1", "1", "0", "0", "0"],
                    ["0", "0", "0", "0", "0"],
                ]
            ),
            1,
        )

    def test_ExampleTwo(self):
        self.assertEqual(
            self.s.numIslands(
                [
                    ["1", "1", "0", "0", "0"],
                    ["1", "1", "0", "0", "0"],
                    ["0", "0", "1", "0", "0"],
                    ["0", "0", "0", "1", "1"],
                ]
            ),
            3,
        )


unittest.main()
