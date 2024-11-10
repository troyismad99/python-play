"""
700. Search in a Binary Search Tree

You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted 
with that node. If such a node does not exist, return null.

Example 1:
     4
    / \ 
   2   7
  / \    
 1   3   

Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]

Example 2:
Input: root = [4,2,7,1,3], val = 5
Output: []

Constraints:
The number of nodes in the tree is in the range [1, 5000].
1 <= Node.val <= 10^7
root is a binary search tree.
1 <= val <= 10^7
"""

# Runtime:          0 ms      your runtime beats 100.0 % of python3 submissions.
# Memory Usage: 18.56 MB Your memory usage beats 26.14 % of python3 submissions.

from itertools import product, permutations, combinations, zip_longest
from collections import namedtuple, deque
from typing import List, Counter, Optional

import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if root is None or root.val == val:
            return root

        if root.val < val:
            return self.searchBST(root.right, val)

        return self.searchBST(root.left, val)


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def compare_trees(self, tree1: TreeNode, tree2: TreeNode) -> bool:

        if tree1 or tree2:
            return (
                False
                if not tree1 or not tree2
                else (
                    tree1.val == tree2.val
                    and self.compare_trees(tree1.left, tree2.left)
                    and self.compare_trees(tree1.right, tree2.right)
                )
            )
        else:
            return True

    def test_ExampleOne(self):
        a = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
        b = TreeNode(2, TreeNode(1), TreeNode(3))

        c = self.s.searchBST(a, 2)
        self.assertTrue(self.compare_trees(b, c))

    def test_ExampleTwo(self):
        a = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
        c = self.s.searchBST(a, 5)
        self.assertIsNone(c)


unittest.main()
