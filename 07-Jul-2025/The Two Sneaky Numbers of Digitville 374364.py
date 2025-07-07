# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

# from typing import List

# class Solution:
#     def getSneakyNumbers(self, nums: List[int]) -> List[int]:
#         counts = [0] * len(nums)
#         x= []

#         for num in nums:
#             counts[num] += 1
#             if counts[num] == 2:  
#                 x.append(num)
#         return x
from typing import List
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        count=[0]*len(nums)
        x=[]
        for num in nums:
            count[num]+=1
            if count[num]==2:
                x.append(num)
        return x


        

        