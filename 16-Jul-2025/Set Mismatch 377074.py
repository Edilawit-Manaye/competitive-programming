# Problem: Set Mismatch - https://leetcode.com/problems/set-mismatch/description/

class Solution:
    def findErrorNums(self, nums):
        for i in range(len(nums)):
            while nums[i] != i+1 and nums[i] !=nums[nums[i]-1]:
                pos = nums[i]-1
                nums[i],nums[pos]=nums[pos],nums[i]
        result=[]
        for i in range(len(nums)):
            if nums[i]!=i+1:
                result.append(nums[i])
                result.append(i+1)
        return result 


                  


        