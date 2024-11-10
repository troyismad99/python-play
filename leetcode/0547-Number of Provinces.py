"""
547. Number of Provinces

There are n cities. Some of them are connected, while some are not. 
If city a is connected directly with city b, and city b is connected directly with city c, 
then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

Example 1:
CITY |0 1 2
------|------
     0|1 1 0 
     1|1 1 0
     2|0 0 1

Connections:
0 ► 1
1 ► 0
2 ► none

Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2

Example 2:

 |0 1 2
-|------
0|1 0 0 
1|0 1 0
2|0 0 1

Connections:
0 ► none
1 ► none
2 ► none
Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3

Constraints:
1 <= n <= 200
n == isConnected.length
n == isConnected[i].length
isConnected[i][j] is 1 or 0.
isConnected[i][i] == 1
isConnected[i][j] == isConnected[j][i]
"""

# Runtime:          3 ms     your runtime beats 89.80 % of python3 submissions.
# Memory Usage: 18.40 MB Your memory usage beats 9.72 % of python3 submissions.

from itertools import product, permutations, combinations, zip_longest
from collections import namedtuple
from typing import List, Counter

import math


class Solution:

    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        def visit_city(city):

            visited[city] = True

            for adjacent_city, connected in enumerate(isConnected[city]):
                if not visited[adjacent_city] and connected:
                    visit_city(adjacent_city)

        city_count = len(isConnected)

        visited = [False] * city_count
        provinces = 0

        for city in range(city_count):

            #  have we been here?
            if not visited[city]:
                visit_city(city)
                provinces += 1

        return provinces


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_ExampleOne(self):
        self.assertEqual(self.s.findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]), 2)

    def test_ExampleTwo(self):
        self.assertEqual(self.s.findCircleNum([[1, 0, 0], [0, 1, 0], [0, 0, 1]]), 3)

    def test_ExampleThree(self):
        self.assertEqual(self.s.findCircleNum([[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]), 1)


unittest.main()
