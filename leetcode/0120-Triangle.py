'''
120. Triangle

Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. 
More formally, if you are on index i on the current row, 
you may move to either index i or index i + 1 on the next row.

Example 1:
    Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    Output: 11
    Explanation: The triangle looks like:
       2
      3 4
     6 5 7
    4 1 8 3
    The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

Example 2:
    Input: triangle = [[-10]]
    Output: -10

Constraints:
    1 <= triangle.length <= 200
    triangle[0].length == 1
    triangle[i].length == triangle[i - 1].length + 1
    -10^4 <= triangle[i][j] <= 10^4

 
Follow up: Could you do this using only O(n) extra space, where n is the total number of rows in the triangle?
'''
# Runtime: 76 ms        Your runtime beats 9.42 % of python3 submissions.
# Memory Usage: 15.2 MB Your memory usage beats 26.71 % of python3 submissions.

class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:

        # work our way from the bottom up
        # the last row becomes our first entries into the result array. 
        # Each subsequent row determines which value to add to keep the smallest result. 
        # Technically after each row is processed the array could shrink by one element.
        result = [0] * (len(triangle) + 1)

        for row in triangle[::-1]:
            for i in range(len(row)):
                result[i] = row[i] + min(result[i], result[i + 1])
        
        return result[0]

s = Solution()

print(s.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))
print(s.minimumTotal([[-10]]))
