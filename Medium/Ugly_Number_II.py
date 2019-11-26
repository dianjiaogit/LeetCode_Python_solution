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
        if n == 1:
            return 1
        n = n - 1
        primes = set()
        factors = {2,3,5}
        m = 2
        while True:
            #print(m)
            #print(primes)
            check1 = 0
            for i in primes:
                if m % i == 0:
                    check1 = 1
                    break
            if check1 == 1:
                m += 1
                continue
            check2 = 0
            for i in factors:
                if m % i == 0:
                    check2 = 1
                    break
            if check2 == 0:
                primes.add(m)
            else:
                n = n - 1
                if n == 0:
                    return m
            m += 1