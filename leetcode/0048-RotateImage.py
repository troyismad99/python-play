'''
48. Rotate Image

You are given an n x n 2D matrix representing an image, 
rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
DO NOT allocate another 2D matrix and do the rotation.

Example 1:
    Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [[7,4,1],[8,5,2],[9,6,3]]

    1 2 3     7 4 1
    4 5 6  => 8 5 2
    7 8 9     9 6 3

Example 2:
    Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

    5  1  9 11     15 13  2   5
    2  4  8 10  => 14  3  4   1
   13  3  6  7     12  6  8   9
   15 14 12 16     16  7  10 11

Example 3:
    Input: matrix = [[1]]
    Output: [[1]]

Example 4:
    Input: matrix = [[1,2],[3,4]]
    Output: [[3,1],[4,2]]

Constraints:
    matrix.length == n
    matrix[i].length == n
    1 <= n <= 20
    -1000 <= matrix[i][j] <= 1000
'''
# Runtime: 28 ms        Your runtime beats 94.83 % of python3 submissions.
# Memory Usage: 14.4 MB

class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # to rotate in place we need a series of element swaps
        # each swap is a four element swap

        n = len(matrix)

        for i in range(n//2):
            for ii in range(n - n//2):
                matrix[i][ii], matrix[~ii][i], matrix[~i][~ii], matrix[ii][~i] = \
                         matrix[~ii][i], matrix[~i][~ii], matrix[ii][~i], matrix[i][ii]

import unittest

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_ExampleOne(self):
        e = [[1,2,3],[4,5,6],[7,8,9]]
        a = [[7,4,1],[8,5,2],[9,6,3]]
        self.s.rotate(e)
        self.assertEqual(e, a)

    def test_ExampleTwo(self):
        e = [[1]]
        a = [[1]]
        self.s.rotate(e)
        self.assertEqual(e, a)

    def test_ExampleThree(self):
        e = [[1,2,3],[4,5,6],[7,8,9]]
        a = [[7,4,1],[8,5,2],[9,6,3]]
        self.s.rotate(e)
        self.assertEqual(e, a)

    def test_ExampleFour(self):
        e = [[1,2],[3,4]]
        a = [[3,1],[4,2]]
        self.s.rotate(e)
        self.assertEqual(e, a)

unittest.main()
