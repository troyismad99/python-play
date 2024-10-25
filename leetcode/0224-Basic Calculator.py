"""
224. Basic Calculator

Given a string s representing a valid expression, implement a basic calculator to 
evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings 
as mathematical expressions, such as eval().

 

Example 1:

Input: s = "1 + 1"
Output: 2
Example 2:

Input: s = " 2-1 + 2 "
Output: 3
Example 3:

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
 

Constraints:

1 <= s.length <= 3 * 105
s consists of digits, '+', '-', '(', ')', and ' '.
s represents a valid expression.
'+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
'-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
There will be no two consecutive operators in the input.
Every number and running calculation will fit in a signed 32-bit integer.
"""

# Runtime: 18 ms         Your runtime beats 99.53% of python3 submissions.
# Memory Usage: 17.40 MB Your memory usage beats 93.89% of python3 submissions.

from itertools import product
from collections import namedtuple
from typing import List


class Solution:
    def calculate(self, s: str) -> int:

        # Remove any spaces in the string
        s = s.replace(" ", "")

        stack = []

        current_number = 0
        current_total = 0
        sign = 1

        for char in s:

            if char.isdigit():
                current_number = current_number * 10 + int(char)

            elif char == "+":
                current_total += current_number * sign
                sign = 1
                current_number = 0

            elif char == "-":
                current_total += current_number * sign
                sign = -1
                current_number = 0

            elif char == "(":
                # save what we had
                stack.append((current_total, sign))

                # start over for open bracket
                current_total = 0
                sign = 1

            elif char == ")":
                current_total += sign * current_number
                previous_total, previous_sign = stack.pop()
                current_total = previous_total + current_total * previous_sign
                current_number = 0

        current_total += current_number * sign
        return current_total


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_ExampleZero(self):
        self.assertEqual(self.s.calculate("(1 + 1)"), 2)

    def test_ExampleZero2(self):
        self.assertEqual(self.s.calculate("-(1 + 1)"), -2)

    def test_ExampleOne(self):
        self.assertEqual(self.s.calculate("1 + 1"), 2)

    def test_ExampleTwo(self):
        self.assertEqual(self.s.calculate(" 2-1 + 2 "), 3)

    def test_ExampleThree(self):
        self.assertEqual(self.s.calculate("(1+(4+5+2)-3)+(6+8)"), 23)

unittest.main()
