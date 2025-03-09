# Problem: Next Greater Element - https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextGreater=[-1]*len(nums1)
        map={n:i for i ,n in enumerate(nums1)}
        stack=[]
        for c in nums2:
            while stack and  c>stack[-1]:
                val=stack.pop()
                idex=map[val]
                nextGreater[idex]=c
            if c in nums1:
                stack.append(c)
        return nextGreater