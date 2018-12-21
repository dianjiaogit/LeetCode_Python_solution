# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

# Example 1:

# Input: num1 = "2", num2 = "3"
# Output: "6"
# Example 2:

# Input: num1 = "123", num2 = "456"
# Output: "56088"
# Note:

# The length of both num1 and num2 is < 110.
# Both num1 and num2 contain only digits 0-9.
# Both num1 and num2 do not contain any leading zero, except the number 0 itself.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.


class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        len1 = len(num1)
        first = 0
        for i in range (0, len(num1)):
            first += (ord(num1[i]) - 48) * 10 ** (len1 - 1)
            len1 -= 1
        len2 = len(num2)
        second = 0
        for i in range (0, len(num2)):
            second += (ord(num2[i]) - 48) * 10 ** (len2 - 1)
            len2 -= 1
        product = first * second
        if product == 0:
            return "0"
        result = ""
        while product > 0:
            result = chr((product % 10) + 48) + result
            product = product // 10
        return result