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
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeKLists(self, lists):
    a = None
    while len(lists) > 0:
        smallest = 10000000000000000000
        fromi = 0
        i = 0
        #print("New loop")
        while i < len(lists):
            if lists[i] == None:
                lists.remove(lists[i])
                #print("REMOVE")
                continue
            #print(lists[i].val)
            #print(len(lists))
            #print(i)
            if lists[i].val < smallest:
                #print(lists[i].val)
                smallest = lists[i].val
                fromi = i
            i += 1
        #print(smallest)
        if smallest != 10000000000000000000:
            b = ListNode(smallest)
            lists[fromi] = lists[fromi].next
            b.next = a
            a = b
    result = None
    while a != None:
        b = ListNode(a.val)
        b.next = result
        result = b
        a = a.next
    return result