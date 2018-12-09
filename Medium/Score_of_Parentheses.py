# Given a balanced parentheses string S, compute the score of the string based on the following rule:

# () has score 1
# AB has score A + B, where A and B are balanced parentheses strings.
# (A) has score 2 * A, where A is a balanced parentheses string.
 

# Example 1:

# Input: "()"
# Output: 1
# Example 2:

# Input: "(())"
# Output: 2
# Example 3:

# Input: "()()"
# Output: 2
# Example 4:

# Input: "(()(()))"
# Output: 6
 

# Note:

# S is a balanced parentheses string, containing only ( and ).
# 2 <= S.length <= 50


class Solution:
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        r = 0
        count = 0
        i = 0
        start = 0
        while i < len(S):
            if S[i] == "(" and S[i + 1] != ")":
                i += 1
                start = i
                count = 0
                while count != -1:
                    if S[i] == "(":
                        count += 1
                    elif S[i] == ")":
                        count -= 1
                    i += 1
                r = r + 2 * Solution.scoreOfParentheses(self, S[start:i - 1])
            elif S[i] == "(" and S[i + 1] == ")":
                i += 2
                r += 1 
        return r