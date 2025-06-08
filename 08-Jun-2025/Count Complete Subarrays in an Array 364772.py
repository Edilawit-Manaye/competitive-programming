# Problem: Count Complete Subarrays in an Array - https://leetcode.com/problems/count-complete-subarrays-in-an-array/

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        res = 0
        distinct = len(set(nums))
        cnt = Counter()
        right = 0
        
        for left in range(len(nums)):
            while right < len(nums) and len(cnt) < distinct:
                cnt[nums[right]] += 1
                right += 1
            
            if len(cnt) == distinct:
                res += len(nums) - right + 1
            
            cnt[nums[left]] -= 1
            if cnt[nums[left]] == 0:
                del cnt[nums[left]]
        
        return res