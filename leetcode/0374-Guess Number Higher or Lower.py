"""
374. Guess Number Higher or Lower
Easy
Topics
Companies
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked.

 

Example 1:

Input: n = 10, pick = 6
Output: 6
Example 2:

Input: n = 1, pick = 1
Output: 1
Example 3:

Input: n = 2, pick = 1
Output: 1
 

Constraints:

1 <= n <= 231 - 1
1 <= pick <= n
"""

# Runtime:         29 ms Your runtime beats 86.03 % of python3 submissions.
# Memory Usage: 16.69 MB Your memory usage beats 7.16 % of python3 submissions.

from typing import List
from itertools import product, combinations, permutations
from collections import namedtuple
import math


class Solution:

    def __init__(self, pick: int):
        self.pick = pick

    def guess(self, num: int) -> int:

        if num == self.pick:
            return 0

        return -1 if num > self.pick else 1

    def guessNumber(self, n: int) -> int:

        # The guess API is already defined for you.
        # @param num, your guess
        # @return -1 if num is higher than the picked number
        #          1 if num is lower than the picked number
        #          otherwise return 0
        # def guess(num: int) -> int:

        if n == 1:
            return 1

        low = 1
        high = n

        while True:

            mid = (low + high) // 2

            g = self.guess(mid)

            if g == 1:
                low = mid + 1

            elif g == -1:
                high = mid - 1

            else:
                return mid


import unittest


class TestSolution(unittest.TestCase):

    def compare_lists(self, list1, list2):

        if len(list1) != len(list2):
            return False

        if list1 == list2:
            return True

        return sorted(map(sorted, list1)) == sorted(map(sorted, list2))

    def setUp(self):
        self.s = Solution(1)

    def test_ExampleOne(self):
        self.s = Solution(6)
        self.assertEqual(self.s.guessNumber(10), 6)

    def test_ExampleTwo(self):
        self.s = Solution(1)
        self.assertEqual(self.s.guessNumber(1), 1)

    def test_ExampleThree(self):
        self.s = Solution(1)
        self.assertEqual(self.s.guessNumber(2), 1)

    def test_ExampleFour(self):
        self.s = Solution(2)
        self.assertEqual(self.s.guessNumber(2), 2)


unittest.main()
