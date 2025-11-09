# Problem: Sum of All Subset XOR Totals - https://leetcode.com/problems/sum-of-all-subset-xor-totals/

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total_sum = 0
        n = len(nums)
        
       
        for i in range(1 << n):  # 2^n subsets
            xor_total = 0
            for j in range(n):
                if i & (1 << j):  
                    xor_total ^= nums[j]
            total_sum += xor_total
            
        return total_sum