# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def isCapacity(capacity):
            sum=0
            day=1           
            for i in weights:
                sum+=i
                if sum>capacity:
                    day+=1
                    sum=i
            return day<=days
        low=max(weights)
        high=sum(weights)
        while low<= high:
            mid=(low+high)//2
            if isCapacity(mid):
                high=mid-1
            else:
                low=mid+1
        return low 
        