"""
22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]
 

Constraints:
1 <= n <= 8
"""

# Runtime:        0 ms Your runtime beats 100.00 % of python3 submissions.
# Memory Usage: 16.81 MB Your memory usage beats 57.14 % of python3 submissions.

from typing import Counter, List
from itertools import product
from collections import defaultdict

from math import gcd


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def generate(left, right, s):
            if len(s) == n * 2:
                parenthesis.append(s)
                return

            if left < n:
                generate(left + 1, right, f"{s}(")

            if right < left:
                generate(left, right + 1, f"{s})")

        parenthesis = []
        generate(0, 0, "")
        return parenthesis



    def generateParenthesis_one(self, n: int) -> List[str]:
        
        result = []
        left = right = 0
        q = [(left, right, '')]

        while q:
            left, right, s = q.pop()
        
            if len(s) == 2 * n:
                result.append(s)
        
            if left < n:
                q.append((left + 1, right, f'{s}('))
        
            if right < left:
                q.append((left, right + 1, f'{s})'))
        
        return result

import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_ExampleOne(self):
        self.assertEqual(self.s.generateParenthesis(3), ["((()))", "(()())", "(())()", "()(())", "()()()"])

    def test_ExampleTwo(self):
        self.assertEqual(self.s.generateParenthesis(1), ["()"])


unittest.main()
