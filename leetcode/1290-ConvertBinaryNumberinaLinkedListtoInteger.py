'''
1290. Convert Binary Number in a Linked List to Integer

Given head which is a reference node to a singly-linked list. 
The value of each node in the linked list is either 0 or 1. 
The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

Example 1:
    Input: head = [1,0,1]
    Output: 5
    Explanation: (101) in base 2 = (5) in base 10

Example 2:
    Input: head = [0]
    Output: 0

Example 3:
    Input: head = [1]
    Output: 1

Example 4:
    Input: head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
    Output: 18880

Example 5:
    Input: head = [0,0]
    Output: 0

Constraints:
    The Linked List is not empty.
    Number of nodes will not exceed 30.
    Each node's value is either 0 or 1.
'''
# Runtime:      32 ms, faster than 55.97% of Python3 online submissions for Convert Binary Number in a Linked List to Integer.
# Memory Usage: 14.1 MB, less than 88.21% of Python3 online submissions for Convert Binary Number in a Linked List to Integer.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        result = 0

        while head:
            result *= 2 
            result += head.val
            head = head.next
        
        return result


s = Solution()

e = ListNode(1)
e.next = ListNode(0)
e.next.next = ListNode(1)
print(s.getDecimalValue(e))

e2 = ListNode(0)
print(s.getDecimalValue(e2))

e3 = ListNode(1)
print(s.getDecimalValue(e3))

e5 = ListNode(0)
e5.next = ListNode(0)
print(s.getDecimalValue(e5))

a = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
e4 = ListNode(a[0])
tail = e4
i = 1
while i < len(a):
    tail.next = ListNode(a[i])
    tail = tail.next
    i += 1

print(s.getDecimalValue(e4))
