# There are N children standing in a line. Each child is assigned a rating value.

# You are giving candies to these children subjected to the following requirements:

# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# What is the minimum candies you must give?

# Example 1:

# Input: [1,0,2]
# Output: 5
# Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
# Example 2:

# Input: [1,2,2]
# Output: 4
# Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
#              The third child gets 1 candy because it satisfies the above two conditions.


class Solution:
    def candy(self, ratings) -> int:
        if ratings == []:
            return 0
        new1 = [1 for i in ratings]
        new2 = [1 for i in ratings]
        changedForward = True
        changedBackward = True
        ratings2 = ratings[::-1]
        while changedForward and changedBackward:
            changedForward = False
            changedBackward = False
            for i in range(len(ratings)):
                n = Solution.getNei(self, ratings, i)
                for j in n:
                    if ratings[j] < ratings[i] and new1[j] >= new1[i]:
                        changedForward = True
                        new1[i] = new1[j] + 1
                        
            for i in range(len(ratings2)):
                n = Solution.getNei(self, ratings2, i)
                for j in n:
                    if ratings2[j] < ratings2[i] and new2[j] >= new2[i]:
                        changedBackward = True
                        new2[i] = new2[j] + 1
        if changedForward:
            return sum(new2)
        else:
            return sum(new1)
            
    def getNei(self, ratings, i):
        if i == 0:
            if len(ratings) == 1:
                return []
            else:
                return [1]
        if i == len(ratings) - 1:
            return [i-1]
        return [i-1, i+1]