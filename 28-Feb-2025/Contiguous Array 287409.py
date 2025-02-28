# Problem: Contiguous Array - https://leetcode.com/problems/contiguous-array/

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix=0
        max_len=0
        count_prefix={0:-1}  # used the initial value prefix it counts assign the value -1 because it used to calculate the length of subarray
        for i in range(len(nums)):
           if nums[i]==0:
               prefix-=1
           elif nums[i]==1:
               prefix += 1
           if prefix not in count_prefix:
               count_prefix[prefix]=i # represent indexes 
           else:
               max_len=max(max_len,i-count_prefix[prefix])
        return max_len
    
        
        
        
