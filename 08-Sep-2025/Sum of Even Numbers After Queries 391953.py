# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

from typing import List

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = sum(num for num in nums if num % 2 == 0)
        re = []
        
        for value, index in queries:
            original_value = nums[index]
            nums[index] += value
            
            
            if original_value % 2 == 0:
                even_sum -= original_value 
            
            if nums[index] % 2 == 0:
                even_sum += nums[index] 
            re.append(even_sum)
        
        return re