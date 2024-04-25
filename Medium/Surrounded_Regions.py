# Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

# A region is captured by flipping all 'O's into 'X's in that surrounded region.

# Example 1:

# Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
# Explanation: Notice that an 'O' should not be flipped if:
# - It is on the border, or
# - It is adjacent to an 'O' that should not be flipped.
# The bottom 'O' is on the border, so it is not flipped.
# The other three 'O' form a surrounded region, so they are flipped.

# Example 2:

# Input: board = [["X"]]
# Output: [["X"]]

# Constraints:

# m == board.length
# n == board[i].length
# 1 <= m, n <= 200
# board[i][j] is 'X' or 'O'.


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        width = len(board[0])
        height = len(board)
        for i in range(width):
            if board[0][i] == 'O':
                self.get_all_connected(board, 0, i)
            if board[height-1][i] == 'O':
                self.get_all_connected(board, height-1, i)
        for j in range(height):
            if board[j][0] == 'O':
                self.get_all_connected(board, j, 0)
            if board[j][width-1] == 'O':
                self.get_all_connected(board, j, width-1)
        for i in range(height):
            for j in range(width):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '*':
                    board[i][j] = 'O'
	
	
    def get_all_connected(self, board, x, y):
        width = len(board[0])
        height = len(board)
        if (not (x < 0 or y < 0 or x == height or y == width)) and board[x][y] == 'O':
            board[x][y] = '*'
            self.get_all_connected(board, x-1, y)
            self.get_all_connected(board, x, y-1)
            self.get_all_connected(board, x, y+1)
            self.get_all_connected(board, x+1, y)