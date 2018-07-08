# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# For example, given n = 3, a solution set is:

# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 1:
            return ["()"]
        elif n > 1:
            a = []
            b = Solution.generateParenthesis(self, n-1)
            for i in b:
                x = "(" + i + ")"
                a.append(x)
                y = "()" + i
                a.append(y)
                z = i + "()"
                a.append(z)
            for i in range(1, int(n / 2) + 1):
                x = Solution.generateParenthesis(self, i)
                y = Solution.generateParenthesis(self, n - i)
                for j in x:
                    for k in y:
                        a.append(j + k)
                        a.append(k + j)
            a = list(set(a))
            return a