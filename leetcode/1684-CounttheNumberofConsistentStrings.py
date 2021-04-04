'''
1684. Count the Number of Consistent Strings

You are given a string allowed consisting of distinct characters and an array 
of strings words. A string is consistent if all characters in the string 
appear in the string allowed.

Return the number of consistent strings in the array words.

Example 1:
    Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
    Output: 2
    Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.

Example 2:
    Input: allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
    Output: 7
    Explanation: All strings are consistent.

Example 3:
    Input: allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
    Output: 4
    Explanation: Strings "cc", "acd", "ac", and "d" are consistent.

Constraints:
    1 <= words.length <= 10^4
    1 <= allowed.length <= 26
    1 <= words[i].length <= 10
    The characters in allowed are distinct.
    words[i] and allowed contain only lowercase English letters.
'''
# Runtime:       216 ms, faster than 89.78% of Python3 online submissions for Count the Number of Consistent Strings.
# Memory Usage: 16.1 MB, less than 43.20% of Python3 online submissions for Count the Number of Consistent Strings.

class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        
        # be optimistic!
        result = len(words)

        for word in words:
            for letter in word:
                if letter not in allowed:
                    result -= 1
                    break # out of letter

        return result


s = Solution()
print(s.countConsistentStrings("ab", ["ad","bd","aaab","baa","badab"]))
print(s.countConsistentStrings("abc", ["a","b","c","ab","ac","bc","abc"]))
print(s.countConsistentStrings("cad", ["cc","acd","b","ba","bac","bad","ac","d"]))


