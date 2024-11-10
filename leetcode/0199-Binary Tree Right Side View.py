"""
199. Binary Tree Right Side View

Given the root of a binary tree, imagine yourself standing on the right side of it, 
return the values of the nodes you can see ordered from top to bottom.

 

Example 1:
  1
 / \ 
2   3
 \   \ 
  5   4
 

Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:
Input: root = [1,null,3]
Output: [1,3]

Example 3:
Input: root = []
Output: []
 

Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""

# Runtime:          0 ms      your runtime beats 100.0 % of python3 submissions.
# Memory Usage: 16.69 MB Your memory usage beats 28.40 % of python3 submissions.

from itertools import product, permutations, combinations, zip_longest
from collections import deque, namedtuple
from typing import List, Counter, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.max_length = 0

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        rights = []

        if root is None:
            return rights

        # Use deque as a queue to hold the nodes at each level
        queue = deque([root])

        while queue:

            # The rightmost element at the current level is visible from the right side
            rights.append(queue[-1].val)

            # Iterate over nodes at the current level
            for _ in range(len(queue)):

                # Pop the node from the left side of the queue
                current_node = queue.popleft()

                # If left child exists, add it to the queue
                if current_node.left:
                    queue.append(current_node.left)

                # If right child exists, add it to the queue
                if current_node.right:
                    queue.append(current_node.right)

        return rights


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_ExampleOne(self):
        a = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
        self.assertEqual(self.s.rightSideView(a), [1, 3, 4])

    def test_ExampleTwo(self):
        a = TreeNode(1, None, TreeNode(3))
        self.assertEqual(self.s.rightSideView(a), [1, 3])

    def test_ExampleThree(self):
        a = TreeNode()
        self.assertEqual(self.s.rightSideView(a), [0])


unittest.main()
