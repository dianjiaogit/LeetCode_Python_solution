# Given an unsorted integer array, find the smallest missing positive integer.

# Example 1:

# Input: [1,2,0]
# Output: 3
# Example 2:

# Input: [3,4,-1,1]
# Output: 2
# Example 3:

# Input: [7,8,9,11,12]
# Output: 1
# Note:

# Your algorithm should run in O(n) time and uses constant extra space.


class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if nums == [] or nums[0] > 1:
            return 1
        for i in range (0, len(nums) - 1):
            if nums[i] < 1 and nums[i + 1] > 1:
                return 1
            elif nums[i] > 0 and nums[i + 1] > nums[i] + 1:
                return nums[i] + 1
        return nums[-1] + 1