# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for c in range(0,len(nums)+1):
            if c not in nums:
                return c

    
