# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Example 1:

# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:

# Input: "cbbd"
# Output: "bb"

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        a = " "
        result = ""
        for i in s:
            a += i
            a += ' '
        for i in range (1, len(a) - 1):
            j = int(len(result) / 2)
            check = True
            while j <= i and check:
                try:
                    before = a[(i - j) : (i + j + 1)]
                    reverse = before[::-1]
                    if before == reverse:                       
                        if len(before) > len(result):
                            result = before
                    else:
                        check = False
                except:
                    check = False
                j += 1
        return result[1::2]