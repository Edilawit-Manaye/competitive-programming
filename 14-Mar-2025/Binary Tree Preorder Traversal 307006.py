# Problem: Binary Tree Preorder Traversal - https://leetcode.com/problems/binary-tree-preorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #    if node is None:
        #       return
        #    print(root.data, end=", ")
        #    preOrderTraversal(root.left)
        #    preOrderTraversal(root.right)
        output=[]
        def helper(node):
            if node is None:
                return 
            output.append(node.val)
            helper(node.left)
            helper(node.right)
        helper(root)
        return output


        