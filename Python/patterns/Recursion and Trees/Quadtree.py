#Construct a QuadTree

from typing import List
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
        
class QuadTree:
    def construct(self, grid:List[List[int]]) -> Node:
        def dfs(n, r, c):
            #compare the topleft element to every other element to identify the break point
            isAllSame = True
            for i in range(n):
                for j in range(n):
                    if r == i and c == j: continue
                    if grid[r][c] != grid[r+i][c+i]:
                        isAllSame = False
                        break
            #Check if every element in the quadrant is same; check and return for leaf nodes
            if isAllSame:
                return Node(grid[r][c], True, None, None, None, None)
            #Divide the quadrant by 2 and check the process for each sub-quadrant to return the leaf nodes          
            n = n // 2
            topLeft = dfs(n, r, c)
            topRight = dfs(n, r, c + n)
            bottomLeft = dfs(n, r + n, c)
            bottomRight = dfs(n, r + n, c + n)
            
            return Node(grid[r][c], False, topLeft, topRight, bottomLeft, bottomRight)
            
        return dfs(len(grid), 0, 0)
    
if __name__ == "__main__":
    grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
    
    qt = QuadTree()
    print(qt.construct(grid))

#Time Complexity: O(n^2 log n)
#Space Complexity: O(n^2)