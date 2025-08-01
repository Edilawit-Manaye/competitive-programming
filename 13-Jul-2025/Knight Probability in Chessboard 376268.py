# Problem: Knight Probability in Chessboard - https://leetcode.com/problems/knight-probability-in-chessboard/

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        moves = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]
        
        dp = [[[0] * n for _ in range(n)] for _ in range(k + 1)]
        dp[0][row][column] = 1.0
        
        for step in range(1, k + 1):
            for r in range(n):
                for c in range(n):
                    for dr, dc in moves:
                        prev_r, prev_c = r + dr, c + dc
                        if 0 <= prev_r < n and 0 <= prev_c < n:
                            dp[step][r][c] += dp[step - 1][prev_r][prev_c] / 8.0
        
        total_probability = 0.0
        for r in range(n):
            for c in range(n):
                total_probability += dp[k][r][c]
        
        return total_probability