# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

# Example:

# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6


class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if (height == []):
            return 0
        maximum = max(height)
        x = height.count(maximum) - 1
        index = height.index(maximum)
        result = 0
        if (index > 1):
            result += Solution.trap(self, height[:index] + [max(height[:index])])
        while x > 0:
            nextIndex = height[index + 1:].index(maximum) + index + 1
            for i in height[index + 1: nextIndex]:
                result += maximum - i
            index = nextIndex
            x -= 1
        if (index < len(height) - 1):
            result += Solution.trap(self, [max(height[index + 1:])] + height[index + 1:])
        return result