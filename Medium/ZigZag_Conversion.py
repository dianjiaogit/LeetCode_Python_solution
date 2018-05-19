# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);
# Example 1:

# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:

# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:

# P     I    N
# A   L S  I G
# Y A   H R
# P     I


class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        a = 1
        dic = {}
        check = False
        result = ''
        for i in range(len(s)):
            if a in dic:
                dic[a] = dic[a] + s[i]
            else:
                dic[a] = s[i]
            if a < numRows and a > 1:
                if check == False:
                    a += 1
                else:
                    a -= 1
            elif a == numRows:
                check = True
                a -= 1
            elif a == 1:
                check = False
                a += 1
        for j in range(1, numRows + 1):
            try:
                result = result + dic[j]
            except KeyError:
                pass
        return result