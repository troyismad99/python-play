'''
234. Palindrome Linked List

Given the head of a singly linked list, return true if it is a palindrome.

Example 1:
    Input: head = [1,2,2,1]
    Output: true

Example 2:
    Input: head = [1,2]
    Output: false

Constraints:
    The number of nodes in the list is in the range [1, 10^5].
    0 <= Node.val <= 9

Follow up: 
    Could you do it in O(n) time and O(1) space?
'''
# Runtime: 632 ms       Your runtime beats 51.57 % of python3 submissions.
# Memory Usage: 31.5 MB Your memory usage beats 50.64 % of python3 submissions.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        # Similar to a two pointer approach used with lists
        # fast will reach the end of the list 
        # slow will reach the middle
        slow = fast = head

        # points to a reversed version of the first half
        rev = None

        # A lot happening here:
        #   fast moves to the end
        #   slow moves to the middle
        #   rev gets created while slow and fast are moving
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next

        # if the element count is even slow will stop on the last element
        # of the first half. Move it to the first element of the second half
        if fast:
            slow = slow.next

        # compare the two halves
        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next

        return rev is None

# examples
s = Solution()

a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(2)
a.next.next.next = ListNode(1)
print(s.isPalindrome(a))

a = ListNode(1)
a.next = ListNode(2)
print(s.isPalindrome(a))
