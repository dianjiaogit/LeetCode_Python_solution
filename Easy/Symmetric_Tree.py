# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
 

# But the following [1,2,2,null,3,null,3] is not:

#     1
#    / \
#   2   2
#    \   \
#    3    3
 

# Follow up: Solve it both recursively and iteratively.



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root) -> bool:
        if root == None:
            return True
        if root.left == None and root.right == None:
            return True
        l1 = [root.left, root.right]
        l2 = []
        while len(l1) > 0:
            check = []
            for i in l1:
                if i == None:
                    check.append(None)
                else:
                    check.append(i.val)
            if check[::-1] != check:
                return False
            for i in l1:
                if i != None:
                    l2.append(i.left)
                    l2.append(i.right)
            l1 = l2
            l2 = []
        return True