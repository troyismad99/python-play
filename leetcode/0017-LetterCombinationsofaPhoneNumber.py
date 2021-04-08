'''
17. Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible 
letter combinations that the number could represent. 
Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. 
Note that 1 does not map to any letters.



Example 1:
    Input: digits = "23"
    Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
    Input: digits = ""
    Output: []

Example 3:
    Input: digits = "2"
    Output: ["a","b","c"]

Constraints:
    0 <= digits.length <= 4
    digits[i] is a digit in the range ['2', '9'].
'''
# Runtime: 32 ms        Your runtime beats 54.35 % of python3 submissions.
# Memory Usage: 14.4 MB Your memory usage beats 33.21 % of python3 submissions.

from itertools import product 

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        
        # dictionary of the numbers and their letters
        letter_map = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
                      "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        if len(digits) == 0:
            return []

        if len(digits) == 1:
            return list(letter_map[digits[0]])

        # list of the letter_map items we care about
        l = [letter_map[i] for i in digits]

        # itertools.product => Cartesian product of input iterables.
        return (list(map(''.join,(product(*l)))))


s = Solution()

print(s.letterCombinations("23"))
print(s.letterCombinations(""))
print(s.letterCombinations("2"))
