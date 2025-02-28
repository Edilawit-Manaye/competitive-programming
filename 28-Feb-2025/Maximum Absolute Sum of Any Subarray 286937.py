# Problem: Maximum Absolute Sum of Any Subarray - https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

# from typing import List

# class Solution:
#     def maxAbsoluteSum(self, nums: List[int]) -> int:
#         min_pre, max_pre = 0, 0
#         cur = 0
#         res = 0
        
#         for n in nums:
#             cur += n
#             res = max(res, abs(cur - min_pre), abs(cur - max_pre))
#             min_pre = min(min_pre, cur)
#             max_pre = max(max_pre, cur)
        
#         return res
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        maxx = nums[0]
        minn = nums[0]
        res =  nums[0]
        ans = nums[0]
        for i in range(1,len(nums)):
            maxx = max(maxx + nums[i] , nums[i])
            res = max(res, maxx)
            minn = min(minn + nums[i] , nums[i])
            ans = min(minn, ans)
        return (max(abs(res), abs(ans)))
