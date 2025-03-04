# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        prev=points[0]
        n=len(points)
        for i in range(1,len(points)):
            curr=points[i]
            if curr[0] <=prev[1]:
                n-=1
                prev=[curr[0],min(prev[1],curr[1])]
            else:
                prev=curr
        return n

            
        
            



        