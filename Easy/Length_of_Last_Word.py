# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

# If the last word does not exist, return 0.

# Note: A word is defined as a character sequence consists of non-space characters only.

# Example:

# Input: "Hello World"
# Output: 5


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if set(s) == {' '} or len(s) == 0:
            return 0
        else:
            s = s[::-1]
            while s[0] == ' ':
                s = s[1:]
            a = s.find(' ')
            if a == -1:
                return len(s)
            else:
                return a