'''
9. Palindrome Number
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. 
For example, 121 is palindrome while 123 is not.

Example 1:
    Input: x = 121
    Output: true

Example 2:
    Input: x = -121
    Output: false
    Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
    Input: x = 10
    Output: false
    Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Example 4:
    Input: x = -101
    Output: false

Constraints:
    -2^31 <= x <= 2^31 - 1
 
Follow up: Could you solve it without converting the integer to a string?
'''

# Runtime: 72 ms, faster than 30.56% of Python3 online submissions for Palindrome Number.
# Memory Usage: 14.4 MB, less than 17.15% of Python3 online submissions for Palindrome Number.

class Solution:
    def isPalindrome(self, x: int) -> bool:

        # negatives cannot be palindromes
        if x < 0:
            return False

        # reverse the int
        originalX = x
        reverseX = 0

        while x > 0:
            lastdigit = x % 10
            reverseX = reverseX * 10 + lastdigit
            x = x // 10

        return originalX == reverseX

# examples
s = Solution()
print(s.isPalindrome(121))
print(s.isPalindrome(-121))
print(s.isPalindrome(10))
print(s.isPalindrome(-101))
print(s.isPalindrome(99))
print(s.isPalindrome(2**31))
