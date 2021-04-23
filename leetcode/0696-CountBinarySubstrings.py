'''
696. Count Binary Substrings

Give a string s, count the number of non-empty (contiguous) substrings that have the same number of 0's and 1's, 
and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

Example 1:
    Input: "00110011"
    Output: 6
    Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: 
        "0011", "01", "1100", "10", "0011", and "01".

    Notice that some of these substrings repeat and are counted the number of times they occur.
    Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.

Example 2:
    Input: "10101"
    Output: 4
    Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.

Note:
    s.length will be between 1 and 50,000.
    s will only consist of "0" or "1" characters.
'''
# Runtime: 156 ms       Your runtime beats 80.94 % of python3 submissions.
# Memory Usage: 14.6 MB Your memory usage beats 42.93 % of python3 submissions.

class Solution:
    def countBinarySubstrings(self, s: str) -> int:

        # The digits need to be consecutive
        # we can count the groups and then compare the group counts
        # Example 1: 00111 is two 0 and three 1 => 2, 3
        #            the answer is min(2,3) => 2 [01 and 0011]
        # Example 2: 001110011 is two 0; three 1; two 0, two 1 or 
        #                              2,3,2,2
        #            the answer is min(2,3) 
        #                         + min (3,2) 
        #                           + min (2,2) => 6

        result = 0
        current_count = 1
        previous_count = 0
        
        for i in range(1, len(s)):
            # same digit?
            if s[i] == s[i-1]: 
                current_count += 1
            else:
                result += min(current_count, previous_count)
                previous_count, current_count = current_count, 1

        # we need to add the last group
        return result + min(current_count, previous_count)



s = Solution()
print(s.countBinarySubstrings("00110011"))
print(s.countBinarySubstrings("10101"))
