# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

 

# Example 1:

# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
# Example 2:

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

# Constraints:

# 1 <= nums.length <= 8
# -10 <= nums[i] <= 10


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
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