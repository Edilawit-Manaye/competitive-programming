# Problem: Count Complete Subarrays in an Array - https://leetcode.com/problems/count-complete-subarrays-in-an-array/

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        total_distinct = len(set(nums))
        ck = 0
        l = 0
        freq = {}
        distinct_count = 0
        
        for right in range(len(nums)):
            if nums[right] in freq:
                freq[nums[right]] += 1
            else:
                freq[nums[right]] = 1
                distinct_count += 1
            
            while distinct_count == total_distinct:
                ck += len(nums) - right
                freq[nums[l]] -= 1
                if freq[nums[l]] == 0:
                    del freq[nums[l]]
                    distinct_count -= 1
                l+= 1
            
        return ck