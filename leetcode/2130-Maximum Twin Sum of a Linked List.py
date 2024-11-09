"""
2130. Maximum Twin Sum of a Linked List

In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list 
is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. 
These are the only nodes with twins for n = 4.
The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the maximum twin sum of the linked list.

Example 1:
Input: head = [5,4,2,1]
Output: 6
Explanation:
Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
There are no other nodes with twins in the linked list.
Thus, the maximum twin sum of the linked list is 6. 

Example 2:
Input: head = [4,2,2,3]
Output: 7
Explanation:
The nodes with twins present in this linked list are:
- Node 0 is the twin of node 3 having a twin sum of 4 + 3 = 7.
- Node 1 is the twin of node 2 having a twin sum of 2 + 2 = 4.
Thus, the maximum twin sum of the linked list is max(7, 4) = 7. 

Example 3:
Input: head = [1,100000]
Output: 100001
Explanation:
There is only one node with a twin in the linked list having twin sum of 1 + 100000 = 100001.
 
Constraints:
The number of nodes in the list is an even integer in the range [2, 10^5].
1 <= Node.val <= 10^5
"""

# Runtime:         67 ms      your runtime beats 82.74 % of python3 submissions.
# Memory Usage: 46.73 MB Your memory usage beats 16.31 % of python3 submissions.

from itertools import product, permutations, combinations, zip_longest
from collections import namedtuple
from typing import List, Counter, Optional

import math


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def pairSum(self, head: Optional[ListNode]) -> int:

        # fast / slow pointers

        list_sum = []
        max_sum = -math.inf

        dummy_node = ListNode(next=head)

        slow = dummy_node
        fast = head

        while fast and fast.next:

            # slow one at a time
            slow = slow.next

            # we could remove the list and reverse the first half of the list
            list_sum.append(slow.val)

            # fast two at a time
            fast = fast.next.next

        # once fast is at the end, slow is at the node prior to the middle
        max_sum = -math.inf

        for i in reversed(list_sum):
            slow = slow.next
            max_sum = max(max_sum, i + slow.val)

        return max_sum


import unittest


class TestSolution(unittest.TestCase):

    def linked_list_to_list(self, node):

        result = []

        while node:
            result.append(node.val)
            node = node.next

        return result

    def list_to_linked_list(self, vals):

        dummy_node = ListNode()
        last_node = dummy_node

        for i in vals:
            current_node = ListNode(i)
            last_node.next = current_node
            last_node = last_node.next

        return dummy_node.next

    def setUp(self):
        self.s = Solution()

    def test_ExampleOne(self):
        head = self.list_to_linked_list([5, 4, 2, 1])
        result = self.s.pairSum(head)
        self.assertEqual(result, 6)

    def test_ExampleTwo(self):
        head = self.list_to_linked_list([4, 2, 2, 3])

        result = self.s.pairSum(head)
        self.assertEqual(result, 7)

    def test_ExampleTwo(self):
        head = self.list_to_linked_list([1, 100000])
        result = self.s.pairSum(head)
        self.assertEqual(result, 100001)


unittest.main()
