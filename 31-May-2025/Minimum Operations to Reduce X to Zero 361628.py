# Problem: Minimum Operations to Reduce X to Zero - https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/description/

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        cur_sum = 0
        max_window = -1
        left = 0
        
        for right in range(len(nums)):
            cur_sum += nums[right]
            while left <= right and cur_sum > target:
                cur_sum -= nums[left]
                left += 1
            if cur_sum == target:
                max_window = max(max_window, right - left + 1)
        
        return -1 if max_window == -1 else len(nums) - max_window