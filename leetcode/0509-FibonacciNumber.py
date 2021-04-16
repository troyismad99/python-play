'''
509. Fibonacci Number

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the 
Fibonacci sequence, such that each number is the sum of the two 
preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.

Given n, calculate F(n).

Example 1:
    Input: n = 2
    Output: 1
    Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

Example 2:
    Input: n = 3
    Output: 2
    Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

Example 3:
    Input: n = 4
    Output: 3
    Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.

Constraints:
    0 <= n <= 30
'''
# Runtime: 32 ms        Your runtime beats 60.41 % of python3 submissions.
# Memory Usage: 14.1 MB Your memory usage beats 89.45 % of python3 submissions.

class Solution:

    # Fibonacci is a classic dynamic programming example
    # With just a recursive solution you end up repeatedly calculating the same 
    # values.
    # To avoid that we use memoization to 'cache' previously calculated values. 

    def __init__(self):
        self.memo = {}

    def fib(self, n: int) -> int:
        
        if n == 0: 
            return 0

        if n == 1: 
            return 1

        if n not in self.memo:
            self.memo[n] = self.fib(n-1) + self.fib(n-2)
            
        return self.memo[n]

s = Solution()
print(s.fib(2))
print(s.fib(3))
print(s.fib(4))

print(s.fib(5))
print(s.fib(6))
print(s.fib(7))
print(s.fib(8))
print(s.fib(9))
print(s.fib(10))