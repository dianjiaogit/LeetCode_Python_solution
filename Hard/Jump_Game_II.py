# Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

# Each element in the array represents your maximum jump length at that position.

# Your goal is to reach the last index in the minimum number of jumps.

# You can assume that you can always reach the last index.

# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: nums = [2,3,0,1,4]
# Output: 2
 

# Constraints:

# 1 <= nums.length <= 3 * 10^4
# 0 <= nums[i] <= 10^5


class Solution:
    def jump(self, nums) -> int:
        mini = 0
        i = 0
        while i < len(nums):
            if i == len(nums) - 1:
                break
            a = nums[i]
            if len(nums) - 1 <= i + a:
                mini += 1
                break
            lst = nums[i+1:i+a+1]
            for j in range(len(lst)):
                lst[j] = lst[j] + j
            m = max(lst)
            for j in range(len(lst)):
                if m == lst[j]:
                    index = j
            mini += 1
            i = i + index + 1
        return mini