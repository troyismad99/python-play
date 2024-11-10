"""
236. Lowest Common Ancestor of a Binary Tree

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: 
“The lowest common ancestor is defined between two nodes p and q as the lowest node in T 
that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Example 1:
      3
   __/ \_
  5      1
 / \    / \
6   2  0   8
   / \
  7   4

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:
      3
   __/ \_
  5      1
 / \    / \
6   2  0   8
   / \
  7   4

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1
 
Constraints:
The number of nodes in the tree is in the range [2, 10^5].
-10^9 <= Node.val <= 10^9
All Node.val are unique.
p != q
p and q will exist in the tree.
"""

# Runtime:          15 ms      your runtime beats 44.04 % of python3 submissions.
# Memory Usage: 117.22 MB Your memory usage beats 24.60 % of python3 submissions.

from itertools import product, permutations, combinations, zip_longest
from collections import namedtuple
from typing import List, Counter, Optional

import functools as fn


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        if not root or root == p or root == q:
            return root

        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        if l and r:
            return root

        return l or r


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_ExampleOne(self):

        a = TreeNode(
            3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(0), TreeNode(8))
        )

        b = self.s.lowestCommonAncestor(a, TreeNode(5), TreeNode(1))

        self.assertEqual(b, TreeNode(3))

    def test_ExampleTwo(self):

        a = TreeNode(
            3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(0), TreeNode(8))
        )

        self.assertEqual(self.s.lowestCommonAncestor(a, TreeNode(5), TreeNode(4)), (TreeNode(5)))

    def test_ExampleThree(self):
        a = TreeNode(1, None, TreeNode(2))
        self.assertEqual(self.s.lowestCommonAncestor(a, TreeNode(1), TreeNode(2)), TreeNode(1))


unittest.main()
