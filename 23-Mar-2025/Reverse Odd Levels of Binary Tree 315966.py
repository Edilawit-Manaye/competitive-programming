# Problem: Reverse Odd Levels of Binary Tree - https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return []
        q=deque([root])
        index_level=0
        while q :
                length=len(q)
                if index_level%2==1:
                    l=0
                    r=length-1
                    while l<r:
                        q[l].val ,q[r].val=q[r].val,q[l].val
                        l+=1
                        r-=1
                for _ in range(length):
                    node=q.popleft()
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                index_level+=1
        return root 
                    

