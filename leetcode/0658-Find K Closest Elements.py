"""
658. Find K Closest Elements

Given a sorted integer array arr, two integers k and x, return the k closest integers 
to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
 

Example 1:
Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]

Example 2:
Input: arr = [1,1,2,3,4,5], k = 4, x = -1
Output: [1,1,2,3]

Constraints:
1 <= k <= arr.length
1 <= arr.length <= 104
arr is sorted in ascending order.
-104 <= arr[i], x <= 104
"""

# Runtime:          0 ms Your runtime beats 100 % of python3 submissions.
# Memory Usage: 17.76 MB Your memory usage beats 98.51 % of python3 submissions.

from typing import List
from itertools import product, combinations, permutations
from collections import namedtuple
import math


class Solution:

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        if len(arr) == k:
            return arr

        # lowest and highest possible starting points
        lowest_start = 0
        highest_start = len(arr) - k

        # work them towards each other (binary search)
        while lowest_start < highest_start:

            mid = lowest_start + (highest_start - lowest_start) // 2

            if x <= arr[mid]:
                highest_start = mid

            elif arr[mid + k] <= x:
                lowest_start = mid + 1

            else:
                middist = abs(x - arr[mid])
                midkdist = abs(x - arr[mid + k])

                if middist <= midkdist:
                    highest_start = mid

                else:
                    lowest_start = mid + 1

        return arr[lowest_start : lowest_start + k]


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
        self.assertEqual(self.s.findClosestElements([1, 2, 3, 4, 5], k=4, x=3), [1, 2, 3, 4])

    def test_ExampleTwo(self):
        self.assertEqual(self.s.findClosestElements([1, 1, 2, 3, 4, 5], k=4, x=-1), [1, 1, 2, 3])

    def test_ExampleThree(self):
        self.assertEqual(self.s.findClosestElements([-2, -1, 1, 2, 3, 4, 5], k=7, x=3), [-2, -1, 1, 2, 3, 4, 5])

    def test_ExampleFour(self):
        self.assertEqual(self.s.findClosestElements([-2, -1, 1, 2, 3, 4, 5], k=2, x=3), [2, 3])


unittest.main()
