# Problem: 01 Knapsack - https://www.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1

class Solution:
    def knapsack(self, W, val, wt) -> int:
        n = len(val)
        dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(W + 1):
                if wt[i - 1] <= j:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - wt[i - 1]] + val[i - 1])
                else:
                    dp[i][j] = dp[i - 1][j]
        
        return dp[n][W] 

