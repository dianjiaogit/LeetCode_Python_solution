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
        i = 0
        while (i < len(s)):
            for j in range (0, i + 1):
                x = s[j : (len(s) - i + j)]
                a = x[::-1]
                if (x == a):
                    return x
            i = i + 1