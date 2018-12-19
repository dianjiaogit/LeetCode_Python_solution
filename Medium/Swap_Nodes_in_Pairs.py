# Given a linked list, swap every two adjacent nodes and return its head.

# Example:

# Given 1->2->3->4, you should return the list as 2->1->4->3.
# Note:

# Your algorithm should use only constant extra space.
# You may not modify the values in the list's nodes, only nodes itself may be changed.



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        else:
            first = head.val
            head = head.next
            if head == None:
                return ListNode(first)
            else:
                second = head.val
                head = head.next
                newList = ListNode(second)
                newList.next = ListNode(first)
                newList.next.next = Solution.swapPairs(self, head)
                return newList