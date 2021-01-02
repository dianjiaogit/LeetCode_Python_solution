# Given an m x n matrix, return all elements of the matrix in spiral order.

# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]

# Example 2:
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100


class Solution:
    def spiralOrder(self, matrix):
        m = len(matrix)
        if m == 0:
            return None
        n = len(matrix[0])
        if n == 0:
            return None
        result = []
        for i in range(n):
            result.append(matrix[0][i])
        for i in range(1, m):
            result.append(matrix[i][-1])
        if m > 1:
            for i in range(2, n+1):
                result.append(matrix[-1][-i])
        if n > 1:
            for i in range(2, m):
                result.append(matrix[-i][0])
        m = matrix[1:-1]
        for i in range(len(m)):
            m[i] = m[i][1:-1]
        x = Solution.spiralOrder(self, m)
        if x != None:
            result.extend(x)
        return result