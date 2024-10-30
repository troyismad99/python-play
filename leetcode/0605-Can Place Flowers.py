"""
605. Can Place Flowers

You have a long flowerbed in which some of the plots are planted, and some are not. 
However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, 
and an integer n, return true if n new flowers can be planted in the flowerbed without 
violating the no-adjacent-flowers rule and false otherwise.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
 

Constraints:
1 <= flowerbed.length <= 2 * 10^4
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
"""

# Runtime:          2 ms       our runtime beats 95.97% of python3 submissions.
# Memory Usage: 17.13 MB Your memory usage beats 11.94% of python3 submissions.

from itertools import product
from collections import namedtuple
from typing import List


class Solution:

    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        if n == 0:
            return True

        for i in range(len(flowerbed)):

            if (
                flowerbed[i] == 0
                and (i == 0 or flowerbed[i - 1] == 0)
                and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)
            ):

                flowerbed[i] = 1
                n -= 1

                if n == 0:
                    return True

        return False

    # Runtime:         11 ms       our runtime beats 34.61% of python3 submissions.
    # Memory Usage: 16.93 MB Your memory usage beats 41.72% of python3 submissions.
    def canPlaceFlowers_one(self, flowerbed: List[int], n: int) -> bool:

        if n == 0:
            return True

        planted_flowers = 0

        for i, plot in enumerate(flowerbed):

            #  check if this spot is a candidate
            if plot == 1:
                continue

            # check to the left
            if i > 0 and flowerbed[i - 1] == 1:
                continue

            #  check to the right
            if i != len(flowerbed) - 1 and flowerbed[i + 1] == 1:
                continue

            flowerbed[i] = 1
            planted_flowers += 1

            if planted_flowers == n:
                return True

        return planted_flowers == n


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_ExampleOne(self):
        self.assertEqual(self.s.canPlaceFlowers([1, 0, 0, 0, 1], 1), True)

    def test_ExampleTwo(self):
        self.assertEqual(self.s.canPlaceFlowers([1, 0, 0, 0, 1], 2), False)

    def test_ExampleThree(self):
        self.assertEqual(self.s.canPlaceFlowers([1, 0, 0, 0, 1, 0, 0], 2), True)


unittest.main()
