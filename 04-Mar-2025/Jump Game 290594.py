# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal=len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if i+nums[i]>=goal:
                goal=i
        return True if goal==0 else False 
# another approach
# class Solution:
#    def canJump(self, nums: List[int]) -> bool:
#       n=len(nums)
#       reach=0  
#       for i in range(n) :
          
#          if reach<i:  
#                 return False
#          cur_reach=i+nums[i]
#          reach=max(reach,cur_reach)
#       return True 
