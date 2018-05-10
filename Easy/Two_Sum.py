# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range (len(nums)):
            if nums[i] < target / 2:
                try:
                    if i < nums.index(target - nums[i]):
                        return [i, nums.index(target - nums[i])]
                    elif i > nums.index(target - nums[i]):
                        return [nums.index(target - nums[i]), i]
                except:
                    pass
        for i in range (len(nums) - 1):
            if nums[i] == target / 2:
                nums.remove(target / 2)
                try:
                    return [i, nums.index(target / 2) + 1]
                except:
                    pass