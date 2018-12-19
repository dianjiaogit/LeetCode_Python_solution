# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

# Your algorithm's runtime complexity must be in the order of O(log n).

# If the target is not found in the array, return [-1, -1].

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]


class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1, -1]
        half = int((len(nums) - 1) / 2)
        if nums[half] > target:
            return Solution.searchRange(self, nums[:half], target)
        elif nums[half] < target:
            result = Solution.searchRange(self, nums[half + 1:], target)
            if result == [-1,-1]:
                return [-1,-1]
            else:
                result[0] += half + 1
                result[1] += half + 1
                return result
        else:
            start = half
            end = half
            check = True
            while check:
                if start - 1 >= 0 and nums[start - 1] == target:
                    start -= 1
                else:
                    check = False
            check = True
            while check:
                if end + 1 < len(nums) and nums[end + 1] == target:
                    end += 1
                else:
                    check = False
            return [start, end]