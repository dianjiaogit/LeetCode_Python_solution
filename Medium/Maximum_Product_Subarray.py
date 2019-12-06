# Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

# Example 1:

# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:

# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        maxSoFar = nums[0]
        if nums[0] >= 0:
            maxCurrent = nums[0]
            maxAbs = nums[0]
            numOfNegative = 0
        else:
            maxAbs = abs(nums[0])
            maxCurrent = None
            numOfNegative = 1
        for i in nums[1:]:
            if i == 0:
                if maxCurrent != None:
                    maxSoFar = max(maxSoFar, maxCurrent)
                maxCurrent = 0
                maxAbs = 0
                numOfNegative = 0
            elif i > 0:
                if maxCurrent != None:
                    maxCurrent = max(maxCurrent * i, i)
                else:
                    maxCurrent = i
                maxAbs = max(maxAbs * i, i)
            else:
                maxAbs = max(maxAbs * abs(i), abs(i))
                numOfNegative += 1
                if numOfNegative % 2 == 0:
                    if maxCurrent != None:
                        maxCurrent = max(maxAbs, maxCurrent)
                    else:
                        maxCurrent = maxAbs
                else:
                    if maxCurrent != None:
                        maxSoFar = max(maxSoFar, maxCurrent)
                    maxCurrent = None
        if maxCurrent != None:
            maxSoFar = max(maxSoFar, maxCurrent)
        return maxSoFar