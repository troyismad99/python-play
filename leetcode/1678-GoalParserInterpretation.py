'''
1678. Goal Parser Interpretation

You own a Goal Parser that can interpret a string command. The command 
consists of an alphabet of "G", "()" and/or "(al)" in some order. 
The Goal Parser will interpret "G" as the string "G", "()" as the 
tring "o", and "(al)" as the string "al". 
The interpreted strings are then concatenated in the original order.

Given the string command, return the Goal Parser's interpretation of command.

Example 1:
    Input: command = "G()(al)"
    Output: "Goal"
    Explanation: The Goal Parser interprets the command as follows:
    G -> G
    () -> o
    (al) -> al
    The final concatenated result is "Goal".

Example 2:
    Input: command = "G()()()()(al)"
    Output: "Gooooal"

Example 3:
    Input: command = "(al)G(al)()()G"
    Output: "alGalooG"

Constraints:
    1 <= command.length <= 100
    command consists of "G", "()", and/or "(al)" in some order.
'''
# Runtime: 32 ms, faster than 52.45% of Python3 online submissions for Goal Parser Interpretation.
# Memory Usage: 14.1 MB, less than 69.96% of Python3 online submissions for Goal Parser Interpretation.

class Solution:
    def interpret(self, command: str) -> str:        
        return command.replace('()', 'o').replace('(al)', 'al')

# examples
s = Solution()
print(s.interpret("G()(al)"))
print(s.interpret("G()()()()(al)"))
print(s.interpret("(al)G(al)()()G"))

