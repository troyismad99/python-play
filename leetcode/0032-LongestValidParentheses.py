'''
32. Longest Valid Parentheses

Given a string containing just the characters '(' and ')', 
find the length of the longest valid (well-formed) parentheses substring.

Example 1:
    Input: s = "(()"
    Output: 2
    Explanation: The longest valid parentheses substring is "()".

Example 2:
    Input: s = ")()())"
    Output: 4
    Explanation: The longest valid parentheses substring is "()()".

Example 3:
    Input: s = ""
    Output: 0

Constraints:
    0 <= s.length <= 3 * 10^4
    s[i] is '(', or ')'.
'''
# Runtime: 36 ms        Your runtime beats 96.68 % of python3 submissions.
# Memory Usage: 14.8 MB Your memory usage beats 24.73 % of python3 submissions.

class Solution:
    def longestValidParentheses(self, s: str) -> int:

        # guard against empty string
        if not s:
            return 0

        dp = [0] * (len(s) + 1)
        stack = []

        # scan the string
        for i in range(len(s)):
            if s[i] == '(':
                # toss the index of an open on the stack
                stack.append(i)
            elif stack:
                # remove index of the corresponding open                
                j = stack.pop()
                # longest parentheses for this i
                dp[i+1] = dp[j] + i - j + 1

        return max(dp)


s = Solution()
print(s.longestValidParentheses("(()"))
print(s.longestValidParentheses(")()())"))
print(s.longestValidParentheses(""))
print(s.longestValidParentheses("(((()))"))

