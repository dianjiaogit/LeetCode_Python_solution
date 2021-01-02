# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
# Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

# Constraints:

# 1 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= starti <= endi <= 10^4



class Solution:
    def merge(self, intervals):
        intervals.sort()
        result = []
        i = 0
        while i in range(0, len(intervals) - 1):
            a = intervals[i]
            b = intervals[i+1]
            if a[1] < b[0]:
                result.append(a)
            if b[0] in range(a[0], a[1] + 1):
                intervals[i + 1] = [a[0], max(a[1], b[1])]
            i += 1
        result.append(intervals[-1])
        return result