# Problem: Count Subarrays Where Max Element Appears at Least K Times - https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_n = max(nums)
        max_cnt = 0 
        left = 0 
        res = 0 
        for right in range(len(nums)):
            if nums[right] == max_n:
                max_cnt += 1
            
            
            while max_cnt >= k:
                if nums[left] == max_n:
                    max_cnt -= 1
                left += 1
            res += left

        return res