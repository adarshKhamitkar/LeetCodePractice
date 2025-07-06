"""
There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination.

Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.

Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Output: true
Explanation: There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2

Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
Output: false
Explanation: There is no path from vertex 0 to vertex 5.
"""

from typing import List
from collections import defaultdict

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        graph = defaultdict(list)
        seen_vertices = set()

        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)

        def dfs(node):
            if node == destination: return True

            for neighbour_node in graph[node]:
                if neighbour_node not in seen_vertices:
                    seen_vertices.add(neighbour_node)
                    if dfs(neighbour_node):
                        return True
            return False
        return dfs(source)
    
    #Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges.
    #Space Complexity: O(V) for the graph representation and the recursion stack.
