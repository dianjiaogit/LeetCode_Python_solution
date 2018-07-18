# Given two binary strings, return their sum (also a binary string).

# The input strings are both non-empty and contains only characters 1 or 0.

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        n = 0
        a = int(a)
        b = int(b)
        r = 0
        c = 0
        while a * b != 0:
            if a % 10 == 1 and b % 10 == 1:
                r += c * 10 ** n
                c = 1
            elif (a % 10 == 1 or b % 10 == 1) and c == 1:
                c = 0
                pass
            else:
                r += (a % 10 + b % 10 + c) * 10 ** n
                if c == 1:
                    c = 0
            a = int(a / 10)
            b = int(b / 10)
            n += 1
        if c == 1:
            r += int(Solution.addBinary(self,str(a + b), c)) * 10 ** n
        else:
            r += (a + b) * 10 ** n
        return str(r)