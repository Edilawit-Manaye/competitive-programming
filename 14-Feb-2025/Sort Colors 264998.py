# Problem: Sort Colors - https://leetcode.com/problems/sort-colors/



class Solution:
    def sortColors(self, nums: List[int]) -> None:
        
        n=len(nums)

        for i in range(n-1):
            is_sorted=True
            for j in range(1,n-i):
                if nums[j]<nums[j-1]:
                    nums[j],nums[j-1]=nums[j-1],nums[j]
                    is_sorted=False
            if is_sorted:
                break
        return nums
