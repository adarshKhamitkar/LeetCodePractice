"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid,r,c):
            if(r < 0 or c < 0 or r >= len(grid) or c>=len(grid[0]) or grid[r][c]!="1"): return
            grid[r][c] = "0" #mark visited
            dfs(grid,r-1,c)
            dfs(grid,r+1,c)
            dfs(grid,r,c-1)
            dfs(grid,r,c+1)

        num_of_islands = 0
        if not grid: return -1
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if(grid[i][j] == "1"):
                    dfs(grid,i,j)
                    num_of_islands+=1
        return num_of_islands
