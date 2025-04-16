# Problem: Balance a Binary Search Tree - https://leetcode.com/problems/balance-a-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # make the tree
    def treeMaker(self, arr):
        if len(arr) == 1:
            return TreeNode(arr[0])
        if len(arr) == 0:
            return 
        
        mid = len(arr) // 2
        left = self.treeMaker(arr[:mid])
        right = self.treeMaker(arr[mid+1:])

        return TreeNode(arr[mid],left,right)

    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr = []
        # traverse the tree inorder
        def inorder(node):
            if node:
                inorder(node.left)
                arr.append(node.val)
                inorder(node.right)
        inorder(root)
        print(arr)

        return self.treeMaker(arr)