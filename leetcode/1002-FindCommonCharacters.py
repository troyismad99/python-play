'''
1002. Find Common Characters

Given an array A of strings made only from lowercase letters, 
return a list of all characters that show up in all strings within the list (including duplicates).

For example, if a character occurs 3 times in all strings but not 4 times, 
you need to include that character three times in the final answer.

You may return the answer in any order.

Example 1:
    Input: ["bella","label","roller"]
    Output: ["e","l","l"]

Example 2:
    Input: ["cool","lock","cook"]
    Output: ["c","o"]

Note:
    1 <= A.length <= 100
    1 <= A[i].length <= 100
    A[i][j] is a lowercase letter
'''
# Runtime: 44 ms, faster than 82.40% of Python3 online submissions for Find Common Characters.
# Memory Usage: 14.2 MB, less than 95.21% of Python3 online submissions for Find Common Characters.

import collections

class Solution:
    def commonChars(self, A: list[str]) -> list[str]:
        
        # start with the first string
        result = collections.Counter(A[0])

        for a in A:
            # bitwise AND performs an intersect of the two dictionaries
            # lowest count of common elements will be preserved
            result &= collections.Counter(a)

        return list(result.elements())

s = Solution()

print(s.commonChars(["bella","label","roller"]))
print(s.commonChars(["cool","lock","cook"]))
