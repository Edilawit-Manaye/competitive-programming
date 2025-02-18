# Problem: Maximum Sum Obtained of Any Permutation - https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/description/

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        res = 0
        n = len(nums)
        prefix = [0] * (n + 1)

        for i , j in requests:
            prefix[i] += 1
            prefix[j+1] -= 1
    
        for k in range(1,len(prefix)):
            prefix[k] += prefix[k-1]
        
        prefix.sort(reverse = True)
        nums.sort(reverse = True)
    
        for j in range(n):
            res += nums[j] * prefix[j]
        
        return res % (10**9 + 7)
