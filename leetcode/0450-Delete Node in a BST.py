"""
450. Delete Node in a BST

Given a root node reference of a BST and a key, delete the node with the given key in the BST. 
Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.

Example 1:


Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

Example 2:

Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
Explanation: The tree does not contain a node with value = 0.

Example 3:
Input: root = [], key = 0
Output: []

Constraints:
The number of nodes in the tree is in the range [0, 10^4].
-10^5 <= Node.val <= 10^5
Each node has a unique value.
root is a valid binary search tree.
-10^5 <= key <= 10^5

Follow up: Could you solve it with time complexity O(height of tree)?
"""

# Runtime:          4 ms      your runtime beats  9.48 % of python3 submissions.
# Memory Usage: 20.45 MB Your memory usage beats 23.93 % of python3 submissions.

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

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if root is None:
            return None

        # three options:
        # a. key is smaller
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root

        # b. key is larger
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
            return root

        # c. key is equal (we found the node to remove)

        # If the node has only one child or no child
        if root.left is None:
            return root.right

        if root.right is None:
            return root.left

        # Two children
        min_right_subtree = root.right

        while min_right_subtree.left:
            min_right_subtree = min_right_subtree.left

        # Copy the inorder successor's content to this node
        root.val = min_right_subtree.val

        # Delete the inorder successor
        root.right = self.deleteNode(root.right, min_right_subtree.val)

        return root


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
        a = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, None, TreeNode(7)))

        b1 = TreeNode(5, TreeNode(4, TreeNode(2)), TreeNode(6, None, TreeNode(7)))
        b2 = TreeNode(5, TreeNode(2, None, TreeNode(4)), TreeNode(6, None, TreeNode(7)))

        c = self.s.deleteNode(a, 3)
        self.assertTrue(self.compare_trees(b1, c) or self.compare_trees(b2, c))

    def test_ExampleTwo(self):
        a = TreeNode(5, TreeNode(2, None, TreeNode(4)), TreeNode(6, None, TreeNode(7)))
        c = self.s.deleteNode(a, 0)
        self.assertTrue(self.compare_trees(a, c))

    def test_ExampleThree(self):
        a = TreeNode()
        c = self.s.deleteNode(a, 0)
        self.assertIsNone(c)


unittest.main()
