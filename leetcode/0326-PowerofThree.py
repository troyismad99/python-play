'''
326. Power of Three

Given an integer n, return true if it is a power of three. Otherwise, return false.
An integer n is a power of three, if there exists an integer x such that n == 3x.

Example 1:
    Input: n = 27
    Output: true

Example 2:
    Input: n = 0
    Output: false

Example 3:
    Input: n = 9
    Output: true

Example 4:
    Input: n = 45
    Output: false

Constraints:
    -2^31 <= n <= 2^31 - 1

'''
# Runtime: 64 ms        Your runtime beats 93.29 % of python3 submissions.
# Memory Usage: 14.2 MB Your memory usage beats 47.06 % of python3 submissions.

# thought about just hardcoding in these values for a quick lookup solution
# but i think they wanted something more
i = 1
r = []
while i < pow(2, 31):
    i *= 3
    r.append(i)
print(r)

class Solution:
    def isPowerOfThree(self, n: int) -> bool:

        # return n in [3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049, 177147, 531441, 1594323, 4782969, 14348907, 43046721, 129140163, 387420489, 1162261467, 3486784401]

        while n % 3 == 0 and n != 0:
            n /= 3
        
        if n == 1: 
            return True

        return False



import unittest

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_ExampleOne(self):
        self.assertTrue(self.s.isPowerOfThree(27))

    def test_ExampleTwo(self):
        self.assertFalse(self.s.isPowerOfThree(0))

    def test_ExampleThree(self):
        self.assertTrue(self.s.isPowerOfThree(9))

    def test_ExampleFour(self):
        self.assertFalse(self.s.isPowerOfThree(45))

unittest.main()

i = 1

while i < pow(2, 31):
    i *= 3
    print(i)

