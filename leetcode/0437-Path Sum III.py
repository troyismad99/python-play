"""
437. Path Sum III

Given the root of a binary tree and an integer targetSum, return the number of paths 
where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards 
(i.e., traveling only from parent nodes to child nodes).

Example 1:
      10
     /  \
    5    -3
   / \     \
  3   2     11
 / \   \
3  -2   1

Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3 -> (5,3) (-3,11) (5,2,1)
Explanation: The paths that sum to 8 are shown.

Example 2:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3
 
Constraints:
The number of nodes in the tree is in the range [0, 1000].
-10^9 <= Node.val <= 10^9
-1000 <= targetSum <= 1000
"""

# Runtime:          15 ms      your runtime beats 44.04 % of python3 submissions.
# Memory Usage: 117.22 MB Your memory usage beats 24.60 % of python3 submissions.

from itertools import product, permutations, combinations, zip_longest
from collections import namedtuple
from typing import List, Counter, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        def dfs(node, current_sum):

            if node is None:
                return 0

            # Increment the current path's sum with the current node's value
            current_sum += node.val

            # Number of times the (current_sum - target_sum) has occurred so far
            # which indicates a valid path when subtracted from the current_sum
            path_count = path_counts[current_sum - targetSum]

            # Store the current path's sum in the counter
            path_counts[current_sum] += 1

            # Recursively find paths in left and right subtrees
            path_count += dfs(node.left, current_sum)
            path_count += dfs(node.right, current_sum)

            # Once the node is done, remove its sum from the counter
            # to not use it in the parallel subtree calls
            path_counts[current_sum] -= 1

            # Return the number of paths found
            return path_count

        # Initialize a counter to keep track of all path sums
        path_counts = Counter({0: 1})

        return dfs(root, 0)


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_ExampleOne(self):

        a = TreeNode(
            10,
            TreeNode(5, TreeNode(3, TreeNode(3), TreeNode(-2)), TreeNode(2, None, TreeNode(1))),
            TreeNode(-3, None, TreeNode(11)),
        )

        self.assertEqual(self.s.pathSum(a, 8), 3)


unittest.main()
