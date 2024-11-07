"""
2390. Removing Stars From a String

You are given a string s, which contains stars *.

In one operation, you can:

Choose a star in s.
Remove the closest non-star character to its left, as well as remove the star itself.
Return the string after all stars have been removed.

Note:

The input will be generated such that the operation is always possible.
It can be shown that the resulting string will always be unique.

Example 1:
Input: s = "leet**cod*e"
Output: "lecoe"
Explanation: Performing the removals from left to right:
- The closest character to the 1st star is 't' in "leet**cod*e". s becomes "lee*cod*e".
- The closest character to the 2nd star is 'e' in "lee*cod*e". s becomes "lecod*e".
- The closest character to the 3rd star is 'd' in "lecod*e". s becomes "lecoe".
There are no more stars, so we return "lecoe".

Example 2:
Input: s = "erase*****"
Output: ""
Explanation: The entire string is removed, so we return an empty string.

Constraints:
1 <= s.length <= 10^5
s consists of lowercase English letters and stars *.
The operation above can be performed on s.
"""

# Runtime:         84 ms      your runtime beats 73.21 % of python3 submissions.
# Memory Usage: 17.91 MB Your memory usage beats 71.83 % of python3 submissions.

from itertools import product, permutations, combinations, zip_longest
from collections import namedtuple
from typing import List, Counter

import math


class Solution:

    def removeStars(self, s: str) -> str:

        new_word_stack = []

        for c in s:
            if c == "*":
                new_word_stack.pop()
            else:
                new_word_stack.append(c)

        return "".join(new_word_stack)


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_ExampleOne(self):
        self.assertEqual(self.s.removeStars("leet**cod*e"), "lecoe")

    def test_ExampleTwo(self):
        self.assertEqual(self.s.removeStars("erase*****"), "")


unittest.main()
