'''
329. Longest Increasing Path in a Matrix

Given an m x n integers matrix, return the length of the longest increasing 
path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. 
You may not move diagonally or move outside the boundary 
(i.e., wrap-around is not allowed).

Example 1:
    9    9   4
    ^
    6    6   8
    ^
    2 <- 1   1

    Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
    Output: 4
    Explanation: The longest increasing path is [1, 2, 6, 9].

Example 2:
    3 -> 4 -> 5
              \/
    3    2    6

    2    2    1

    Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
    Output: 4
    Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

Example 3:
    Input: matrix = [[1]]
    Output: 1 

Constraints:
    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 200
    0 <= matrix[i][j] <= 231 - 1
'''
# Runtime: 356 ms       Your runtime beats 95.58 % of python3 submissions.
# Memory Usage: 15.2 MB Your memory usage beats 68.51 % of python3 submissions.

class Solution:

    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        
        def dfs(i, ii):
            # if we don't have it, calculate it
            if not memo[i][ii]:
                val = matrix[i][ii]

                # calculate by gathering the scores form the 4 possible move directions
                memo[i][ii] = 1 + max(
                    dfs(i - 1, ii) if i and val > matrix[i - 1][ii] else 0,
                    dfs(i + 1, ii) if i < height - 1 and val > matrix[i + 1][ii] else 0,
                    dfs(i, ii - 1) if ii and val > matrix[i][ii - 1] else 0,
                    dfs(i, ii + 1) if ii < width - 1 and val > matrix[i][ii + 1] else 0)

            return memo[i][ii]

        # guard against empty
        if not matrix or not matrix[0]: 
            return 0

        # build our memoization matrix to remember scores from previously visited locations
        height, width = len(matrix), len(matrix[0])
        memo = [[0] * width for _ in range(height)]

        return max(dfs(x, y) for x in range(height) for y in range(width))

s = Solution()

print(s.longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]))
print(s.longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]]))
print(s.longestIncreasingPath([[1]]))