# Problem: Maximal Square - https://leetcode.com/problems/maximal-square/

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        if not matrix or not matrix[0]:
            return 0

        ROWS, COLS = len(matrix), len(matrix[0])
        cache = {}  

        def helper(r, c):
            if r >= ROWS or c >= COLS:
                return 0
            if (r, c) in cache:
                return cache[(r, c)]

            down = helper(r + 1, c)
            right = helper(r, c + 1)
            diag = helper(r + 1, c + 1)

            if matrix[r][c] == "1":
                cache[(r, c)] = 1 + min(down, right, diag)
            else:
                cache[(r, c)] = 0
            
            return cache[(r, c)]

        helper(0, 0)

        
        return max(cache.values()) ** 2