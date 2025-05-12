# Problem: https://neetcode.io/problems/same-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True
        elif not p or not q: return False
        else:
            cond1 =  p.val == q.val 
            cond2 = self.isSameTree(p.left, q.left)
            cond3 = self.isSameTree(p.right, q.right)
            return cond1 and cond2 and cond3
