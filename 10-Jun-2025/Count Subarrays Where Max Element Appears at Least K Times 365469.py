# Problem: Count Subarrays Where Max Element Appears at Least K Times - https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:

        maxx = max(nums)
        l = 0
        r = 0
        c = 0
        ans = 0
        for r in range(len(nums)):
            if nums[r] == maxx:
                c += 1
            while  c >= k:
                ans += len(nums) - r
                if nums[l] == maxx:
                    c -= 1
                l += 1

        return ans

        
​
