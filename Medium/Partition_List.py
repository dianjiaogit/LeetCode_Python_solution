# Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

# You should preserve the original relative order of the nodes in each of the two partitions.

# Example 1:


# Input: head = [1,4,3,2,5,2], x = 3
# Output: [1,2,2,4,3,5]
# Example 2:

# Input: head = [2,1], x = 2
# Output: [1,2]

# Constraints:

# The number of nodes in the list is in the range [0, 200].
# -100 <= Node.val <= 100
# -200 <= x <= 200

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head, x: int):
        if head == None:
            return None
        if head.next == None:
            return head
        left_start = None
        left_cur = None
        right_start = None
        right_cur = None
        while head != None:
            if head.val < x:
                if left_start == None:
                    left_start = ListNode(head.val)
                    left_cur = left_start
                else:
                    left_cur.next = ListNode(head.val)
                    left_cur = left_cur.next
            else:
                if right_start == None:
                    right_start = ListNode(head.val)
                    right_cur = right_start
                else:
                    right_cur.next = ListNode(head.val)
                    right_cur = right_cur.next
            head = head.next
        if left_start == None:
            return right_start
        if right_start == None:
            return left_start
        left_cur.next = right_start
        return left_start