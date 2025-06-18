# Problem: Binary Subarrays With Sum - https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def helper(x):
            total=0
            left=0
            res=0
            if x<0:
                return 0
            for right in range(len(nums)):
                    total+=nums[right]
                    while total>x:
                        total-=nums[left]
                        left +=1
                    res += right-left+1
            return res
        return helper(goal)-helper(goal-1)
        



