# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

# Example 1:

# Input: "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()"
# Example 2:

# Input: ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()"


class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        index = []
        longest = 0
        count = 0
        for i in range (0, len(s)):
            if s[i] == '(':
                stack.append((s[i],i))
            else:
                if stack != []:
                    start = stack[-1][-1]
                    stack.pop(-1)
                    index.append(start)
                    index.append(i)
        index.sort()
        for i in range (0, len(index) - 1):
            if index[i] == index[i + 1] - 1:
                count += 1
            else:
                if count != 0:
                    longest = max(longest, count + 1)
                    count = 0
        if count != 0:
            longest = max(longest, count + 1)
        return longest