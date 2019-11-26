# Write a program to find the n-th ugly number.

# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

# Example:

# Input: n = 10
# Output: 12
# Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
# Note:  

# 1 is typically treated as an ugly number.
# n does not exceed 1690.


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        m = 0
        while n > 0:
            m += 1
            if Solution.check(m):
                n -= 1
        return m
    def check(n):
        if n == 1:
            return True
        factors = {5,3,2}
        for i in factors:
            if n % i == 0:
                return Solution.check(n / i)
        return False