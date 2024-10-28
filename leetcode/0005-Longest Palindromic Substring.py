"""
5. Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"
 

Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters.

"""

# Runtime:        236 ms Your runtime beats 81.28 % of python3 submissions.
# Memory Usage: 16.51 MB Your memory usage beats 80.92 % of python3 submissions.

from typing import List
from itertools import product, combinations
from collections import namedtuple
import math


class Solution:

    def longestPalindrome(self, s: str) -> str:

        def expand_from_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1 : right]

        candidate = s[0]

        for i in range(len(s) - 1):
            # palidromes can have an odd or even number of letters ex aba or abba
            odd = expand_from_center(i, i)
            even = expand_from_center(i, i + 1)

            if len(odd) > len(candidate):
                candidate = odd
            if len(even) > len(candidate):
                candidate = even

        return candidate


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_ExampleOne(self):
        # self.assertEqual(self.s.longestPalindrome("babad"), "bab")
        self.assertIn(self.s.longestPalindrome("babad"), ["bab", "aba"])

    def test_ExampleTwo(self):
        self.assertEqual(self.s.longestPalindrome("cbbd"), "bb")


unittest.main()
