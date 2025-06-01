# Problem: Max Consecutive Ones III - https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_w=0
        left=0
        n= len(nums)
        nums_zero=0
        for r in range(n):
            if nums[r]==0:
                nums_zero+=1
            while nums_zero >k:
                if nums[left]==0:
                    nums_zero-=1
                left+=1
            max_w=max(max_w,r-left+1)
        return max_w
