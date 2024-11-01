"""
392. Is Subsequence
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by 
deleting some (can be none) of the characters without disturbing the relative positions 
of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false

Constraints:
0 <= s.length <= 100
0 <= t.length <= 10^4
s and t consist only of lowercase English letters.
 

Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, 
and you want to check one by one to see if t has its subsequence. 
In this scenario, how would you change your code?
"""

# Runtime:          0 ms       our runtime beats 100.0 % of python3 submissions.
# Memory Usage: 16.71 MB Your memory usage beats  8.77 % of python3 submissions.

from itertools import product, permutations, combinations, zip_longest
from collections import namedtuple
from typing import List, Counter

import math


class Solution:

    def isSubsequence(self, s: str, t: str) -> bool:

        start = 0

        for i in s:
            location = t.find(i, start)

            # not found
            if location == -1:
                return False

            # found
            start = location + 1

        return True


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_ExampleOne(self):
        self.assertTrue(self.s.isSubsequence(s="abc", t="ahbgdc"))

    def test_ExampleTwo(self):
        self.assertFalse(self.s.isSubsequence(s="axc", t="ahbgdc"))

    def test_ExampleThree(self):
        self.assertFalse(self.s.isSubsequence(s="q", t="abc"))

    def test_ExampleFour(self):
        self.assertTrue(self.s.isSubsequence(s="ab", t="abc"))


unittest.main()
