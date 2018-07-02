# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

# Example 1:

# Input: "()"
# Output: true
# Example 2:

# Input: "()[]{}"
# Output: true
# Example 3:

# Input: "(]"
# Output: false
# Example 4:

# Input: "([)]"
# Output: false
# Example 5:

# Input: "{[]}"
# Output: true


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = []
        for i in range(0, len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                a.append(s[i])
            else:
                if a == []:
                    return False
                if abs(ord(s[i]) - ord(a[-1])) <= 2:
                    a.pop(-1)
                else:
                    return False
        if a != []:
            return False
        return True