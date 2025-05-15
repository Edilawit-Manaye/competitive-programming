# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expected_num=0
        actual_num=0
        for i ,num in enumerate(nums):
            expected_num+=i+1
            actual_num+=num
        diff=expected_num-actual_num
        return diff
            
    
