"""
1456. Maximum Number of Vowels in a Substring of Given Length

Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Example 1:
Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.

Example 2:
Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.

Example 3:
Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.

Constraints:
1 <= s.length <= 10^5
s consists of lowercase English letters.
1 <= k <= s.length
"""

# Runtime:        101 ms       our runtime beats 38.39 % of python3 submissions.
# Memory Usage: 17.04 MB Your memory usage beats 93.80 % of python3 submissions.

from itertools import product, permutations, combinations, zip_longest
from collections import namedtuple
from typing import List, Counter

import math


class Solution:

    def maxVowels(self, s: str, k: int) -> int:

        vowels = set("aeiou")

        # start with the first k elements
        max_vowel = sum(char in vowels for char in s[:k])

        # tracks the number of vowels in our sliding window
        current_count = max_vowel

        for i in range(k, len(s)):

            # Each iteration we check:
            # the char entering the window
            # the char leaving the window 
            # and adjust the vowel counts as needed

            current_count += s[i] in vowels
            current_count -= s[i - k] in vowels

            # Check for a new max
            max_vowel = max(max_vowel, current_count)

        return max_vowel


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_ExampleOne(self):
        self.assertEqual(self.s.maxVowels("abciiidef", 3), 3)

    def test_ExampleTwo(self):
        self.assertEqual(self.s.maxVowels("aeiou", 2), 2)

    def test_ExampleThree(self):
        self.assertEqual(self.s.maxVowels("leetcode", 3), 2)


unittest.main()
