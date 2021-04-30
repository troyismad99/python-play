'''
970. Powerful Integers

Given three integers x, y, and bound, return a list of all the powerful integers that have a value less than or equal to bound.

An integer is powerful if it can be represented as x^i + y^j for some integers i >= 0 and j >= 0.

You may return the answer in any order. In your answer, each value should occur at most once.

Example 1:
    Input: x = 2, y = 3, bound = 10
    Output: [2,3,4,5,7,9,10]
    Explanation:
    2 = 2^0 + 3^0
    3 = 2^1 + 3^0
    4 = 2^0 + 3^1
    5 = 2^1 + 3^1
    7 = 2^2 + 3^1
    9 = 2^3 + 3^0
    10 = 2^0 + 3^2

Example 2:
    Input: x = 3, y = 5, bound = 15
    Output: [2,4,6,8,10,14]

Constraints:
    1 <= x, y <= 100
    0 <= bound <= 10^6
'''
# Runtime: 28 ms        Your runtime beats 87.70 % of python3 submissions.
# Memory Usage: 14.3 MB 

n = 10
while pow(2, n) < pow(10,6):
    n += 1
print(n)

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> list[int]:

        # we can brute force this one.
        # bound is constrained 10^6
        # 10^6 = 1000000
        # 2^20 = 1048576
        # we only need to calculate 20 results (0 to 19) for each set

        xset = {x**i for i in range(20) if x**i < bound}
        yset = {y**i for i in range(20) if y**i < bound}

        # merge the lists
        return list({i + ii for i in xset for ii in yset if i + ii <= bound})

s = Solution()

print(s.powerfulIntegers(2,3,10))
print(s.powerfulIntegers(3,5,15))

print(s.powerfulIntegers(1,3,10))
print(s.powerfulIntegers(3,5,0))



