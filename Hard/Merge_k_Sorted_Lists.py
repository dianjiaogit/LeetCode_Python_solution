# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

# Example:

# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        a = None
        dic = {}
        for i in lists:
            if i != None:
                if i.val not in dic.keys():
                    dic[i.val] = [i]
                else:
                    dic[i.val].append(i)
        while len(dic) > 0:
            smallest = min(dic.keys())
            b = ListNode(smallest)
            x = dic[smallest][0]
            if x.next != None:
                if x.next.val in dic.keys():
                    dic[x.next.val].append(x.next)
                else:
                    dic[x.next.val] = [x.next]
            if len(dic[smallest]) == 1:
                dic.pop(smallest)
            else:
                dic[smallest].pop(0)  
            b.next = a
            a = b
        result = None
        while a != None:
            b = ListNode(a.val)
            b.next = result
            result = b
            a = a.next
        return result