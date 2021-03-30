'''
1108. Defanging an IP Address

Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

Example 1:
    Input: address = "1.1.1.1"
    Output: "1[.]1[.]1[.]1"

Example 2:
    Input: address = "255.100.50.0"
    Output: "255[.]100[.]50[.]0"

Constraints:
    The given address is a valid IPv4 address.
'''
# Runtime: 32 ms,      faster than 49.08% of Python3 online submissions for Defanging an IP Address.
# Memory Usage: 14.3 MB, less than 35.10% of Python3 online submissions for Defanging an IP Address.

class Solution:
    def defangIPaddr(self, address: str) -> str:        
        return address.replace('.', '[.]')

# examples
s = Solution()

print(s.defangIPaddr('1.1.1.1'))
print(s.defangIPaddr('255.100.50.0'))
print(s.defangIPaddr('192.168.1.90'))