# Problem: Wiggle Subsequence  - https://leetcode.com/problems/wiggle-subsequence/

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        pos = 1
        neg = 1
        for i in range(1, n):
            pos2 = pos
            neg2 = neg
            
            if nums[i] > nums[i - 1]:
                pos2 = neg + 1
            elif nums[i] < nums[i - 1]:
                neg2 = pos + 1
            
            pos = pos2
            neg = neg2
        
        return max(pos, neg)