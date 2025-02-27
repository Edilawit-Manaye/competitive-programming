# Problem: Maximum Absolute Sum of Any Subarray - https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        min_sum = float('inf')
        
        current_max = 0
        current_min = 0
        
        for num in nums:
            current_max += num
            current_min += num

            if current_max > max_sum:
                max_sum = current_max
            if current_min < min_sum:
                min_sum = current_min
            
            if current_max < 0:
                current_max = 0
            if current_min > 0:
                current_min = 0
        
        return max(abs(max_sum), abs(min_sum))

