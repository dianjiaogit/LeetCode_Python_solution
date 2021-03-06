# Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

# Example 1:

# Input: 1->2->3->3->4->4->5
# Output: 1->2->5
# Example 2:

# Input: 1->1->1->2->3
# Output: 2->3


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        if head.val == head.next.val:
            while head.val == head.next.val:
                head = head.next
                if head == None:
                    return head
                if head.next == None:
                    return None
            head = head.next
            return Solution.deleteDuplicates(self, head)
        else:
            head.next = Solution.deleteDuplicates(self, head.next)
            return head