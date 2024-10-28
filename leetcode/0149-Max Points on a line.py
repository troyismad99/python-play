"""
149. Max Points on a Line

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, 
return the maximum number of points that lie on the same straight line.

 

Example 1:
Input: points = [[1,1],[2,2],[3,3]]
Output: 3


Example 2:
Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4 

Constraints:

1 <= points.length <= 300
points[i].length == 2
-104 <= xi, yi <= 104
All the points are unique.
"""

# Runtime:        19 ms Your runtime beats 97.29 % of python3 submissions.
# Memory Usage: 16.79 MB Your memory usage beats 57.87 % of python3 submissions.

from typing import Counter, List
from itertools import product
from collections import defaultdict

from math import gcd


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:

        points.sort()

        # the number of points on the slope with the most points
        max_slope_points = 0

        slope = defaultdict(int)

        for i, (x1, y1) in enumerate(points):

            # for each point calculate the slope to all the other points
            slope.clear()

            for x2, y2 in points[i + 1 :]:

                dx, dy = x2 - x1, y2 - y1

                # avoid floating point division issues by using a ratio
                G = gcd(dx, dy)
                m = (dx // G, dy // G)

                # we are actually counting line segments with the same slope
                slope[m] += 1
                if slope[m] > max_slope_points:
                    max_slope_points = slope[m]

        # +1 to account for the start point
        # ... ie: the number of points on the line is one greater than the number of line segments
        return max_slope_points + 1


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_ExampleOne(self):
        self.assertEqual(self.s.maxPoints([[1, 1], [2, 2], [3, 3]]), 3)

    def test_ExampleTwo(self):
        self.assertEqual(self.s.maxPoints([[1, 1], [2, 2], [3, 8]]), 2)

    def test_ExampleThree(self):
        self.assertEqual(self.s.maxPoints([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]), 4)


unittest.main()
