"""
1161. Maximum Level Sum of a Binary Tree

Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

Example 1:
      1
     / \ 
    7   0
   / \    
 -7   8   
 
Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.

Example 2:
Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
Output: 2

Constraints:
The number of nodes in the tree is in the range [1, 10^4].
-10^5 <= Node.val <= 10^5
"""

# Runtime:         22 ms      your runtime beats 59.28 % of python3 submissions.
# Memory Usage: 20.52 MB Your memory usage beats 15.51 % of python3 submissions.

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

    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        # Use deque as a queue to hold the nodes at each level
        queue = deque([root])

        current_level = 0
        max_sum = -math.inf
        max_level = 0

        while queue:

            current_level += 1
            level_sum = 0

            # Process all the nodes at the current level
            for _ in range(len(queue)):

                node = queue.popleft()
                level_sum += node.val

                # are there children to add to the queue?
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            # Update max_sum and answer if the current level's sum is greater than max_sum
            if max_sum < level_sum:
                max_sum = level_sum
                max_level = current_level

        # Return the level that had the maximum sum
        return max_level


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_ExampleOne(self):
        a = TreeNode(1, TreeNode(7, TreeNode(7), TreeNode(-8)), TreeNode(0))
        self.assertEqual(self.s.maxLevelSum(a), 2)


unittest.main()
