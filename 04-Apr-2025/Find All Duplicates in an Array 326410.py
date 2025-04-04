# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/



class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # res=[]
        # ab=Counter(nums)
        # for num in nums:
        #     if ab[num]==2 and num not in res:
        #         res.append(num)
        # return res
         count=Counter(nums)
         itemm=count.items()
         res=[]
         for val,num in itemm:
            if num==2:
                res.append(val)
         return res 

             



    
