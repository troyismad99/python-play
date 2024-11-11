"""
1466. Reorder Routes to Make All Paths Lead to the City Zero

There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way 
to travel between two different cities (this network form a tree). 
Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.

This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

Your task consists of reorienting some roads such that each city can visit the city 0. 
Return the minimum number of edges changed.

It's guaranteed that each city can reach city 0 after reorder.

Example 1:
  *    *
0 -> 1 -> 3 <-2
 \<- 4 -> 5
        *
Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
Output: 3
Explanation: Change the direction of edges show in * such that each node can reach the node 0 (capital).

Example 2:
0 <- 1 -> 2 <- 3 -> 4
        *         *
Input: n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
Output: 2
Explanation: Change the direction of edges show in * such that each node can reach the node 0 (capital).

Example 3:
Input: n = 3, connections = [[1,0],[2,0]]
Output: 0

Constraints:
2 <= n <= 5 * 10^4
connections.length == n - 1
connections[i].length == 2
0 <= ai, bi <= n - 1
ai != bi
"""

# Runtime:        187 ms      your runtime beats 56.60 % of python3 submissions.
# Memory Usage: 50.05 MB Your memory usage beats 48.85 % of python3 submissions.

from itertools import product, permutations, combinations, zip_longest
from collections import namedtuple, defaultdict
from typing import List, Counter

import math


class Solution:

    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        #  how will the poeple get home if all the roads are changed to point to city 0?

        def dfs(node):

            visited[node] = True
            count = 0

            # Iterate over connected nodes of the current node.
            for connected_node in adjacency_list[node]:

                if not visited[connected_node]:

                    # If the edge from the current node to the connected node is in
                    # the original direction, increase the reorder count.
                    if (node, connected_node) in directed_edges:
                        count += 1

                    # Add the result of recursively calling dfs on the connected node.
                    count += dfs(connected_node)

            return count

        # Create an adjacency list and a set to store directed edges.
        adjacency_list = defaultdict(list)

        directed_edges = set()

        # Populate the adjacency list and directed edges set.
        for a, b in connections:
            adjacency_list[a].append(b)
            adjacency_list[b].append(a)
            directed_edges.add((a, b))

        # Initialize a list to keep track of visited nodes.
        visited = [False] * n

        # Start the depth-first search from node 0 and return the reorder count.
        return dfs(0)


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_ExampleOne(self):
        self.assertEqual(self.s.minReorder(6, [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]), 3)

    def test_ExampleTwo(self):
        self.assertEqual(self.s.minReorder(5, [[1, 0], [1, 2], [3, 2], [3, 4]]), 2)

    def test_ExampleThree(self):
        self.assertEqual(self.s.minReorder(3, [[1, 0], [2, 0]]), 0)


unittest.main()
