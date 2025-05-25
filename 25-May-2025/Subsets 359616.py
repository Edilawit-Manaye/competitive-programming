# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        powerr_set = []
        n = len(nums)
        
        
        for mask in range(1 << n):
            subset = []
            
            for i in range(n):
                if mask & (1 << i):
                    subset.append(nums[i])
            powerr_set.append(subset)
        
        return powerr_set
        ## return 