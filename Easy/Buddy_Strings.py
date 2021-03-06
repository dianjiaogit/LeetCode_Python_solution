# Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.

 

# Example 1:

# Input: A = "ab", B = "ba"
# Output: true
# Example 2:

# Input: A = "ab", B = "ab"
# Output: false
# Example 3:

# Input: A = "aa", B = "aa"
# Output: true
# Example 4:

# Input: A = "aaaaaaabc", B = "aaaaaaacb"
# Output: true
# Example 5:

# Input: A = "", B = "aa"
# Output: false
 

# Note:

# 0 <= A.length <= 20000
# 0 <= B.length <= 20000
# A and B consist only of lowercase letters.


class Solution:
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if (len(A) != len(B)):
            return False
        a = 0
        for i in range(0, len(A)):
            if (A[i] != B[i]):
                a += 1
        if (a == 2 and set(A) == set(B)):
            return True
        if (a == 0 and len(A) != len(set(A))):
            return True
        return False