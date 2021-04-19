'''
19. Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Follow up: Could you do this in one pass?

Example 1:
    Input: head = [1,2,3,4,5], n = 2
    Output: [1,2,3,5]

Example 2:
    Input: head = [1], n = 1
    Output: []

Example 3:
    Input: head = [1,2], n = 1
    Output: [1]
 
Constraints:
    The number of nodes in the list is sz.
    1 <= sz <= 30
    0 <= Node.val <= 100
    1 <= n <= sz
'''
# Runtime: 36 ms      Your runtime beats 43.74 % of python3 submissions.
# Memory Usage: 14 MB Your memory usage beats 92.06 % of python3 submissions.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        # two pointers
        # the gap between them will be equal to n
        # iterate them until the end, skip over the node at slow

        # dummy to remember the start
        dummy = ListNode(0)
        dummy.next = head
        fast = slow = dummy
        
        # move fast ahead to n
        for _ in range(n):
            fast = fast.next
        
        # iterate both until fast reaches the last one
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        
        # skip over the slow +1 by setting next to the node after slow.next
        slow.next = slow.next.next
        return dummy.next



s = Solution()

l = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
a = s.removeNthFromEnd(l, 2)
while a:
    print(a.val)
    a = a.next

a = s.removeNthFromEnd(ListNode(1), 1)
while a:
    print(a.val)
    a = a.next

a = s.removeNthFromEnd(ListNode(1, ListNode(2)), 1)
while a:
    print(a.val)
    a = a.next

