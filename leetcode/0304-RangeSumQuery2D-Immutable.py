'''
304. Range Sum Query 2D - Immutable

Given a 2D matrix matrix, handle multiple queries of the following type:

    Calculate the sum of the elements of matrix inside the rectangle defined by its 
    upper left corner (row1, col1) and lower right corner (row2, col2).

Implement the NumMatrix class:
    NumMatrix(int[][] matrix) 
        Initializes the object with the integer matrix matrix.

    int sumRegion(int row1, int col1, int row2, int col2) 
        Returns the sum of the elements of matrix inside the rectangle defined by its 
        upper left corner (row1, col1) and lower right corner (row2, col2).

Example 1:
Input
["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
[[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
Output
[null, 8, 11, 12]

Explanation
NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
[3, 0, 1, 4, 2]
[5, 6, 3, 2, 1]
[1, 2, 0, 1, 5]
[4, 1, 0, 1, 7]
[1, 0, 3, 0, 5]

numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the * rectangle)
[3, 0, 1, 4, 2]
[5, 6, 3, 2, 1]
[1, *2, *0, *1, 5]
[4, *1, *0, *1, 7]
[1, *0, *3, *0, 5]

numMatrix.sumRegion(1, 1, 2, 2); // return 11 (i.e sum of the * rectangle)
[3, 0, 1, 4, 2]
[5, *6, *3, 2, 1]
[1, *2, *0, 1, 5]
[4, 1, 0, 1, 7]
[1, 0, 3, 0, 5]

numMatrix.sumRegion(1, 2, 2, 4); // return 12 (i.e sum of the * rectangle)
[3, 0, 1, 4, 2]
[5, 6, *3, *2, *1]
[1, 2, *0, *1, *5]
[4, 1, 0, 1, 7]
[1, 0, 3, 0, 5]

Constraints:
    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 200
    -10^5 <= matrix[i][j] <= 10^5
    0 <= row1 <= row2 < m
    0 <= col1 <= col2 < n
    At most 10^4 calls will be made to sumRegion.
'''
# Runtime: 104 ms       Your runtime beats 88.40 % of python3 submissions.
# Memory Usage: 17.3 MB Your memory usage beats 53.93 % of python3 submissions.

from itertools import product
class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        # pre calculate the sums of each matrix that starts at 0,0 and ends at each cell
        i, ii = len(matrix), len(matrix[0])

        # add an extra row of 0 for clarity; otherwise we need a bunch of -1 
        # and bounds checks to stay inside the matrix while populating
        self.dp = [[0] * (ii+1) for _ in range(i+1)] 

        for col, row in product(range(ii), range(i)):
            # each value is the sum of the previous calculated values above and to the left
            self.dp[row+1][col+1] = self.dp[row+1][col] + self.dp[row][col+1] - self.dp[row][col] + matrix[row][col]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # just need the four corner values now        
        return self.dp[row2+1][col2+1] - self.dp[row1][col2+1] - self.dp[row2+1][col1] + self.dp[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
obj = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
print(obj.sumRegion(2, 1, 4, 3))
print(obj.sumRegion(1, 1, 2, 2))
print(obj.sumRegion(1, 2, 2, 4))
