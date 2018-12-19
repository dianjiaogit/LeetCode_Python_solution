# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

# You are given a target value to search. If found in the array return its index, otherwise return -1.

# You may assume no duplicate exists in the array.

# Your algorithm's runtime complexity must be in the order of O(log n).

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        if len(nums) == 1 and nums[0] != target:
            return -1
        half = int((len(nums) - 1) / 2)
        if nums[half] < target:
            if nums[-1] > target:
                result = Solution.search(self, nums[half + 1 : ], target)
                if result == -1:
                    return -1
                else:
                    return half + 1 + Solution.search(self, nums[half + 1 :], target)
            elif nums[-1] < target:
                if nums[-1] > nums[half]:
                    return Solution.search(self, nums[:half], target)
                else:
                    result = Solution.search(self, nums[half + 1 : ], target)
                    if result == -1:
                        return -1
                    else:
                        return half + 1 + Solution.search(self, nums[half + 1 :], target)
            else:
                return len(nums) - 1
        elif nums[half] > target:
            if nums[0] < target:
                return Solution.search(self, nums[:half], target)
            elif nums[0] > target:
                if nums[0] <= nums[half]:
                    result = Solution.search(self, nums[half + 1 :], target)
                    if result == -1:
                        return -1
                    else:
                        return half + 1 + Solution.search(self, nums[half + 1 :], target)
                else:
                    return Solution.search(self, nums[:half], target)
            else:
                return 0
        else:
            return half