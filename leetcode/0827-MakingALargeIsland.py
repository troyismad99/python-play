'''
You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1s.

Example 1:
    Input: grid = [[1,0],[0,1]]
    Output: 3
    Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.

Example 2:
    Input: grid = [[1,1],[1,0]]
    Output: 4
    Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.

Example 3:
    Input: grid = [[1,1],[1,1]]
    Output: 4
    Explanation: Can't change any 0 to 1, only one island with area = 4.

 

Constraints:
    n == grid.length
    n == grid[i].length
    1 <= n <= 500
    grid[i][j] is either 0 or 1.
'''

# Runtime:      3584 ms Your runtime beats 67.09 % of python3 submissions.
# Memory Usage: 23.8 MB Your memory usage beats 74.75 % of python3 submissions.

from typing import Counter
from itertools import product

class Solution:
    def largestIsland(self, grid: list[list[int]]) -> int:

        m, n = len(grid), len(grid[0])
        result = 0

        # checks for each cell when looking for neighbours
        neighbour_checks = [[1,0],[-1,0],[0,-1],[0,1]]

        # each island found is marked with a unique 'marker'
        # marker starts at two since 0 and 1 are already used        
        islands, marker = Counter(), 2
        
        # depth first search to find and mark all the islands
        # we re-use grid for this
        def dfs(t, i, j):
            if not 0 <= i < m or not 0 <= j < n or grid[i][j] != 1: 
                return
            islands[t] += 1
            grid[i][j] = t
            for x, y in neighbour_checks: 
                dfs(t, x+i, y+j)
        
        # find and mark all the islands in the grid, each with a unique number
        for x, y in product(range(m), range(n)):
            if grid[x][y] == 1:
                dfs(marker, x, y)
                marker += 1
                
        # print(grid)
        # print(islands)

        # which zero can we flip to make the biggest island?
        for x, y in product(range(m), range(n)):

            # we only care about the zeros
            if grid[x][y] != 0: 
                continue

            # keep track of the islands that border this zero 
            neighbours = set()
            for dx, dy in neighbour_checks:
                if 0 <= x + dx < m and 0 <= y + dy < n and grid[x+dx][y+dy] != 0:
                    neighbours.add(grid[x+dx][y+dy])

            # get the sum of all the neighbour islands that would become one island
            result = max(result, sum(islands[i] for i in neighbours) + 1)
            
        return result if result != 0 else m*n

s = Solution()

print(s.largestIsland([[1,0],[0,1]]))
print(s.largestIsland([[1,1],[1,0]]))
print(s.largestIsland([[1,1],[1,1]]))

print(s.largestIsland([[1,0,0],[0,1,1],[1,0,0]]))


print(s.largestIsland([[1,0,0,0,1],
                       [0,1,1,0,1],
                       [1,0,0,1,1]]))