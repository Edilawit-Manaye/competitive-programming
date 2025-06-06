# Problem: Boats to Save People - https://leetcode.com/problems/boats-to-save-people/

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l,r=0,len(people)-1
        res=0
        while l<=r:
            remain=limit-people[r]
            r-=1
            res+=1
            if  l<=r and remain>=people[l]:
                l+=1
        return  res
        