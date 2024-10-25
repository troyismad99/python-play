"""
227. Basic Calculator II

Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid. 
All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, 
such as eval().

 

Example 1:

Input: s = "3+2*2"
Output: 7
Example 2:

Input: s = " 3/2 "
Output: 1
Example 3:

Input: s = " 3+5 / 2 "
Output: 5
 

Constraints:

1 <= s.length <= 3 * 105
s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
s represents a valid expression.
All the integers in the expression are non-negative integers in the range [0, 231 - 1].
The answer is guaranteed to fit in a 32-bit integer.
"""

# Runtime: 41 ms         Your runtime beats 99.75% of python3 submissions.
# Memory Usage: 21.02 MB Your memory usage beats 16.28% of python3 submissions.

from itertools import product
from collections import namedtuple
from typing import List


class Solution:
    def calculate(self, s: str) -> int:

        # Remove any spaces in the string
        s = s.replace(" ", "")

        stack = []

        current_number = 0
        operation = "+"

        # Add a '+' to handle the last number
        for char in f"{s}+":

            if char.isdigit():
                current_number = current_number * 10 + int(char)

            else:
                if operation == "*":
                    stack[-1] *= current_number

                elif operation == "+":
                    stack.append(current_number)

                elif operation == "-":
                    stack.append(-current_number)

                elif operation == "/":
                    # Perform integer division (truncated towards zero)
                    stack[-1] = int(stack[-1] / current_number)

                # Update operation and reset current number
                operation = char
                current_number = 0

        return sum(stack)


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_ExampleOne(self):
        self.assertEqual(self.s.calculate("3+2*2"), 7)

    def test_ExampleTwo(self):
        self.assertEqual(self.s.calculate(" 3/2 "), 1)

    def test_ExampleThree(self):
        self.assertEqual(self.s.calculate(" 3+5 / 2 "), 5)

    def test_ExampleFour(self):
        self.assertEqual(self.s.calculate(" 33+5 * 2 "), 43)

    def test_ExampleFive(self):
        self.assertEqual(self.s.calculate("14-3/2"), 13)


unittest.main()
