# Problem: Maximum Sum With at Most K Elements - https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/description/

class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
       n,m=len(grid),len(grid[0])
       for row in grid:
           row.sort(reverse=True)
       heap=[]
       for i in range(n):
          row=grid[i]
          for j in range(limits[i]):
             heappush(heap,row[j])
       while len(heap)>k:
           heappop(heap)
       return sum(heap)
              