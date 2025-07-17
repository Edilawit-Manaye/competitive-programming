# Problem: Convert Sorted Array to Binary Search Tree - https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helppp(l,r):
           if l>r:
              return None
           mid=(l+r)//2
           root=TreeNode(nums[mid])
           root.left=helppp(l,mid-1)
           root.right=helppp(mid+1,r)
           return root
        return helppp(0,len(nums)-1)
