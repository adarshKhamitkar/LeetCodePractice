"""
You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.

Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2

Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
Output: 1
"""
from collections import defaultdict
from collections import deque, List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        
        _list = defaultdict(list)

        #for un-directed graph, use double links
        for u,v in edges:
            _list[u].append(v)
            _list[v].append(u)

        components = 0
        _hash = set()
        nodes = [i for i in range(n)]

        #DFS Iterative
        _stack = []
    
        for i in nodes:
            if i not in _hash:
                components += 1
                _stack = [i] #add the component and start a new stack. The number of times a new component is started is the number of components which exist in the graph
                while _stack:
                    node = _stack.pop()
                    if node not in _hash:
                        _hash.add(node) #add the node to seen set after it has been completely visited
                        for neighbour_node in _list[node]:
                            if neighbour_node not in _hash:
                                _stack.append(neighbour_node)


        #BFS Iterative
        # queue = deque()
    
        # for i in nodes:
        #     if i not in _hash:
        #         components += 1
        #         queue.append(i) #add the component and start a new stack. The number of times a new component is started is the number of components which exist in the graph
        #         while queue:
        #             node = queue.popleft()
        #             if node not in _hash:
        #                 _hash.add(node) #add the node to seen set after it has been completely visited
        #                 for neighbour_node in _list[node]:
        #                     if neighbour_node not in _hash:
        #                         queue.append(neighbour_node)
        # return components
                


        #Path compression: Rather than updating the immediate parent of a given node, we will actually update the ultimate parent of the given node. This reduces the time complexity to O(1) while identifying the true parent of any given node.

        # def find (node: int) -> int: #find the parent of a given node
        #     res = node
        #     while res != par[res]: #loop until the ultimate parent is reached
        #         par[res] = par[par[res]] #assign to ultimate parent
        #         res = par[res]
        #     return res

        # def union (node1:int, node2:int) -> int:
        #     par1, par2 = find(node1), find(node2)

        #     if par1 == par2: #no to merge if ultimate parent of both the nodes are same
        #         return 0
            
        #     if rank[par1] > rank[par2]:
        #         par[par2] = par1
        #         rank[par1] += par2
        #     else:
        #         par[par1] = par2
        #         rank[par2] += par1

        #     return 1

        # par = [i for i in range(n)] #Every node is a parent of itself
        # rank = [1] * n #every node has itself connection, rank = 1

        # res = n
        # for node1, node2 in edges:
        #     res -= union(node1, node2)

        # return res
        
        #DFS
        # graph = defaultdict(list)
        # seen_vertices = set()

        # for x,y in edges:
        #     graph[x].append(y)
        #     graph[y].append(x)

        # components = 0

        # def dfs(node):
        #     if node not in seen_vertices:
        #         seen_vertices.add(node)
        #         for neighbour_node in graph[node]:
        #             dfs(neighbour_node)
        #         return 1
        #     return 0

        # for node in range(n):
        #     components += dfs(node)

        # return components