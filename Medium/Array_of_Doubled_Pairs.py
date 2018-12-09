# Given an array of integers A with even length, return true if and only if it is possible to reorder it such that A[2 * i + 1] = 2 * A[2 * i] for every 0 <= i < len(A) / 2.

# Example 1:

# Input: [3,1,3,6]
# Output: false
# Example 2:

# Input: [2,1,2,6]
# Output: false
# Example 3:

# Input: [4,-2,2,-4]
# Output: true
# Explanation: We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or [2,4,-2,-4].
# Example 4:

# Input: [1,2,4,16,8,4]
# Output: false
 

# Note:

# 0 <= A.length <= 30000
# A.length is even
# -100000 <= A[i] <= 100000


class Solution:
    def canReorderDoubled(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        A.sort()
        while len(A) > 0:
            x = A[0]
            A.pop(0)
            try:
                if x >= 0:
                    A.remove(x * 2)
                else:
                    A.remove(x / 2)
            except:
                return False
        return True