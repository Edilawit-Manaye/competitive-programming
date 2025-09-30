# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo={}
        def dp(index,total):
            if (index,total) in memo:
                return memo[(index,total)] 
            if index==len(nums):
              return 1 if  target==total else 0
                

            memo[(index,total)]=(dp(index+1,total+nums[index]) + dp(index+1,total-nums[index]) )
            return memo[(index,total)]
        return dp(0,0)
            

        