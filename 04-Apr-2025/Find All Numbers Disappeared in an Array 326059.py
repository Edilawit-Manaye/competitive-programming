# Problem: Find All Numbers Disappeared in an Array - https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

class Solution:
    def findDisappearedNumbers(self, nums):
        for i in range(len(nums)):
            while nums[i]!=i+1 and nums[i]!= nums[nums[i]-1]:
                nums[nums[i]-1],nums[i]=nums[i],nums[nums[i]-1]
        res=[]
        for i in range(len(nums)):
            if nums[i]!=i+1:
                res.append(i+1)
        return res