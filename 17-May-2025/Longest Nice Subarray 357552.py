# Problem: Longest Nice Subarray - https://leetcode.com/problems/longest-nice-subarray/

from typing import List

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        res = 0
        cur = 0  
        left = 0 
        
        for right in range(len(nums)):
            while cur & nums[right]:
                cur ^= nums[left]
                left += 1
            cur |= nums[right]
            res = max(res, right - left + 1)
        
        return res