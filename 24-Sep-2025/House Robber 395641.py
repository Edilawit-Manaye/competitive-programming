# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)     
        memo = {}
        def dp(i: int) -> int:
            if i in memo:
                return memo[i]
            if i==0:
                memo[i]=nums[i]
                return memo[i]
            elif i==1: 
                memo[i]=max(nums[0],nums[1])
                return memo[i]
            rob_current_index=dp(i-2)+nums[i]
            not_rob=dp(i-1)
            memo[i]=max(rob_current_index,not_rob)
            return memo[i]
        return dp(n-1)
            