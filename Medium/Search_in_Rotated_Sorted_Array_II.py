# You are given an integer array nums sorted in ascending order (not necessarily distinct values), and an integer target.

# Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,4,4,5,6,6,7] might become [4,5,6,6,7,0,1,2,4,4]).

# If target is found in the array return its index, otherwise, return -1.

 

# Example 1:

# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true
# Example 2:

# Input: nums = [2,5,6,0,0,1,2], target = 3
# Output: false
 

# Constraints:

# 1 <= nums.length <= 5000
# -10^4 <= nums[i] <= 10^4
# nums is guaranteed to be rotated at some pivot.
# -10^4 <= target <= 10^4
 

# Follow up: This problem is the same as Search in Rotated Sorted Array, where nums may contain duplicates. Would this affect the run-time complexity? How and why?



class Solution:
    def search(self, nums, target) -> bool:
        mid = len(nums)//2
        if len(nums) == 0:
            return False
        elif len(nums) == 1:
            return nums[0] == target
        if nums[0] == nums[mid]:
            if nums[0] != target:
                return Solution.search(self, nums[1:], target)
            else:
                return True
        if nums[0] < nums[mid]:
            if target in range(nums[0], nums[mid]):
                return Solution.searchSorted(self, nums[:mid], target)
            else:
                return Solution.search(self, nums[mid:], target)
        else:
            if target in range(nums[mid], nums[-1]+1):
                return Solution.searchSorted(self, nums[mid:], target)
            else:
                return Solution.search(self, nums[:mid], target)
        
    def searchSorted(self, nums, target) -> bool:
        if len(nums) == 0:
            return False
        elif len(nums) == 1:
            return nums[0] == target
        mid = len(nums)//2
        if target < nums[0] or target > nums[-1]:
            return False
        if target < nums[mid]:
            return Solution.search(self, nums[:mid], target)
        else:
            return Solution.search(self, nums[mid:], target)