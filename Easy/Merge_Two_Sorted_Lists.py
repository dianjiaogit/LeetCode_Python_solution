# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

# Example:

# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        if l1.val <= l2.val:
            if l1.next == None:
                l1.next = l2
                return l1
            else:
                l1.next = Solution.mergeTwoLists(self, l1.next, l2)
                return l1
        else:
            if l2.next == None:
                l2.next = l1
                return l2
            else:
                l2.next = Solution.mergeTwoLists(self, l1, l2.next)
                return l2