# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it.

# Example:

# Input: 5
# Output:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]

class Solution:
    def generate(self, numRows: int) -> [[int]]:
        if numRows == 0:
            return []
        result = [[1]]
        counter = 1
        while (numRows > 1):
            lastRow = result[-1]
            currentRow = [1]
            for i in range (0, counter - 1):
                currentRow.append(lastRow[i] + lastRow[i + 1])
            currentRow.append(1)
            result.append(currentRow)
            numRows -= 1
            counter += 1
        return result