"""
1768. Merge Strings Alternately

You are given two strings word1 and word2. Merge the strings by adding letters 
in alternating order, starting with word1. If a string is longer than the other, 
append the additional letters onto the end of the merged string.

Return the merged string.

Example 1:
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

Example 2:
Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s

Example 3:
Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
 
Constraints:
1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.
"""

# Runtime:         35 ms Your runtime beats 54.29 % of python3 submissions.
# Memory Usage: 16.41 MB Your memory usage beats 81.77 % of python3 submissions.

from typing import List
from itertools import product, combinations, permutations
from collections import namedtuple
import math


class Solution:

    def mergeAlternately(self, word1: str, word2: str) -> str:

        answer = []

        for i in range(min(len(word1), len(word2))):
            answer.append(word1[i] + word2[i])

        return "".join(answer) + word1[i + 1 :] + word2[i + 1 :]


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
        self.assertEqual(self.s.mergeAlternately(word1="abc", word2="pqr"), "apbqcr")

    def test_ExampleTwo(self):
        self.assertEqual(self.s.mergeAlternately("ab", "pqrs"), "apbqrs")

    def test_ExampleThree(self):
        self.assertEqual(self.s.mergeAlternately("abcd", "pq"), "apbqcd")


unittest.main()
