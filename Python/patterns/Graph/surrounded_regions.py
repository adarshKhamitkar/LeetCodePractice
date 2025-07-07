"""

You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell.
Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.

 

Example 1:

Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

Example 2:

Input: board = [["X"]]

Output: [["X"]]

"""

from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #1. Capture all the Border cells with temp vals. They are not surrounded 4 dimensionally so they will escape.
        #2. Change all the 'O's to 'X' in the inner cells. They can't escape since they are surrounded 4 dimensionally.
        #3. Change back all the temp vals in Border cells to 'O's.

        ROWS, COLS = len(board), len(board[0])

        def dfs(row,col):
            if row < 0 or row == ROWS or col < 0 or col == COLS or board[row][col] != 'O':
                return
            else:
                board[row][col] = 'E'
                dfs(row, col - 1)
                dfs(row, col + 1)
                dfs(row + 1, col)
                dfs(row - 1, col)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O' and (r in [0, (ROWS-1)] or c in [0, (COLS-1)]):
                    dfs(r,c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'E':
                    board[r][c] = 'O'


    # Time Complexity: O(m * n) where m is the number of rows and n is the number of columns in the board.
    # Space Complexity: O(m * n) for the recursion stack in the worst case, which can be O(m * n) if the board is filled with 'O's.
    # This is not optimal for large boards, as it uses a depth-first search (DFS) approach that can lead to high memory usage.
            