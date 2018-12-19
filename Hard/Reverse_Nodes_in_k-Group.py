# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

# Example:

# Given this linked list: 1->2->3->4->5

# For k = 2, you should return: 2->1->4->3->5

# For k = 3, you should return: 3->2->1->4->5

# Note:

# Only constant extra memory is allowed.
# You may not alter the values in the list's nodes, only nodes itself may be changed.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return None
        else:
            lst = []
            check = False
            for i in range (0, k):
                if (head != None):
                    lst.append(head.val)
                    head = head.next
                else:
                    check = True
                    break                                            
            if check:
                    i = len(lst) - 1
                    while i >= 0:
                        newList = ListNode(lst[i])
                        newList.next = head
                        head = newList
                        i -= 1
                    return head
            else:
                result = Solution.reverseKGroup(self, head, k)
                for i in lst:
                    newList = ListNode(i)
                    newList.next = result
                    result = newList
                return result