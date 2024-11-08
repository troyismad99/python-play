"""
2095. Delete the Middle Node of a Linked List

You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, 
where ⌊x⌋ denotes the largest integer less than or equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.

Example 1:
Input: head = [1,3,4,7,1,2,6]
Output: [1,3,4,1,2,6]
Explanation:
The above figure represents the given linked list. The indices of the nodes are written below.
Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
We return the new list after removing this node. 

Example 2:
Input: head = [1,2,3,4]
Output: [1,2,4]
Explanation:
The above figure represents the given linked list.
For n = 4, node 2 with value 3 is the middle node, which is marked in red.

Example 3:
Input: head = [2,1]
Output: [2]
Explanation:
The above figure represents the given linked list.
For n = 2, node 1 with value 1 is the middle node, which is marked in red.
Node 0 with value 2 is the only node remaining after removing node 1.

Constraints:
The number of nodes in the list is in the range [1, 10^5].
1 <= Node.val <= 10^5
"""

# Runtime:         xx ms      your runtime beats xxxxx % of python3 submissions.
# Memory Usage: xxxxx MB Your memory usage beats xxxxx % of python3 submissions.

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

        #  Two pointers
        #  fast & slow approach

        dummy_node = ListNode(next=head)

        slow = dummy_node
        fast = head

        while fast and fast.next:

            # slow one at a time
            slow = slow.next

            # fast two at a time
            fast = fast.next.next

        # once fast is at the end, slow is at the node prior to the middle

        # remove the middle node by skipping over
        slow.next = slow.next.next

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
        l1 = ListNode(6)
        l2 = ListNode(2, l1)
        l3 = ListNode(1, l2)
        l4 = ListNode(7, l3)
        l5 = ListNode(4, l4)
        l6 = ListNode(3, l5)
        head = ListNode(1, l6)

        result = self.s.deleteMiddle(head)
        self.assertEqual(self.linked_list_to_list(result), [1, 3, 4, 1, 2, 6])

    def test_ExampleTwo(self):
        l1 = ListNode(4)
        l2 = ListNode(3, l1)
        l3 = ListNode(2, l2)
        head = ListNode(1, l3)

        result = self.s.deleteMiddle(head)
        self.assertEqual(self.linked_list_to_list(result), [1, 2, 4])

    def test_ExampleThree(self):
        l1 = ListNode(1)
        head = ListNode(2, l1)

        result = self.s.deleteMiddle(head)
        self.assertEqual(self.linked_list_to_list(result), [2])


unittest.main()
