'''
953. Verifying an Alien Dictionary

In an alien language, surprisingly they also use english lowercase letters, 
but possibly in a different order. The order of the alphabet is some 
permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order 
of the alphabet, return true if and only if the given words are sorted 
lexicographically in this alien language.

Example 1:
    Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
    Output: true
    Explanation: As 'h' comes before 'l' in this language, then the sequence 
                 is sorted.

Example 2:
    Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
    Output: false
    Explanation: As 'd' comes after 'l' in this language, 
                 then words[0] > words[1], hence the sequence is unsorted.

Example 3:
    Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
    Output: false
    Explanation: The first three characters "app" match, and the second string 
                 is shorter (in size.) 
                 According to lexicographical rules "apple" > "app", 
                 because 'l' > '∅', where '∅' is defined as the blank 
                 character which is less than any other character.

Constraints:
    1 <= words.length <= 100
    1 <= words[i].length <= 20
    order.length == 26
    All characters in words[i] and order are English lowercase letters.
'''
# Runtime: 36 ms        Your runtime beats 61.36 % of python3 submissions.
# Memory Usage: 14.2 MB Your memory usage beats 91.50 % of python3 submissions.

class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        
        # create and populate an alien dictionary
        alien_dictionary = {}

        for index, val in enumerate(order):
            alien_dictionary[val] = index

        # going to check each word against the next word
        for i in range(len(words) - 1):

            # and then each letter in the word
            for j in range(len(words[i])):

                # next word is shorter, (but has the same letters to here)
                if j >= len(words[i + 1]):
                    return False

                # if the letters are not the same...
                if words[i][j] != words[i + 1][j]:

                    # ... wrong order
                    if alien_dictionary[words[i][j]] > alien_dictionary[words[i + 1][j]]:
                        return False

                    # ... proper order, move to next set of words
                    break

        return True


s = Solution()
print(s.isAlienSorted(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))
print(s.isAlienSorted(["word","world","row"], "worldabcefghijkmnpqstuvxyz"))
print(s.isAlienSorted(["apple", "app"], "abcdefghijklmnopqrstuvwxyz"))
