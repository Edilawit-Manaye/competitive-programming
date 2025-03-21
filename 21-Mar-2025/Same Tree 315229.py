# Problem: Same Tree - https://leetcode.com/problems/same-tree/description/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p==q==None:
            return True
        if not p or not q:
            return False 
        v1= p.val if p else 0
        v2=q.val if q else 0
        if v1 !=v2:
            return False 
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        


        