# Given an integer array nums, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets.

# Example 1:

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]
 

# Constraints:

# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.



class Solution:
    def subsets(self, nums):
        result = [[]]
        if nums == []:
            return result
        l = len(nums)
        n = 2**l
        for i in range(1, n):
            b = bin(i)
            current = []
            b = b[2:]
            b = b[::-1]
            for j in range(len(b)):
                if b[j] == "1":
                    current.append(nums[-j-1])
            result.append(current)
        return result