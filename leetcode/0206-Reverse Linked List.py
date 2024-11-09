"""
206. Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []

Constraints:
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
 

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

# Runtime:          0 ms      your runtime beats 100.0 % of python3 submissions.
# Memory Usage: 17.46 MB Your memory usage beats 91.95 % of python3 submissions.

from itertools import product, permutations, combinations, zip_longest
from collections import namedtuple
from typing import List, Counter, Optional

import math


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        #  guard against empty list
        if head is None:
            return None

        if head.next is None:
            return head

        dummy_node = ListNode()
        current = head

        while current is not None:

            next_ = current.next

            current.next = dummy_node.next
            dummy_node.next = current

            current = next_

        return dummy_node.next


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

        result = self.s.reverseList(head)
        self.assertEqual(self.linked_list_to_list(result), [5, 4, 3, 2, 1])

    def test_ExampleTwo(self):
        l1 = ListNode(2)
        head = ListNode(1, l1)

        result = self.s.reverseList(head)
        self.assertEqual(self.linked_list_to_list(result), [2, 1])

    def test_ExampleThree(self):

        result = self.s.reverseList(None)
        self.assertEqual(self.linked_list_to_list(result), [])


unittest.main()
