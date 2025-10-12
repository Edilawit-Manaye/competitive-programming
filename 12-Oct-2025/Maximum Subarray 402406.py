# Problem: Maximum Subarray - https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_c=max_gloal=nums[0]
        for i in range(1,len(nums)):
            max_c=max(nums[i],nums[i]+max_c)
            if max_c>max_gloal:
                max_gloal=max_c
        return max_gloal 
