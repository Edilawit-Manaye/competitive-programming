# Problem: Minimum Operations to Exceed Threshold Value II - https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        num_operation=0
        heapq.heapify(nums)
        while len(nums)>1 and nums[0]<k:
            x=heapq.heappop(nums)
            y=heapq.heappop(nums)
            res=2*min(x,y)+max(x,y)
            heapq.heappush(nums,res)
            num_operation += 1
        return num_operation
        if nums and num[0]<k:
            return -1
            

