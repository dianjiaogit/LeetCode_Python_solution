# Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its zigzag level order traversal as:
# [
#   [3],
#   [20,9],
#   [15,7]
# ]



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root):
        result = []
        if root == None:
            return result
        result.append([root.val])
        l1 = [root]
        l2 = []
        count = 1
        while l1 != []:
            ls = []
            for i in l1:
                if i.left != None:
                    ls.append(i.left.val)
                    l2.append(i.left)
                if i.right != None:
                    ls.append(i.right.val)
                    l2.append(i.right)
            l1 = l2
            l2 = []
            if ls != []:
                if count % 2 == 1:
                    ls = ls[::-1]
                result.append(ls)
                count += 1
        return result