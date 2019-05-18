# Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

# Note:

# The solution set must not contain duplicate quadruplets.

# Example:

# Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]


class Solution:
    def fourSum(self, nums: [int], target: int) -> [[int]]:
        nums.sort()
        length = len(nums) - 1
        rset = set()
        for i in range(length - 2):
            if nums[i] + nums[-1] + nums[-2] + nums[-3] < target:
                continue
            j = length
            while j > i + 2:
                if nums[i] + nums[i + 1] + nums[i + 2] + nums[j] > target:
                    j -= 1
                    continue
                for k in range(i + 1, j - 1):
                    if nums[i] + nums[j] + nums[k] + nums[j - 1] < target:
                        continue
                    l = j - 1
                    while l > k:
                        if nums[i] + nums[j] + nums[k] + nums[l] > target:
                            l -= 1
                            continue
                        if nums[i] + nums[j] + nums[k] + nums[l] == target:
                            rset.add((nums[i], nums[k], nums[l], nums[j]))
                            break
                        l -= 1
                j -= 1
        result = []
        for i in rset:
            result.append(list(i))
        return result