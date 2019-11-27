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
        lst = [1]
        i2 = 0
        i3 = 0
        i5 = 0
        for i in range (1, n):
            smallest = min(lst[i2] * 2,
                           lst[i3] * 3,
                           lst[i5] * 5)
            lst.append(smallest)
            if smallest == lst[i2] * 2:
                i2 += 1
            if smallest == lst[i3] * 3:
                i3 += 1
            if smallest == lst[i5] * 5:
                i5 += 1
        return lst[-1]