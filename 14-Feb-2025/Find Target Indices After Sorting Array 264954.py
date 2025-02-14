# Problem: Find Target Indices After Sorting Array - https://leetcode.com/problems/find-target-indices-after-sorting-array/

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        sorted_nums=sorted(nums)
        res=[]
        for i,val in enumerate(sorted_nums):
            if val ==target:
                res.append(i)
        return res 
        