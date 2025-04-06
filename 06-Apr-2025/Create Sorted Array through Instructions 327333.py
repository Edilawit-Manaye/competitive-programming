# Problem: Create Sorted Array through Instructions - https://leetcode.com/problems/create-sorted-array-through-instructions/

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        nums = SortedList()
        total_cost = 0
        MOD = 10**9 + 7
        
        for instruction in instructions:
            less_count = nums.bisect_left(instruction)
            greater_count = len(nums) - nums.bisect_right(instruction)
            total_cost += min(less_count, greater_count)
            nums.add(instruction)
        
        return total_cost % MOD