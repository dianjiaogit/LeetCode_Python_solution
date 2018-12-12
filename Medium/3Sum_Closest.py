# Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

# Example:

# Given array nums = [-1, 2, 1, -4], and target = 1.

# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        result = sum(nums[0:3])
        for i in range (0, len(nums) - 2):
            start = i + 1
            end = len(nums) - 1
            while start < end:
                if (abs(nums[i] + nums[start] + nums[end] - target) < abs(result - target)):
                    result = nums[i] + nums[start] + nums[end]
                if nums[i] + nums[start] + nums[end] > target:
                    end -= 1
                elif nums[i] + nums[start] + nums[end] < target:
                    start += 1
                else:
                    return target
        return result