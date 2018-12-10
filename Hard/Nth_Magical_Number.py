# A positive integer is magical if it is divisible by either A or B.

# Return the N-th magical number.  Since the answer may be very large, return it modulo 10^9 + 7.

 

# Example 1:

# Input: N = 1, A = 2, B = 3
# Output: 2
# Example 2:

# Input: N = 4, A = 2, B = 3
# Output: 6
# Example 3:

# Input: N = 5, A = 2, B = 4
# Output: 10
# Example 4:

# Input: N = 3, A = 6, B = 4
# Output: 8
 

# Note:

# 1 <= N <= 10^9
# 2 <= A <= 40000
# 2 <= B <= 40000


class Solution(object):
    def nthMagicalNumber(self, N, A, B):
        """
        :type N: int
        :type A: int
        :type B: int
        :rtype: int
        """
        x = A
        y = B
        if x > y:
            greater = x
            smaller = y
        else:
            greater = y
            smaller = x
        while(True):
            if((greater % x == 0) and (greater % y == 0)):
                lcm = greater
                break
            greater += 1
        if A == B:
            return (N * A) % (10 ** 9 + 7)
        for i in range(1,smaller + 1):
            if((x % i == 0) and (y % i == 0)):
                hcf = i
        n = int(N / 2) * min(A, B)
        a = int(n / A) + int(n / B) - int(n / lcm)
        while a < N:
            n += hcf
            if n % A == 0 or n % B == 0:
                a += 1
        return n % (10 ** 9 + 7)