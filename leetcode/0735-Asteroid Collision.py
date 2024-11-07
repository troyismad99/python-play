"""
735. Asteroid Collision

We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction 
(positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, 
the smaller one will explode. If both are the same size, both will explode. 
Two asteroids moving in the same direction will never meet.

Example 1:
Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

Example 2:
Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.

Example 3:
Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.

Constraints:
2 <= asteroids.length <= 104
-1000 <= asteroids[i] <= 1000
asteroids[i] != 0
"""

# Runtime:          7 ms      your runtime beats 59.95 % of python3 submissions.
# Memory Usage: 17.95 MB Your memory usage beats 14.42 % of python3 submissions.

from itertools import product, permutations, combinations, zip_longest
from collections import namedtuple
from typing import List, Counter

import math


class Solution:

    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        asteroid_stack = []

        for asteroid in asteroids:

            # is this one moving right?
            if asteroid > 0:
                #  just track it
                asteroid_stack.append(asteroid)

            else:
                # we have a left moving asteroid

                # are there any previous right moving asteroids for it to collide with?
                while asteroid_stack and asteroid_stack[-1] > 0 and asteroid_stack[-1] < abs(asteroid):
                    asteroid_stack.pop()

                # same size: both explode
                if asteroid_stack and asteroid_stack[-1] == abs(asteroid):
                    asteroid_stack.pop()

                # append any left moving that will never collide
                elif not asteroid_stack or asteroid_stack[-1] < 0:
                    asteroid_stack.append(asteroid)

        return asteroid_stack


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_ExampleOne(self):
        self.assertEqual(self.s.asteroidCollision([5, 10, -5]), [5, 10])

    def test_ExampleTwo(self):
        self.assertEqual(self.s.asteroidCollision([8, -8]), [])

    def test_ExampleThree(self):
        self.assertEqual(self.s.asteroidCollision([10, 2, -5]), [10])

    def test_ExampleFour(self):
        self.assertEqual(self.s.asteroidCollision([-2, -1, 1, 2]), [-2, -1, 1, 2])


unittest.main()
