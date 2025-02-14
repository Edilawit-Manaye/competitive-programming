# Problem: How Many Numbers Are Smaller Than the Current Number - https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

#the optimal solution 
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        count_map = {}
        for index, value in enumerate(sorted_nums):
            if value not in count_map:
                count_map[value] = index
        
        result = []
        for num in nums:
            result.append(count_map[num])
        
        return result
# the brute force approach
# class Solution:
#     def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
#         n=len(nums)
#         res=[0]*len(nums)
#         count=0
#         for i in range(n):
#             for j in range(n):
#                 if nums[j]< nums[i]:
#                     count += 1
#             res[i]=count
#             count=0
#         return res 
        