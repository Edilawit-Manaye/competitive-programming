# Problem: Minimum Time to Repair Cars - https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def isValid(time) :
            n=0
            for i in ranks:
                n+=int((time/i)**0.5)
            return n>=cars

        l=0
        high=2**50
        while l<=high:
            mid=(l+high)//2
            if isValid(mid):
                high=mid-1
            else:
                l=mid+1
        return l 
    
        