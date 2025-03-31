# Problem: House Robber IV - https://leetcode.com/problems/house-robber-iv/

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def isValid(c):
            count=0
            i=0
            while i < len(nums):
                if c >= nums[i]:
                    count+=1
                    i+=2
                else:
                    i+=1
            return  count>=k
        low=min(nums)
        high=max(nums)
        res=0
        while low<=high:
            mid=(low+high)//2
            if isValid(mid):
                high=mid-1
                res=mid
            else:
                low=mid+1
        return res
        