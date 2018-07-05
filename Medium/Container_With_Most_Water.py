# Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

# Note: You may not slant the container and n is at least 2.

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        x = 0
        y = len(height) - 1
        m = 0
        while x < y:
            a = min(height[x], height[y]) * (y - x)
            if a > m:
                m = a
            if height[x] > height[y]:
                y -= 1
            else:
                x += 1
        return m