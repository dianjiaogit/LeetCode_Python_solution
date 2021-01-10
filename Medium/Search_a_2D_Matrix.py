# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
 

# Example 1:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
# Example 2:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -10^4 <= matrix[i][j], target <= 10^4



class Solution:
    def searchMatrix(self, matrix, target):
        start = 0
        end = len(matrix) - 1
        while start + 1 < end:
            line = matrix[(end - start)//2 + start]
            if target < line[0]:
                end = (end - start)//2 + start
            else:
                start = (end - start)//2 + start
        if target < matrix[start][0]:
            return False
        if target > matrix[end][-1]:
            return False
        if target >= matrix[start][0] and target <= matrix[start][-1]:
            return Solution.searchLine(matrix[start], target)
        elif target >= matrix[end][0] and target <= matrix[end][-1]:
            return Solution.searchLine(matrix[end], target)
        else:
            return False
        
    def searchLine(line, target):
        start = 0
        end = len(line) - 1
        while start + 1 < end:
            if target < line[(end - start)//2 + start]:
                end = (end - start)//2 + start
            else:
                start = (end - start)//2 + start
        if target == line[start] or target == line[end]:
            return True
        else:
            return False