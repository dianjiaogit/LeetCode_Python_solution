# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:

# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:

# Input: nums = [1]
# Output: [[1]]
 

# Constraints:

# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# All the integers of nums are unique.


class Solution:
    def permute(self, nums):
        result = [nums]
        x = Solution.nextPermutation(self, result[-1])
        while x not in result:
            result.append(x)
            x = Solution.nextPermutation(self, result[-1])
        return result
        
    def nextPermutation(self, num):
        """
        Do not return anything, modify nums in-place instead.
        """
        a = 0
        b = 0
        nums = num[:]
        for i in range(len(nums)):
            if nums[i] > nums[a] and nums[i] < nums[b]:
                b = i
            if i < len(nums) - 1 and nums[i] < nums[i+1]:
                a = i
                b = i+1
        if a == 0 and b == 0:
            for j in range(len(nums)//2):
                x = nums[j]
                nums[j] = nums[-j-1]
                nums[-j-1] = x
        else:
            x = nums[a]
            nums[a] = nums[b]
            nums[b] = x
            nums[a+1:] = sorted(nums[a+1:])
        return nums