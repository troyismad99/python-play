'''
1192. Critical Connections in a Network

There are n servers numbered from 0 to n-1 connected by undirected server-to-server 
connections forming a network where connections[i] = [a, b] represents a connection 
between servers a and b. Any server can reach any other server directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some server unable to reach some other server.

Return all critical connections in the network in any order.

Example 1:
    Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
    Output: [[1,3]]
    Explanation: [[3,1]] is also accepted.

3---1--2
    | /
    |/
    0
 
Constraints:
    1 <= n <= 10^5
    n-1 <= connections.length <= 10^5
    connections[i][0] != connections[i][1]
    There are no repeated connections.
'''
# Runtime: 2152 ms      Your runtime beats 94.48 % of python3 submissions.
# Memory Usage: 84.6 MB Your memory usage beats 78.94 % of python3 submissions.

class Solution:
    def criticalConnections(self, n: int, connections: list[list[int]]) -> list[list[int]]:

        # Createa graph structure that captures the paths from a node
        graph = [[] for i in range(n)]
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        # print(graph)

        depths = [-1] * n
        results = []

        def dfs(prev_node, cur_node, cur_depth):

            depths[cur_node] = cur_depth
            min_depth = cur_depth

            for neighbour in graph[cur_node]:

                # "Check yo self, before you wreck yo self."
                if neighbour == prev_node: 
                    continue

                # how deep is this neighbour
                neighbour_depth = depths[neighbour]
                
                # -1 indicates not processed
                if neighbour_depth == -1:
                    neighbour_depth = dfs(cur_node, neighbour, cur_depth+1)
                
                if neighbour_depth > cur_depth:
                    results.append([cur_node, neighbour])
                else:
                    min_depth = min(min_depth, neighbour_depth)
            
            depths[cur_node] = min_depth
            return min_depth

        # start at node-0
        dfs(None, 0, 0)

        return results

s = Solution()
print(s.criticalConnections(4, [[0,1],[1,2],[2,0],[1,3]]))
