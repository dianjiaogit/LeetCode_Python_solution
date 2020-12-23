# Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*' where: 

# '.' Matches any single character.​​​​
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).

 

# Example 1:

# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# Example 2:

# Input: s = "aa", p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
# Example 3:

# Input: s = "ab", p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
# Example 4:

# Input: s = "aab", p = "c*a*b"
# Output: true
# Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
# Example 5:

# Input: s = "mississippi", p = "mis*is*p*."
# Output: false
 

# Constraints:

# 0 <= s.length <= 20
# 0 <= p.length <= 30
# s contains only lowercase English letters.
# p contains only lowercase English letters, '.', and '*'.
# It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if s == "" and p == "":
            return True
        if s == "":
            if len(p) == 1:
                return False
            if p[1] == '*':
                p = p[2:]
                return Solution.isMatch(self, s, p)
            else:
                return False
        if p == "":
            return False
        
        p = Solution.reShape(self, p)
        
        a = s[0]
        b = p[0]
        if len(p) > 1 and p[1] == '*':
            if b == '.':
                return Solution.isMatch(self, s, p[2:]) or Solution.isMatch(self, s[1:], p) or Solution.isMatch(self, s[1:], p[2:])
            if a != b:
                p = p[2:]
                return Solution.isMatch(self, s, p)
            else:
                return Solution.isMatch(self, s[1:], p) or Solution.isMatch(self, s[1:], p[2:]) or Solution.isMatch(self, s, p[2:])
        else:
            if a != b:
                if b != '.':
                    return False
                else:
                    return Solution.isMatch(self, s[1:], p[1:])
            else:
                return Solution.isMatch(self, s[1:], p[1:])
        
    def reShape(self, p):
        newp = ""
        current = ""
        for i in range(len(p) -1):
            if p[i+1] == '*':
                check = p[i:i+2]
                if check != current:
                    current = check
                    newp = newp + current
            else:
                if p[i] != '*':
                    current = ""
                    newp = newp + p[i]
        if p[-1] != '*':
            newp = newp + p[-1]            
        return newp
            