# Problem: Delete Node in a BST - https://leetcode.com/problems/delete-node-in-a-bst/

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return root
        elif key<root.val:
            root.left=self.deleteNode(root.left,key)
        elif key>root.val:
            root.right=self.deleteNode(root.right,key)
        else:
            if not root.left:
                return root.right 
            elif not root.right:
                return root.left
            curr=root.right
            while curr.left:
                curr=curr.left
            root.val=curr.val
            root.right=self.deleteNode(root.right,root.val)
        return root