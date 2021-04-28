'''
63. Unique Paths II

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and space is marked as 1 and 0 respectively in the grid.

Example 1:
    -------
    |S| | |
    -------
    | |*| |
    -------
    | | |F|
    -------

    Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    Output: 2
    Explanation: There is one obstacle in the middle of the 3x3 grid above.
    There are two ways to reach the bottom-right corner:
    1. Right -> Right -> Down -> Down
    2. Down -> Down -> Right -> Right

Example 2:
    Input: obstacleGrid = [[0,1],[0,0]]
    Output: 1

Constraints:
    m == obstacleGrid.length
    n == obstacleGrid[i].length
    1 <= m, n <= 100
    obstacleGrid[i][j] is 0 or 1.
'''
# Runtime: 32 ms        Your runtime beats 98.52 % of python3 submissions.
# Memory Usage: 14.4 MB Your memory usage beats 33.38 % of python3 submissions.

from itertools import product

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:

        # guard against bad grid
        if not obstacleGrid or not obstacleGrid[0] or obstacleGrid[0][0] or obstacleGrid[~0][~0]: 
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])

        # mark where we have been
        dp = [[0] * n for _ in range(m)]

        dp[0][0] = int(obstacleGrid[0][0] == 0)

        print(product(range(m), range(n)))

        for i, j in product(range(m), range(n)):

            # is this an obstacle?
            if obstacleGrid[i][j] == 1:
                continue

            # check if we can visit here from above or left
            if i > 0: 
                dp[i][j] += dp[i-1][j]
            if j > 0: 
                dp[i][j] += dp[i][j-1]

        # return the bottom right corner
        return dp[-1][-1]

import unittest

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_ExampleOne(self):
        self.assertEqual(self.s.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]), 2)

    def test_ExampleTwo(self):
        self.assertEqual(self.s.uniquePathsWithObstacles([[0,1],[0,0]]), 1)


unittest.main()
