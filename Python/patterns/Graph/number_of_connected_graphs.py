"""
You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.

Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2

Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
Output: 1
"""
from typing import List
from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        seen_vertices = set()

        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)


        connected_components = 0

        def dfs(node):
            if node not in seen_vertices:
                seen_vertices.add(node)
                for neighbour_node in graph[node]:
                    dfs(neighbour_node)
                return 1
            return 0

        for node in range(n):
            connected_components += dfs(node)

        return connected_components
    
    # Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges.
    # Space Complexity: O(V) for the graph representation and the recursion stack.