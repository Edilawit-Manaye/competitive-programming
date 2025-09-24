# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        if sum(nums)%2!=0:
            return False
        target=sum(nums)//2
        memo={}
        def dp(index,current_sum):
            
            
            if current_sum>target or index==len(nums):
                return False 
            if current_sum==target:
                return True
            if (index,current_sum) in memo:     
                return memo[(index,current_sum)]

            # include=dp(index+1,current_sum+nums[index])
            # exclude=dp(index+1,current_sum)
            # val=include or exclude
            memo[(index,current_sum)]=dp(index+1,current_sum+nums[index]) or dp(index+1,current_sum)
            return  memo[(index,current_sum)]
        return dp(0,0)


# class Solution:
#     def canPartition(self, nums: List[int]) -> bool:
#         if sum(nums) % 2 != 0:
#             return False
        
#         target= sum(nums)//2
#         memo={}
#         n=len(nums)
#         def help(idx,curr_sum):
#             if idx==n or curr_sum>target:
#                 return False
#             if curr_sum == target:
#                 return True
#             if (idx,curr_sum) in memo:
#                 return memo[(idx,curr_sum)]
#             memo[(idx,curr_sum)] = help(idx+1,curr_sum) or help(idx+1,curr_sum+nums[idx])
#             return memo[(idx,curr_sum)]        
#         return help(0,0)
