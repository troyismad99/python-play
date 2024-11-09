"""
328. Odd Even Linked List

Given the head of a singly linked list, group all the nodes with odd indices together 
followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

Example 1:
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

Example 2:
Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]
 
Constraints:
The number of nodes in the linked list is in the range [0, 10^4].
-10^6 <= Node.val <= 10^6
"""

# Runtime:          3 ms      your runtime beats 15.55 % of python3 submissions.
# Memory Usage: 18.00 MB Your memory usage beats 99.84 % of python3 submissions.

from itertools import product, permutations, combinations, zip_longest
from collections import namedtuple
from typing import List, Counter, Optional

import math


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        #  guard against empty list
        if head is None:
            return None

        odd = head
        even = head.next

        #  put this in our pocket for later ;)
        first_even = even

        while even and even.next:

            odd.next = even.next
            odd = odd.next
            
            even.next = odd.next
            even = even.next


        odd.next = first_even


        return head


import unittest


class TestSolution(unittest.TestCase):

    def linked_list_to_list(self, node):
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result

    def setUp(self):
        self.s = Solution()

    def test_ExampleOne(self):
        l1 = ListNode(5)
        l2 = ListNode(4, l1)
        l3 = ListNode(3, l2)
        l4 = ListNode(2, l3)
        head = ListNode(1, l4)

        result = self.s.deleteMiddle(head)
        self.assertEqual(self.linked_list_to_list(result), [1, 3, 5, 2, 4])

    def test_ExampleTwo(self):
        l1 = ListNode(7)
        l2 = ListNode(4, l1)
        l3 = ListNode(6, l2)
        l4 = ListNode(5, l3)
        l5 = ListNode(3, l4)
        l6 = ListNode(1, l5)
        head = ListNode(2, l6)

        result = self.s.deleteMiddle(head)
        self.assertEqual(self.linked_list_to_list(result), [2, 3, 6, 7, 1, 5, 4])


unittest.main()
