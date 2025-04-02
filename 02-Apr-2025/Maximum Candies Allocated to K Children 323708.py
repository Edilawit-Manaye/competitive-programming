# Problem: Maximum Candies Allocated to K Children - https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies)<k:
            return 0
        def isValid(c):
            count=0
            for l in candies:
                if l>=c:
                    count+=(l//c)
            return count>=k

        low=1
        high=sum(candies)//k
        res=0
        while low<=high:
            mid=(low+high)//2
            if isValid(mid):
                low=mid+1
                res=mid

            else:
                high=mid-1
        return res
        