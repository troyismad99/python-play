"""
872. Leaf-Similar Trees

Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

Example 1:
      3
   __/ \_
  5      1
 / \    / \
6   2  9   8
   / \
  7   4

      3
   __/ \_
  5      1
 / \    / \
6   7  4   2
          / \
         9   8

Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true (6,7,4,9,8)

Example 2:
  1            1
 / \          / \
2   3        3   2
Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false (2,3) and (3,2)

Constraints:
The number of nodes in each tree will be in the range [1, 200].
Both of the given trees will have values in the range [0, 200].
"""

# Runtime:          0 ms      your runtime beats 100.0 % of python3 submissions.
# Memory Usage: 16.70 MB Your memory usage beats 30.04 % of python3 submissions.

from itertools import product, permutations, combinations, zip_longest
from collections import namedtuple
from typing import List, Counter, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def get_leaf_nodes(self, root):

        if root is None:
            return []

        leaves = self.get_leaf_nodes(root.left) + self.get_leaf_nodes(root.right)

        return leaves or [root.val]

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        root1_leaves = self.get_leaf_nodes(root1)
        root2_leaves = self.get_leaf_nodes(root2)

        return root1_leaves == root2_leaves


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_ExampleOne(self):

        a = TreeNode(
            3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(9), TreeNode(8))
        )
        b = TreeNode(
            3, TreeNode(5, TreeNode(6), TreeNode(7)), TreeNode(1, TreeNode(4), TreeNode(2, TreeNode(9), TreeNode(8)))
        )
        self.assertEqual(self.s.leafSimilar(a, b), True)

    def test_ExampleTwo(self):

        a = TreeNode(1, TreeNode(2), TreeNode(3))
        b = TreeNode(1, TreeNode(3), TreeNode(2))
        self.assertEqual(self.s.leafSimilar(a, b), False)


unittest.main()
