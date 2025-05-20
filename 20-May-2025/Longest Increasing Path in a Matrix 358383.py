# Problem: Longest Increasing Path in a Matrix - https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = {}

        def dfs(r, c, preVal):
            if r < 0 or r == rows or c < 0 or c == cols or matrix[r][c] <= preVal:
                return 0
            
            if (r,c) in dp:
                return dp[(r,c)]
            
            dp[(r, c)] = 1 + max(
                        dfs(r + 1, c, matrix[r][c]),
                        dfs(r - 1, c, matrix[r][c]),
                        dfs(r, c + 1, matrix[r][c]),
                        dfs(r, c - 1, matrix[r][c])
                            )
            return dp[(r, c)]
            
        for i in range(rows):
            for j in range(cols):
                dfs(i, j, -1)
        return max(dp.values())