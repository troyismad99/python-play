'''
1281. Subtract the Product and Sum of Digits of an Integer

Given an integer number n, return the difference between:
    the product of its digits and 
    the sum of its digits.
 
Example 1:
Input: n = 234
    Output: 15 
    Explanation: 
    Product of digits = 2 * 3 * 4 = 24 
    Sum of digits = 2 + 3 + 4 = 9 
    Result = 24 - 9 = 15

Example 2:
    Input: n = 4421
    Output: 21
    Explanation: 
    Product of digits = 4 * 4 * 2 * 1 = 32 
    Sum of digits = 4 + 4 + 2 + 1 = 11 
    Result = 32 - 11 = 21
 
Constraints:
    1 <= n <= 10^5
'''
# Runtime: 28 ms,      faster than 79.23% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.
# Memory Usage: 14.2 MB, less than 70.67% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        digitsum  = 0
        digitprod = 1

        while n:

            # discovered divmod that does both the % and //
            n, digit = divmod(n, 10)
            digitsum  += digit
            digitprod *= digit
        
        return digitprod - digitsum


# examples
s = Solution()
print(s.subtractProductAndSum(234))
print(s.subtractProductAndSum(4421))
