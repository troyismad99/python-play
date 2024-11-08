"""
394. Decode String

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets 
is being repeated exactly k times. 

Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, 
square brackets are well-formed, etc. Furthermore, you may assume that the original data 
does not contain any digits and that digits are only for those repeat numbers, k. 

For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 10^5.

Example 1:
Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Example 2:
Input: s = "3[a2[c]]"
Output: "accaccacc"

Example 3:
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"

Constraints:
1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].
"""

# Runtime:          0 ms      your runtime beats   100 % of python3 submissions.
# Memory Usage: 16.47 MB Your memory usage beats 85.62 % of python3 submissions.

from itertools import product, permutations, combinations, zip_longest
from collections import namedtuple
from typing import List, Counter

import math


class Solution:

    def decodeString(self, s: str) -> str:

        stack = []
        current_k = 0
        current_s = ""

        for c in s:
            if c == "[":
                # save where we are
                stack.append((current_k, current_s))
                current_k = 0
                current_s = ""

            elif c == "]":
                # grab what we had
                previous_k, previous_s = stack.pop()
                current_s = previous_s + previous_k * current_s

            elif c.isdigit():
                current_k = current_k * 10 + int(c)
            else:
                current_s += c

        return current_s


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_ExampleOne(self):
        self.assertEqual(self.s.decodeString("3[a]2[bc]"), "aaabcbc")

    def test_ExampleTwo(self):
        self.assertEqual(self.s.decodeString("3[a2[c]]"), "accaccacc")

    def test_ExampleThree(self):
        self.assertEqual(self.s.decodeString("2[abc]3[cd]ef"), "abcabccdcdcdef")


unittest.main()
