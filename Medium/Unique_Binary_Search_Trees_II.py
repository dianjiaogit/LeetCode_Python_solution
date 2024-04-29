# Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

# Example 1:
# Input: n = 3
# Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]

# Example 2:
# Input: n = 1
# Output: [[1]]
 

# Constraints:

# 1 <= n <= 8

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        result = []
        d = {}
        d[0] = [None]
        one = TreeNode(1)
        d[1] =[one]
        for i in range(2, n+1):
            d = self.help(i, d)
        return d[n]
		
	
    def help(self, n, d):
        if n not in d.keys():
            lst = []
            pre_lst = d[n-1]
            for t in pre_lst:
                cur = TreeNode(n)
                cur.left = t
                lst.append(cur)
                cp = self.copy(t)
                cur = cp.right
                last = cp
                if cur == None:
                    new = TreeNode(n)
                    cp.right = new
                    lst.append(cp)
                    
                else:
                    while True:
                        if cur == None:
                            new = TreeNode(n)
                            last.right = new
                            lst.append(cp)
                            break
                        else:
                            new = TreeNode(n)
                            new.left = cur
                            last.right = new
                            tmp = self.copy(cp)
                            lst.append(tmp)
                            
                            last.right = new.left
                            last = cur
                            cur = cur.right
                            
            d[n] = lst
        return d
            
                
    def copy(self, t):
        if t:
            new = TreeNode(t.val)
            new.left = self.copy(t.left)
            new.right = self.copy(t.right)
            return new
        else:
            return None
