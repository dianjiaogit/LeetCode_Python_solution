# There are two sorted arrays nums1 and nums2 of size m and n respectively.

# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

# Example 1:
# nums1 = [1, 3]
# nums2 = [2]

# The median is 2.0
# Example 2:
# nums1 = [1, 2]
# nums2 = [3, 4]

# The median is (2 + 3)/2 = 2.5


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        result = merge(nums1, nums2)
        a = len(result)
        if a % 2 == 1:
            return result[a // 2]
        else:
            return (result[a // 2] + result[a // 2 - 1]) / 2
        
def merge(nums1, nums2):
    if nums1 == []:
        return nums2
    elif nums2 == []:
        return nums1
    else:
        if nums1[0] <= nums2[0]:
            return nums1[0:1] + merge(nums1[1:], nums2)
        else:
            return nums2[0:1] + merge(nums1, nums2[1:])