# The count-and-say sequence is the sequence of integers with the first five terms as following:

# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.

# Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

# Note: Each term of the sequence of integers will be represented as a string.

 

# Example 1:

# Input: 1
# Output: "1"
# Example 2:

# Input: 4
# Output: "1211"


class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        result = ""
        if n > 1:
            string = Solution.countAndSay(self, n - 1)
            counter = 0
            current = 0
            for i in string:
                if int(i) == current:
                    counter += 1
                else:
                    result = result + str(counter) + str(current)
                    current = int(i)
                    counter = 1
            result = result + str(counter) + str(current)
        return result[2:] 