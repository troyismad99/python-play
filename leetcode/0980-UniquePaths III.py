"""
980. Unique Paths III

You are given an m x n integer array grid where grid[i][j] could be:

1 representing the starting square. There is exactly one starting square.
2 representing the ending square. There is exactly one ending square.
0 representing empty squares we can walk over.
-1 representing obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to 
the ending square, that walk over every non-obstacle square exactly once.

 

Example 1:
Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)



Example 2:
Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)

Example 3:
Input: grid = [[0,1],[2,0]]
Output: 0
Explanation: There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 20
1 <= m * n <= 20
-1 <= grid[i][j] <= 2
There is exactly one starting cell and one ending cell.
"""

# Runtime: 7 ms        Your runtime beats 99.69% of python3 submissions.
# Memory Usage: 16.66 MB Your memory usage beats 42.01% of python3 submissions.

from itertools import product
from collections import namedtuple
from typing import List

class Solution:
      def uniquePathsIII(self, grid: List[List[int]]) -> int:

        sx, sy, ex, ey, ec = 0, 0, 0, 0, 1
        m = len(grid)
        n = len(grid[0])

        for x in range(m):
            for y in range(n):

                if grid[x][y] == 1:
                    # start
                    sx, sy = x, y
                
                elif grid[x][y] == 2:
                    #end
                    ex, ey = x, y
                
                elif grid[x][y] == 0:
                    # count cells we need to visit
                    ec += 1

        def dfs(x, y, rem):
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == -1:
                return 0
            if (x, y) == (ex, ey):
                return 1 if rem == 0 else 0

            grid[x][y] = -1
            total_paths = (
                dfs(x + 1, y, rem - 1) + dfs(x, y + 1, rem - 1) + dfs(x - 1, y, rem - 1) + dfs(x, y - 1, rem - 1)
            )
            grid[x][y] = 0

            return total_paths

        return dfs(sx, sy, ec)


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_ExampleOne(self):
        self.assertEqual(self.s.uniquePathsIII([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]), 2)

    def test_ExampleTwo(self):
        self.assertEqual(self.s.uniquePathsIII([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]), 4)

    def test_ExampleThree(self):
        self.assertEqual(self.s.uniquePathsIII([[0, 1], [2, 0]]), 0)


unittest.main()
