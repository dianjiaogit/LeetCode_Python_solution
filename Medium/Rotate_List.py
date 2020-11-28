# Given the head of a linked list, rotate the list to the right by k places.

# Example 1:
# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]

# Example 2:
# Input: head = [0,1,2], k = 4
# Output: [2,0,1]
 
# Constraints:

# The number of nodes in the list is in the range [0, 500].
# -100 <= Node.val <= 100
# 0 <= k <= 2 * 109


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return head
        if head.next == None:
            return head
        lst = [head.val]
        l = 1
        while head.next != None:
            lst.append(head.next.val)
            l += 1
            head = head.next
        k = k % l
        second = lst[:l-k][::-1]
        s = ListNode(second[0])
        for i in second[1:]:
            new = ListNode(i)
            new.next = s
            s = new
        first = lst[l-k:][::-1]
        for i in first:
            new = ListNode(i)
            new.next = s
            s = new
        return s