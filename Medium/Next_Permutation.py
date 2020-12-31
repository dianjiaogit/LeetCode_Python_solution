# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

# If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

# The replacement must be in place and use only constant extra memory.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [1,3,2]
# Example 2:

# Input: nums = [3,2,1]
# Output: [1,2,3]
# Example 3:

# Input: nums = [1,1,5]
# Output: [1,5,1]
# Example 4:

# Input: nums = [1]
# Output: [1]
 

# Constraints:

# 1 <= nums.length <= 100
# 0 <= nums[i] <= 100


class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a = 0
        b = 0
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