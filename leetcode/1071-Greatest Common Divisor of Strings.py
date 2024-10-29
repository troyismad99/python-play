"""
1071. Greatest Common Divisor of Strings

For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t 
(i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

Example 1:
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Example 2:
Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Example 3:
Input: str1 = "LEET", str2 = "CODE"
Output: ""
 

Constraints:
1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.
"""

# Runtime:         0  ms Your runtime beats 100 % of python3 submissions.
# Memory Usage: 16.56 MB Your memory usage beats 64.55 % of python3 submissions.

from typing import List
from itertools import product, combinations, permutations
from collections import namedtuple
import math
from math import gcd


class Solution:

    def gcdOfStrings(self, str1: str, str2: str) -> str:

        return "" if str1 + str2 != str2 + str1 else str1[: gcd(len(str1), len(str2))]


import unittest


class TestSolution(unittest.TestCase):

    def compare_lists(self, list1, list2):

        if len(list1) != len(list2):
            return False

        if list1 == list2:
            return True

        return sorted(map(sorted, list1)) == sorted(map(sorted, list2))

    def setUp(self):
        self.s = Solution()

    def test_ExampleOne(self):
        self.assertEqual(self.s.gcdOfStrings("ABCABC", "ABC"), "ABC")

    def test_ExampleTwo(self):
        self.assertEqual(self.s.gcdOfStrings("ABABAB", "ABAB"), "AB")

    def test_ExampleThree(self):
        self.assertEqual(self.s.gcdOfStrings("LEET", "CODE"), "")

    def test_ExampleFour(self):
        self.assertEqual(
            self.s.gcdOfStrings("TAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"), "TAUXX"
        )


unittest.main()
