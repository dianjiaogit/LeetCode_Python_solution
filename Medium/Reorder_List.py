# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

# Example 1:


# Input: head = [1,2,3,4]
# Output: [1,4,2,3]
# Example 2:


# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]
 

# Constraints:

# The number of nodes in the list is in the range [1, 5 * 104].
# 1 <= Node.val <= 1000


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head == None or head.next == None or head.next.next == None:
            return head
        h = head
        length = 0
        while h != None:
            length += 1
            h = h.next

        self.helper(head, length)
            

    def helper(self, head, length):
        if length == 1:
            last = head.next
            head.next = None
            return last
        if length == 2:
            last = head.next.next
            head.next.next = None
            return last
        last = self.helper(head.next, length - 2)
        sort = head.next
        tmp = last.next
        head.next = last
        last.next = sort
        return tmp