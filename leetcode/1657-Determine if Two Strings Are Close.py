"""
1657. Determine if Two Strings Are Close

Two strings are considered close if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb

Operation 2: Transform every occurrence of one existing character into another existing character, 
and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)

You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

Example 1:
Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"

Example 2:
Input: word1 = "a", word2 = "aa"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.

Example 3:
Input: word1 = "cabbba", word2 = "abbccc"
Output: true
Explanation: You can attain word2 from word1 in 3 operations.
Apply Operation 1: "cabbba" -> "caabbb"
Apply Operation 2: "caabbb" -> "baaccc"
Apply Operation 2: "baaccc" -> "abbccc"

Constraints:
1 <= word1.length, word2.length <= 10^5
word1 and word2 contain only lowercase English letters.
"""

# Runtime:         87 ms      your runtime beats 67.12 % of python3 submissions.
# Memory Usage: 17.28 MB Your memory usage beats 80.02 % of python3 submissions.

from itertools import product, permutations, combinations, zip_longest
from collections import namedtuple
from typing import List, Counter

import math


class Solution:

    def closeStrings(self, word1: str, word2: str) -> bool:

        if len(word1) != len(word2):
            return False

        w1 = Counter(word1)
        w2 = Counter(word2)

        #  are they already equal?
        if w1 == w2:
            return True

        # compare keys -> must have same letters
        if set(w1.keys()) != set(w2.keys()):
            return False

        # check the counts
        return sorted(w1.values()) == sorted(w2.values())


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_ExampleOne(self):
        self.assertTrue(self.s.closeStrings("abc", "bca"))

    def test_ExampleTwo(self):
        self.assertFalse(self.s.closeStrings("a", "aa"))

    def test_ExampleThree(self):
        self.assertTrue(self.s.closeStrings("cabbba", "abbccc"))


unittest.main()
