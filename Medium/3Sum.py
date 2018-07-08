# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Note:

# The solution set must not contain duplicate triplets.

# Example:

# Given array nums = [-1, 0, 1, 2, -1, -4],

# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if set(nums) == {0} and len(nums) > 2:
            return [[0,0,0]]
        r = []
        d = {}
        s = list(set(nums))
        s.sort()
        for i in range (0, len(nums)):
            if nums[i] in d.keys():
                d[nums[i]] += 1
            else:
                d[nums[i]] = 1
        for i in range (0, len(s) - 1):
            d[s[i]] -= 1
            if d[s[i]] > 0:
                d[s[i]] -= 1
                try:
                    if d[0 - s[i] - s[i]] > 0:
                        r.append([s[i], s[i], 0 - s[i] - s[i]])
                except:
                    pass
                d[s[i]] += 1
            for j in range (i + 1, len(s)):
                d[s[j]] -= 1 
                a = 0 - s[i] - s[j]
                try:
                    if a >= s[j] and d[a] > 0:
                        r.append([s[i], s[j], a])
                except:
                    pass
                d[s[j]] += 1
            d.pop(s[i])
        return r