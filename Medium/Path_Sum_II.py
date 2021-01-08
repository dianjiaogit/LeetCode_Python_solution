# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

# Note: A leaf is a node with no children.

# Example:

# Given the below binary tree and sum = 22,

#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \    / \
# 7    2  5   1
# Return:

# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root, sum):
        if root == None:
                return []
        if root.val == sum:
            if root.left == None and root.right == None:
                return [[root.val]]
        x = Solution.pathSum(self, root.left, sum - root.val)
        y = Solution.pathSum(self, root.right, sum - root.val)
        result = []
        for i in x:
            a = [root.val]
            a.extend(i)
            result.append(a)
        for i in y:
            a = [root.val]
            a.extend(i)
            result.append(a)
        return result