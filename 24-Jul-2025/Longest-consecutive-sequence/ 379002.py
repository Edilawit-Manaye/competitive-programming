# Problem: Longest-consecutive-sequence/ - https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
       numms=set(nums)
       longest=0
       for n in numms:
           if n-1 not in numms:
             length=0
             while n+length in numms:
                    length+=1
             longest=max(longest,length)
       return longest 
           