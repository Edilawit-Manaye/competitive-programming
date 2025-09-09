# Problem: Maximum Number of Pairs in Array - https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        count = Counter(nums)  
        p = 0
        leftovers = 0
        
        for freq in count.values():
            p += freq // 2
            leftovers += freq % 2  
        
        return [p, leftovers]
        