# Problem: Continuous Subarray Sum - https://leetcode.com/problems/continuous-subarray-sum/

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False
        
        prefix_sum_mod = {0: -1}  
        current_sum = 0
        
        for i in range(len(nums)):
            current_sum += nums[i]
            if k != 0: 
                current_sum %= k
            
            if current_sum in prefix_sum_mod:
                if i - prefix_sum_mod[current_sum] > 1:  
                    return True
            else:
                prefix_sum_mod[current_sum] = i  
        
        return False