'''
1662. Check If Two String Arrays are Equivalent

Given two string arrays word1 and word2, return true if the two arrays 
represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated
in order forms the string.

Example 1:
    Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
    Output: true
    Explanation:
    word1 represents string "ab" + "c" -> "abc"
    word2 represents string "a" + "bc" -> "abc"
    The strings are the same, so return true.

Example 2:
    Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
    Output: false

Example 3:
    Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
    Output: true

Constraints:
    1 <= word1.length, word2.length <= 103
    1 <= word1[i].length, word2[i].length <= 103
    1 <= sum(word1[i].length), sum(word2[i].length) <= 103
    word1[i] and word2[i] consist of lowercase letters.
'''
# Runtime: 32 ms, faster than 61.12% of Python3 online submissions for Check If Two String Arrays are Equivalent.
# Memory Usage: 14.2 MB, less than 86.06% of Python3 online submissions for Check If Two String Arrays are Equivalent.

class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:

        return ''.join(word1) == ''.join(word2)

s = Solution()
print(s.arrayStringsAreEqual(["ab", "c"],["a", "bc"]))
print(s.arrayStringsAreEqual(["a", "cb"],["ab", "b"]))
print(s.arrayStringsAreEqual(["abc", "d", "defg"],["abcddefg"]))


