"""
1448. Count Good Nodes in Binary Tree

Given a binary tree root, a node X in the tree is named good if in the path from root to X 
there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

Example 1:
    3
   / \
  1   4
 /   / \
3   1   5


Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: All non 1 nodes are good
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.

Example 2:
    3
   /
  3
 / \
4   2

Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.

Example 3:
Input: root = [1]
Output: 1
Explanation: Root is considered as good.

Constraints:
The number of nodes in the binary tree is in the range [1, 10^5].
Each node's value is between [-10^4, 10^4].
"""

# Runtime:        158 ms      your runtime beats  8.70 % of python3 submissions.
# Memory Usage: 31.32 MB Your memory usage beats 12.40 % of python3 submissions.

from itertools import product, permutations, combinations, zip_longest
from collections import namedtuple
from typing import List, Counter, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def goodNodes(self, root: TreeNode) -> int:

        def dfs(tree_node, current_max):

            if tree_node:

                left_path = dfs(tree_node.left, max(tree_node.val, current_max))
                right_path = dfs(tree_node.right, max(tree_node.val, current_max))

                # check path to this node
                if tree_node.val >= current_max:
                    return left_path + right_path + 1

                return left_path + right_path

            return 0

        return dfs(root, root.val)


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_ExampleOne(self):
        a = TreeNode(3, TreeNode(1, TreeNode(3)), TreeNode(4, TreeNode(1), TreeNode(5)))
        self.assertEqual(self.s.goodNodes(a), 4)

    def test_ExampleTwo(self):
        a = TreeNode(3, TreeNode(3, TreeNode(4), TreeNode(2)))
        self.assertEqual(self.s.goodNodes(a), 3)

    def test_ExampleThree(self):
        a = TreeNode(1)
        self.assertEqual(self.s.goodNodes(a), 1)


unittest.main()
