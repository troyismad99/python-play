'''
1486. XOR Operation in an Array

Given an integer n and an integer start.

Define an array nums where 
        nums[i] = start + 2*i (0-indexed) 
    and n == nums.length.

Return the bitwise XOR of all elements of nums.

Example 1:
    Input: n = 5, start = 0
    Output: 8
    Explanation: Array nums is equal to [0, 2, 4, 6, 8] where (0 ^ 2 ^ 4 ^ 6 ^ 8) = 8.
    Where "^" corresponds to bitwise XOR operator.

Example 2:
    Input: n = 4, start = 3
    Output: 8
    Explanation: Array nums is equal to [3, 5, 7, 9] where (3 ^ 5 ^ 7 ^ 9) = 8.

Example 3:
    Input: n = 1, start = 7
    Output: 7

Example 4:
    Input: n = 10, start = 5
    Output: 2

Constraints:
    1 <= n <= 1000
    0 <= start <= 1000
    n == nums.length
'''
# Runtime: 32 ms,      faster than 57.40% of Python3 online submissions for XOR Operation in an Array.
# Memory Usage: 14.3 MB, less than 21.23% of Python3 online submissions for XOR Operation in an Array.

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        
        # don't need nums since XOR is commutative
        # we can calculate the result as we go

        result = start

        for i in range(1, n):
            result = result ^ (start + (2 * i))

        return result


s = Solution()
print(s.xorOperation(5, 0))
print(s.xorOperation(4, 3))
print(s.xorOperation(1, 7))
print(s.xorOperation(10, 5))

