'''
1221. Split a String in Balanced Strings

Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

Given a balanced string s, split it in the maximum amount of balanced strings.

Return the maximum amount of split balanced strings.

Example 1:
    Input: s = "RLRRLLRLRL"
    Output: 4
    Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.

Example 2:
    Input: s = "RLLLLRRRLR"
    Output: 3
    Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.

Example 3:
    Input: s = "LLLLRRRR"
    Output: 1
    Explanation: s can be split into "LLLLRRRR".

Example 4:
    Input: s = "RLRRRLLRLL"
    Output: 2
    Explanation: s can be split into "RL", "RRRLLRLL", since each substring contains an equal number of 'L' and 'R'

Constraints:
    1 <= s.length <= 1000
    s[i] is either 'L' or 'R'.
    s is a balanced string.
'''
# Runtime: 32 ms, faster than 57.71% of Python3 online submissions for Split a String in Balanced Strings.
# Memory Usage: 14.1 MB, less than 72.79% of Python3 online submissions for Split a String in Balanced Strings.

class Solution:
    def balancedStringSplit(self, s: str) -> int:

        result = 0
        counter = 0

        for char in s:
            if char == 'L':
                counter += 1
            if char == 'R':
                counter -= 1
            
            # 0 indicates an equal L and R count
            if counter == 0:
                result += 1

        return result

s = Solution()
print(s.balancedStringSplit("RLRRLLRLRL"))
print(s.balancedStringSplit("RLLLLRRRLR"))
print(s.balancedStringSplit("LLLLRRRR"))
print(s.balancedStringSplit("RLRRRLLRLL"))
