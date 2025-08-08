# Problem: Longest Nice Subarray - https://leetcode.com/problems/longest-nice-subarray/

from typing import List

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        result = 0
        curr = 0  
        left = 0 
        
        for right in range(len(nums)):
            while curr & nums[right]:
                curr ^= nums[left]
                left += 1
            curr |= nums[right]
            result = max(result, right - left + 1)
        
    
        return result 