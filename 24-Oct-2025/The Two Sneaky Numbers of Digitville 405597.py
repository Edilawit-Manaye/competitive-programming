# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        count=[0]*len(nums)
        xxx=[]
        for num in nums:
            count[num]+=1
            if count[num]==2:
                xxx.append(num)
        return xxx


        

        