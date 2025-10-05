# Problem: Champagne Tower - https://leetcode.com/problems/champagne-tower/

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [poured]

        for row in range(1, query_row + 1):
            cur_row = [0] * (row + 1)
            for i in range(row):
                extra = dp[i] - 1
                if extra > 0:
                    cur_row[i] += 0.5 * extra
                    cur_row[i + 1] += 0.5 * extra
            dp = cur_row

        return min(1, dp[query_glass])