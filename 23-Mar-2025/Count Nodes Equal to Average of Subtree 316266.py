# Problem: Count Nodes Equal to Average of Subtree - https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
       res=0
       def traverse(node):
          nonlocal res
          if not node:
             return (0,0)
          node_left,node_countl=traverse(node.left)
          node_right,node_countr=traverse(node.right)
          sum=node_left+node_right + node.val
          n=node_countl+node_countr+1
          average=sum//n

          if average==node.val:
            res+=1
          return sum,n
       traverse(root)
       return res 