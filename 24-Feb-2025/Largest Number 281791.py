# Problem: Largest Number - https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for index,val in enumerate(nums):
            nums[index]=str(val)
        def compare(n1,n2):
            if n1+n2>n2+n1:
                return -1
            else:
                return 1
        nums=sorted(nums,key=cmp_to_key(compare)) # cmp_to_key is a function used for sorting
        return str(int("".join(nums)))
        
        