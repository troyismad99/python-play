"""
399. Evaluate Division

You are given an array of variable pairs equations and an array of real numbers values, 
where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. 
Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the 
jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. 
If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division 
by zero and that there is no contradiction.

Note: The variables that do not occur in the list of equations are undefined, 
so the answer cannot be determined for them.

Example 1:
Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? 
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
note: x is undefined => -1.0

Example 2:
Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]

Example 3:
Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]
 

Constraints:
1 <= equations.length <= 20
equations[i].length == 2
1 <= Ai.length, Bi.length <= 5
values.length == equations.length
0.0 < values[i] <= 20.0
1 <= queries.length <= 20
queries[i].length == 2
1 <= Cj.length, Dj.length <= 5
Ai, Bi, Cj, Dj consist of lower case English letters and digits.
"""

# Runtime:         xx ms      your runtime beats xxxxx % of python3 submissions.
# Memory Usage: xxxxx MB Your memory usage beats xxxxx % of python3 submissions.

from itertools import product, permutations, combinations, zip_longest
from collections import namedtuple, defaultdict
from typing import List, Counter

import math


class Solution:

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        # see: https://algo.monster/liteproblems/399

        # This function finds the root of the set to which 'x' belongs
        # It uses path compression to make subsequent lookups faster
        def find(x):
            if parent[x] != x:
                original_parent = parent[x]
                parent[x] = find(parent[x])  # Recursively find the root parent
                weight[x] *= weight[original_parent]  # Adjust the weight

            return parent[x]

        # Initialize default dictionary for weights and parents
        weight = defaultdict(lambda: 1.0)
        parent = defaultdict(str)

        # Set initial parent of each variable to itself
        for a, b in equations:
            parent[a], parent[b] = a, b

        # Process each equation and union the groups setting the parent relationship and weight
        for i, value in enumerate(values):
            a, b = equations[i]
            root_a, root_b = find(a), find(b)

            if root_a != root_b:  # If 'a' and 'b' have different roots, union them
                parent[root_a] = root_b
                weight[root_a] = weight[b] * value / weight[a]

        # Process each query
        results = []

        for c, d in queries:

            # If either variable is unknown, or they belong to different sets, the result is -1
            if c not in parent or d not in parent or find(c) != find(d):
                results.append(-1.0)
            else:
                # If they belong to the same set, calculate the result based on weights
                results.append(weight[c] / weight[d])

        return results


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_ExampleOne(self):
        self.assertEqual(
            self.s.calcEquation(
                equations=[["a", "b"], ["b", "c"]],
                values=[2.0, 3.0],
                queries=[["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]],
            ),
            [6.00000, 0.50000, -1.00000, 1.00000, -1.00000],
        )

    def test_ExampleTwo(self):
        self.assertEqual(
            self.s.calcEquation(
                equations=[["a", "b"], ["b", "c"], ["bc", "cd"]],
                values=[1.5, 2.5, 5.0],
                queries=[["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]],
            ),
            [3.75000, 0.40000, 5.00000, 0.20000],
        )

    def test_ExampleThree(self):
        self.assertEqual(
            self.s.calcEquation(
                equations=[["a", "b"]], values=[0.5], queries=[["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]
            ),
            [0.50000, 2.00000, -1.00000, -1.00000],
        )


# self.assertFalse(function_name(123))
# self.assertTrue(function_name(123))
# self.assertIn(self.s.function_name(123), [1, 2])
# self.assertTrue(self.compare_lists(self.s.function_name([2, 5, 2, 1, 2], 5), [[1, 2, 2], [5]]))

unittest.main()
