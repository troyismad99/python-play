"""
345. Reverse Vowels of a String

Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:
Input: s = "IceCreAm"
Output: "AceCreIm"
Explanation:
The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:
Input: s = "leetcode"
Output: "leotcede"

Constraints:
1 <= s.length <= 3 * 10^5
s consist of printable ASCII characters.
"""

# Runtime:          7 ms       our runtime beats 92.51 % of python3 submissions.
# Memory Usage: 17.53 MB Your memory usage beats 51.62 % of python3 submissions.

from itertools import product, permutations, combinations, zip_longest
from collections import namedtuple
from typing import List, Counter

import math


class Solution:

    def reverseVowels(self, s: str) -> str:

        vowels = set("AEIOUaeiou")

        s = list(s)

        left = 0
        right = len(s) - 1

        while left < right:

            if s[left] not in vowels:
                left += 1

            elif s[right] not in vowels:
                right -= 1

            else:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        return "".join(s)


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
        self.assertEqual(self.s.reverseVowels("IceCreAm"), "AceCreIm")

    def test_ExampleTwo(self):
        self.assertEqual(self.s.reverseVowels("leetcode"), "leotcede")


unittest.main()
