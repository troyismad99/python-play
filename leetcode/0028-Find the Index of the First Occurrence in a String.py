"""
28. Find the Index of the First Occurrence in a String

Given two strings needle and haystack, return the index of the first occurrence of 
needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 
Constraints:
1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.

"""

# Runtime:          0 ms Your runtime beats 100 % of python3 submissions.
# Memory Usage: 16.80 MB Your memory usage beats 12.26 % of python3 submissions.

from typing import List
from itertools import product, combinations
from collections import namedtuple
import math


class Solution:

    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_ExampleOne(self):
        # self.assertEqual(self.s.longestPalindrome("babad"), "bab")
        self.assertEqual(self.s.strStr("sadbutsad", "sad"), 0)

    def test_ExampleTwo(self):
        self.assertEqual(self.s.strStr("leetcode", "leeto"), -1)


unittest.main()
