# Problem: Minimum Path Sum - https://leetcode.com/problems/minimum-path-sum/description/

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        dp=[[float("inf")]*(col+1) for i in range(row+1)]
        dp[row-1][col]=0 
        for i in range(len(grid)-1,-1,-1):
           for j in range(len(grid[0])-1,-1,-1):
                   dp[i][j]=grid[i][j]+min(dp[i+1][j],dp[i][j+1])
        return dp[0][0]
        