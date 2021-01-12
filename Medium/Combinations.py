# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

# You may return the answer in any order.

# Example 1:

# Input: n = 4, k = 2
# Output:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]
# Example 2:

# Input: n = 1, k = 1
# Output: [[1]]
 

# Constraints:

# 1 <= n <= 20
# 1 <= k <= n



class Solution:
    def combine(self, n: int, k: int):
        lst = [i for i in range(1, n+1)]
        return Solution.combLst(self, lst, k)
            
    def combLst(self, lst, k):
        if k == 1:
            return [[i] for i in lst]
        result = []
        for i in range(len(lst)-1):
            l = Solution.combLst(self, lst[i+1:], k-1)
            for j in l:
                current = [lst[i]]
                current.extend(j)
                result.append(current)
        return result