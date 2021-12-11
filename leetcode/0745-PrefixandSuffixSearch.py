'''
745. Prefix and Suffix Search

Design a special dictionary which has some words and allows you to 
search the words in it by a prefix and a suffix.

Implement the WordFilter class:
    WordFilter(string[] words) Initializes the object with the words in the dictionary.
    f(string prefix, string suffix) Returns the index of the word in the dictionary 
    which has the prefix 'prefix' and the suffix 'suffix'. 
    If there is more than one valid index, return the largest of them. 
    If there is no such word in the dictionary, return -1.

Example 1:
    Input
    ["WordFilter", "f"]
    [[["apple"]], ["a", "e"]]
    Output
    [null, 0]

    Explanation
    WordFilter wordFilter = new WordFilter(["apple"]);
    wordFilter.f("a", "e"); // return 0, because the word at index 0 has prefix = "a" and suffix = 'e".

Constraints:
    1 <= words.length <= 15000
    1 <= words[i].length <= 10
    1 <= prefix.length, suffix.length <= 10
    words[i], prefix and suffix consist of lower-case English letters only.
    At most 15000 calls will be made to the function f.


'''
# Runtime: 2468 ms
# Memory Usage: 26.3 MB

class WordFilter:

    def __init__(self, words: list[str]):
        
        # format a string that we can search with this format: "suffix+prefix"
        # each word will saved in a new list

        # the new list
        self.word_cache = []        
        for word in reversed(words): 
            self.word_cache.append(word + '=' + word) 

        # we just need a string to search
        self.word_cache = ' '.join(self.word_cache)
        

    def f(self, prefix: str, suffix: str) -> int:
        # search for our suffix+prefix and count the number of =
        return self.word_cache.count('=', self.word_cache.find(suffix + '=' + prefix)) - 1

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)


obj = WordFilter(["apple"])
print(obj.f("a","e"))

obj = WordFilter(["orange","apple"])
print(obj.f("a","e"))

obj = WordFilter(["orange","apple"])
print(obj.f("f","f"))