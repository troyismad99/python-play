"""
1372. Longest ZigZag Path in a Binary Tree

You are given the root of a binary tree.

A ZigZag path for a binary tree is defined as follow:

Choose any node in the binary tree and a direction (right or left).
If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
Change the direction from right to left or from left to right.
Repeat the second and third steps until you can't move in the tree.
Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

Return the longest ZigZag path contained in that tree.

Example 1:
1
 \
  1*
 / \
1   1*
   / \
  1*   1
   \
    1*
     \
      1

Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]
Output: 3
Explanation: Longest ZigZag path in blue nodes (right -> left -> right).

Example 2:
  1*
 / \
1*   1
 \
  1*
 / \
1*   1
 \
  1*

Input: root = [1,1,1,null,1,null,null,1,1,null,1]
Output: 4
Explanation: Longest ZigZag path in blue nodes (left -> right -> left -> right).

Example 3:
Input: root = [1]
Output: 0

Constraints:
The number of nodes in the tree is in the range [1, 5 * 10^4].
1 <= Node.val <= 100
"""

# Runtime:         55 ms      your runtime beats 77.47 % of python3 submissions.
# Memory Usage: 31.61 MB Your memory usage beats 30.15 % of python3 submissions.

from itertools import product, permutations, combinations, zip_longest
from collections import namedtuple
from typing import List, Counter, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.max_length = 0

    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        def dfs(node, left_length, right_length):

            # If the node is None, we've reached the end of a path
            if node is None:
                return

            self.max_length = max(self.max_length, left_length, right_length)

            # Recursively explore the left child, incrementing the "left_length" as we are
            # making a zig (left direction) from the right side of the current node
            dfs(node.left, right_length + 1, 0)

            # Recursively explore the right child, incrementing the "right_length" as we are
            # making a zag (right direction) from the left side of the current node
            dfs(node.right, 0, left_length + 1)

       
        # Start DFS with the root of the tree, initial lengths are 0 as starting point
        dfs(root, 0, 0)

        # Once DFS is complete, return the maximum zigzag length found
        return self.max_length


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_ExampleOne(self):
        a = TreeNode(
            1,
            None,
            TreeNode(1, TreeNode(1), TreeNode(1, TreeNode(1, None, TreeNode(1, None, TreeNode(1))), TreeNode(1))),
        )

        self.assertEqual(self.s.longestZigZag(a), 3)

    def test_ExampleTwo(self):
        a = TreeNode(1, TreeNode(1, None, TreeNode(1, TreeNode(1, None, TreeNode(1)), TreeNode(1))), TreeNode(1))
        self.assertEqual(self.s.longestZigZag(a), 4)

    def test_ExampleThree(self):
        a = TreeNode(1)
        self.assertEqual(self.s.longestZigZag(a), 0)


unittest.main()
