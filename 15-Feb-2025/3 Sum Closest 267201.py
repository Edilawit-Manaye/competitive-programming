# Problem: 3 Sum Closest - https://leetcode.com/problems/3sum-closest/description/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n=len(nums)
        closest_sum=float("inf")
        nums.sort()
        for i in range(n):
            if  i>0 and nums[i]==nums[i-1]:
                continue
            l,r=i+1,n-1
            while l<r:
                 current_sum=nums[i]+nums[l]+nums[r]
                 if abs(current_sum-target) < abs(target-closest_sum):
                      closest_sum=current_sum
                 if current_sum==target:
                      return current_sum
                 if current_sum<target:
                      l+=1
                 else:
                      r-=1
        return closest_sum
             
        
       