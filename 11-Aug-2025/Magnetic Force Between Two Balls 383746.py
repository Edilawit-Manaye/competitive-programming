# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort() 
        left = 0
        right = position[-1]
        def good(x):
            start = -1e100 
            count = 0
            for p in position:
                if p - start >= x:
                    start = p
                    count += 1
            return count >= m
        res=-1
        while left <= right:
             mid=(left+right)//2
             if good(mid):
                res=mid
                left=mid+1
             else:
                right=mid-1
        return res

                

