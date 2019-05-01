# Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

# Note that the row index starts from 0.


# In Pascal's triangle, each number is the sum of the two numbers directly above it.

# Example:

# Input: 3
# Output: [1,3,3,1]
# Follow up:

# Could you optimize your algorithm to use only O(k) extra space?

class Solution:
    def getRow(self, rowIndex: int) -> [int]:
        if rowIndex == 0:
            return [1]
        result = [1]
        counter = 1
        while (rowIndex > 0):
            currentRow = [1]
            for i in range (0, counter - 1):
                currentRow.append(result[i] + result[i + 1])
            currentRow.append(1)
            result = currentRow
            rowIndex -= 1
            counter += 1
        return result