'''
554. Brick Wall


There is a brick wall in front of you. The wall is rectangular and has several rows of bricks. 
The bricks have the same height but different width. 
You want to draw a vertical line from the top to the bottom and cross the least bricks.

The brick wall is represented by a list of rows. 
Each row is a list of integers representing the width of each brick in this row from left to right.

If your line go through the edge of a brick, then the brick is not considered as crossed. 
You need to find out how to draw the line to cross the least bricks and return the number of crossed bricks.

You cannot draw a line just along one of the two vertical edges of the wall, 
in which case the line will obviously cross no bricks.

Example:

Input: [[1,2,2,1],
        [3,1,2],
        [1,3,2],
        [2,4],
        [3,1,2],
        [1,3,1,1]]

Output: 2

Explanation: 
           |
[1][*2**][*2**][1]
[***3***][1][*2**]
[1][***3***][*2**]
[*2**][*****4****]
[***3***][1][*2**]
[1][***3***][1][1]
           ^
           |
Note:
    The width sum of bricks in different rows are the same and won't exceed INT_MAX.
    The number of bricks in each row is in range [1,10,000]. The height of wall is in range [1,10,000]. Total number of bricks of the wall won't exceed 20,000.

'''
# Runtime: 184 ms       Your runtime beats 57.40 % of python3 submissions.
# Memory Usage: 19.1 MB Your memory usage beats 62.25 % of python3 submissions.

from collections import defaultdict

class Solution:
    def leastBricks(self, wall: list[list[int]]) -> int:
        
        # we want the path that touches the most edges
        # we can find the edges with the widths, and then
        # get the width with the highest frequency

        freq = defaultdict(int)

        for row in wall:
            rowSum = row[0]
            for j in range(1, len(row)):
                freq[rowSum] += 1
                rowSum += row[j]

        # height - the most frequent edge count
        return len(wall) - max(freq.values() or [0])


s = Solution()
print(s.leastBricks([[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]))