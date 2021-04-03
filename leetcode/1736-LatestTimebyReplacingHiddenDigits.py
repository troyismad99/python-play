'''
1736. Latest Time by Replacing Hidden Digits

You are given a string time in the form of hh:mm, where some of the 
digits in the string are hidden (represented by ?).

The valid times are those inclusively between 00:00 and 23:59.

Return the latest valid time you can get from time by replacing the hidden digits.

Example 1:
    Input: time = "2?:?0"
    Output: "23:50"
    Explanation: The latest hour beginning with the digit '2' is 23 and the latest minute ending with the digit '0' is 50.

Example 2:
    Input: time = "0?:3?"
    Output: "09:39"

Example 3:
    Input: time = "1?:22"
    Output: "19:22"
 
Constraints:
    time is in the format hh:mm.
    It is guaranteed that you can produce a valid time from the given string.
'''
# Runtime: 32 ms,      faster than 57.11% of Python3 online submissions for Latest Time by Replacing Hidden Digits.
# Memory Usage: 14.1 MB, less than 78.34% of Python3 online submissions for Latest Time by Replacing Hidden Digits.

class Solution:
    def maximumTime(self, time: str) -> str:

        time = list(time)

        for i in range(len(time)):

            # do we care about replacing this digit?
            if time[i] == '?':

                # first hour digit depends on second hour digit
                if   i == 0: time[i] = "2" if time[i+1] in "?0123" else "1"

                # second hour depends on first
                elif i == 1: time[i] = "3" if time[0] == "2"       else "9"

                # max minutes is always 59
                elif i == 3: time[i] = "5"
                else: time[i] = "9"

        return "".join(time)

s = Solution()

print(s.maximumTime("2?:?0"))
print(s.maximumTime("0?:3?"))
print(s.maximumTime("1?:22"))

