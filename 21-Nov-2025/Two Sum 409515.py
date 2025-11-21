# Problem: Two Sum - https://leetcode.com/problems/two-sum/description

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       mappp={}
       for i in range(len(nums)):
        comp=target-nums[i]
        if comp in mappp:
            return [i,mappp[comp]]
        mappp[nums[i]]=i