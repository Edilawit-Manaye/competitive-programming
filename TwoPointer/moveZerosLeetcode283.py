class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=0 # time=O(n) and space=O(1)
        for num in  nums:
            if num!=0:
                nums[l]=num
                l+=1
        while l<len(nums):
            nums[l]=0
            l+=1

        
