'''
209. Remove All Adjacent Duplicates in String II

Given a string s, a k duplicate removal consists of choosing k adjacent and equal letters 
from s and removing them causing the left and the right side of the 
deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made.

It is guaranteed that the answer is unique.

Example 1:
    Input: s = "abcd", k = 2
    Output: "abcd"
    Explanation: There's nothing to delete.

Example 2:
    Input: s = "deeedbbcccbdaa", k = 3
    Output: "aa"
    Explanation: 
        First delete "eee" and "ccc", get "ddbbbdaa"
        Then delete "bbb", get "dddaa"
        Finally delete "ddd", get "aa"

Example 3:
    Input: s = "pbbcggttciiippooaais", k = 2
    Output: "ps"

Constraints:
    1 <= s.length <= 10^5
    2 <= k <= 10^4
    s only contains lower case English letters.
'''
# Runtime: 68 ms        Your runtime beats 84.67 % of python3 submissions.
# Memory Usage: 15.9 MB Your memory usage beats 17.88 % of python3 submissions.

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        '''
        A stack solution
        Add the letters to the stack in order, but:
        do not add if the a duplicate of the previous, instead increment the counter
        If the counter equals k, remove that letter
        '''

        # dummy element for the first item
        # the 0 removes it from the results later
        stack = [['dummy', 0]]

        for c in s:
            # is this char the same as the last?
            if stack[-1][0] == c:
                stack[-1][1] += 1
                # same and we have reached k count
                if stack[-1][1] == k:
                    stack.pop() # toss it away
            else:
                stack.append([c,1])

        # expand the chars by the count
        return ''.join(c*k for c,k in stack)

s = Solution()
print(s.removeDuplicates("abcd", 2))
print(s.removeDuplicates("deeedbbcccbdaa", 3))
print(s.removeDuplicates("pbbcggttciiippooaais", 2))

