"""
443. String Compression
Given an array of characters chars, compress it using the following algorithm:
Begin with an empty string s. For each group of consecutive repeating characters in chars:
- If the group's length is 1, append the character to s.
 -Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, 
be stored in the input character array chars. 
Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.

Example 1:
Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".

Example 2:
Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.

Example 3:
Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".

Constraints:
1 <= chars.length <= 2000
chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.
"""

# Runtime:          2 ms       our runtime beats 50.51 % of python3 submissions.
# Memory Usage: 16.86 MB Your memory usage beats  5.60 % of python3 submissions.

from itertools import groupby
from collections import namedtuple
from typing import List, Counter

import math


class Solution:

    def compress(self, chars: List[str]) -> int:

        s = []

        for key, group in groupby(chars):
            count = sum(1 for _ in group)
            s.append(key)

            if count > 1:
                s.extend(str(count))

        chars[:] = s

        return len(chars)


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_ExampleOne(self):
        self.assertEqual(self.s.compress(["a", "a", "b", "b", "c", "c", "c"]), 6)

    def test_ExampleTwo(self):
        self.assertEqual(self.s.compress(["a"]), 1)

    def test_ExampleThree(self):
        self.assertEqual(self.s.compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]), 4)


unittest.main()
