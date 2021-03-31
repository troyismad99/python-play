'''
771. Jewels and Stones

You're given strings jewels representing the types of stones that are 
jewels, and stones representing the stones you have. Each character in 
stones is a type of stone you have. You want to know how many of the 
stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:
    Input: jewels = "aA", stones = "aAAbbbb"
    Output: 3

Example 2:
    Input: jewels = "z", stones = "ZZ"
    Output: 0

Constraints:
    1 <= jewels.length, stones.length <= 50
    jewels and stones consist of only English letters.
    All the characters of jewels are unique.
'''

# Runtime: 32 ms,      faster than 56.81% of Python3 online submissions for Jewels and Stones.
# Memory Usage: 14.2 MB, less than 46.74% of Python3 online submissions for Jewels and Stones.

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        result = 0

        for i in jewels:
            result += stones.count(i)

        return result


# examples
s = Solution()
print(s.numJewelsInStones("aA", "aAAbbbb"))
print(s.numJewelsInStones("z", "ZZ"))
