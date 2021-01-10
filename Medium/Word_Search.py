# Given an m x n board and a word, find if the word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where "adjacent" cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

# Example 1:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true

# Example 2:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true

# Example 3:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false
 

# Constraints:

# m == board.length
# n = board[i].length
# 1 <= m, n <= 200
# 1 <= word.length <= 10^3
# board and word consists only of lowercase and uppercase English letters.



class Solution:
    def exist(self, board, word):
        result = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    result.append([(i, j)])
        if len(word) == 1:
            if result != []:
                return True
            else:
                return False
        while result != []:
            r = result.pop(0)
            l = len(r)
            if l < len(word):
                lst = Solution.check(self, board, word[l], r)
                lst.extend(result)
                result = lst
            else:
                return True   
        return False
                            
                
    
    def getNeigh(self, board, a, b):
        result = {}
        if a != 0:
            if board[a-1][b] not in result:
                result[board[a-1][b]] = [(a-1, b)]
            else:
                result[board[a-1][b]].append((a-1, b))
        if b != 0:
            if board[a][b-1] not in result:
                result[board[a][b-1]] = [(a, b-1)]
            else:
                result[board[a][b-1]].append((a, b-1))
        if a != len(board)-1:
            if board[a+1][b] not in result:
                result[board[a+1][b]] = [(a+1, b)]
            else:
                result[board[a+1][b]].append((a+1, b))
        if b != len(board[a])-1:
            if board[a][b+1] not in result:
                result[board[a][b+1]] = [(a, b+1)]
            else:
                result[board[a][b+1]].append((a, b+1))        
        return result
    
    def check(self, board, w, r):
        newResult = []
        last = r[-1]
        d = Solution.getNeigh(self, board, last[0], last[1])
        if w in d:
            for i in d[w]:
                new = r[:]
                if i not in r:
                    new.append(i)
                    newResult.append(new)
        return newResult