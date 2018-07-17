# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

# You may assume the integer does not contain any leading zero, except the number 0 itself.

# Example 1:

# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Example 2:

# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        c = 0
        if digits[-1] == 9:
            digits[-1] = 0
            c = 1
        else:
            digits[-1] += 1
        if c == 1:
            for i in range (1, len(digits)):
                if digits[-i - 1] == 9:
                    digits[-i - 1] = 0
                else:
                    digits[-i - 1] += 1
                    return digits
        else:
            return digits
        digits = [1] + digits
        return digits