'''
86. Partition List

Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example 1:
    Input: head = [1,4,3,2,5,2], x = 3
    Output: [1,2,2,4,3,5]

Example 2:
    Input: head = [2,1], x = 2
    Output: [1,2]

Constraints:
    The number of nodes in the list is in the range [0, 200].
    -100 <= Node.val <= 100
    -200 <= x <= 200
'''
# Runtime: 36 ms        Your runtime beats 54.24 % of python3 submissions.
# Memory Usage: 14.4 MB 


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        # Create two lists and combine them

        # two lists with a dummy ListNode
        small_start = ListNode(0)
        big_start = ListNode(0)

        # two points
        sp = small_start
        lp = big_start

        while head:
            if head.val < x:
                sp.next = head
                sp = sp.next
            else:
                lp.next = head
                lp = lp.next

            head = head.next
        
        # join them up
        lp.next = None           # we might have a new end
        sp.next = big_start.next # end of smaller than list points to start of greater than than list
        return small_start.next

l = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2))))))

s = Solution()
a = s.partition(l, 3)

while a:
    print(a.val)
    a = a.next

l = ListNode(2, ListNode(1))

s = Solution()
a = s.partition(l, 2)

while a:
    print(a.val)
    a = a.next
