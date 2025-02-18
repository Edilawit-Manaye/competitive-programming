# Problem: Maximum subarray - https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_current=max_global=nums[0]
        for i in range(1,len(nums)):
            max_current=max(nums[i],nums[i]+max_current)
            if max_current>max_global:
                max_global=max_current
        return max_global

