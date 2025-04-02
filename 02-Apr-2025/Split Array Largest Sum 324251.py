# Problem: Split Array Largest Sum - https://leetcode.com/problems/split-array-largest-sum/

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def isValid(c):
             count=1
             cur_sum=0
             for num in nums:
                 cur_sum+=num
                 if cur_sum >c:
                    count+=1
                    cur_sum=num
             return count<=k
        low=max(nums)
        high=sum(nums)
        res=high
        while low<=high:
            mid=(low+high)//2
            if isValid(mid):
                high=mid-1
                res=mid
            else:
                low=mid+1
        return res



 