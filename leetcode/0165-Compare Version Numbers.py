"""
165. Compare Version Numbers

Given two version strings, version1 and version2, compare them. A version string consists of 
revisions separated by dots '.'. The value of the revision is its integer conversion ignoring leading zeros.

To compare version strings, compare their revision values in left-to-right order. 
If one of the version strings has fewer revisions, treat the missing revision values as 0.

Return the following:
If version1 < version2, return -1.
If version1 > version2, return 1.
Otherwise, return 0.
 

Example 1:
Input: version1 = "1.2", version2 = "1.10"
Output: -1
Explanation:
version1's second revision is "2" and version2's second revision is "10": 2 < 10, so version1 < version2.

Example 2:
Input: version1 = "1.01", version2 = "1.001"
Output: 0
Explanation:
Ignoring leading zeroes, both "01" and "001" represent the same integer "1".

Example 3:
Input: version1 = "1.0", version2 = "1.0.0.0"
Output: 0
Explanation:
version1 has less revisions, which means every missing revision are treated as "0".

 

Constraints:
1 <= version1.length, version2.length <= 500
version1 and version2 only contain digits and '.'.
version1 and version2 are valid version numbers.
All the given revisions in version1 and version2 can be stored in a 32-bit integer.
"""

# Runtime:          0 ms        Your runtime beats 100% of python3 submissions.
# Memory Usage: 16.46 MB Your memory usage beats 84.95% of python3 submissions.

from itertools import product, zip_longest
from collections import namedtuple
from typing import List


class Solution:

    def compareVersion(self, version1: str, version2: str) -> int:

        v1 = [int(x) for x in version1.split(".")]
        v2 = [int(x) for x in version2.split(".")]

        for rev1, rev2 in zip_longest(v1, v2, fillvalue=0):
            if rev1 == rev2:
                continue

            return -1 if rev1 < rev2 else 1

        return 0


    def compareVersion_Lime(self, version1: str, version2: str) -> int:

        # Runtime:          4 ms      Your runtime beats  7.73% of python3 submissions.
        # Memory Usage: 16.69 MB Your memory usage beats 17.07% of python3 submissions.
        
        v1 = version1.split(".")
        v2 = version2.split(".")

        v1_len = len(v1)
        v2_len = len(v2)

        for i in range(max(v1_len, v2_len)):

            m1 = int(v1[i]) if i < v1_len else 0
            m2 = int(v2[i]) if i < v2_len else 0

            if m1 < m2:
                return -1
            elif m1 > m2:
                return 1

        return 0


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_ExampleZero(self):
        self.assertEqual(self.s.compareVersion("1.2", "1.10"), -1)

    def test_ExampleZero2(self):
        self.assertEqual(self.s.compareVersion("1.01", "1.001"), 0)

    def test_ExampleOne(self):
        self.assertEqual(self.s.compareVersion("1.0", "1.0.0.0"), 0)

    def test_ExampleTwo(self):
        self.assertEqual(self.s.compareVersion("1.1.1.1", "1.1"), 1)

    def test_ExampleThree(self):
        self.assertEqual(self.s.compareVersion("1.1", "1.1.1.1"), -1)


unittest.main()
