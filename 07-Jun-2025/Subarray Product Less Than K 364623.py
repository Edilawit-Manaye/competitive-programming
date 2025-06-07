# Problem: Subarray Product Less Than K - https://leetcode.com/problems/subarray-product-less-than-k/

from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res = 0
        left = 0
        product = 1
        
        for right in range(len(nums)):
            product *= nums[right]
            
            while left <= right and product >= k:
                product //= nums[left]
                left += 1
                
            res += (right - left + 1)
        
        return res