# Problem: Find All Numbers Disappeared in an Array - https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        num_set = set(nums)
        missing_numbers = []
        
        for i in range(1, n + 1):
            if i not in num_set:
                missing_numbers.append(i)
        
        return missing_numbers

