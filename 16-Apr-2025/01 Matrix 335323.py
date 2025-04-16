# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(mat), len(mat[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        res = [[float('inf') for _ in range(COLS)] for _ in range(ROWS)]
        zeroes = deque()

        for row in range(ROWS):
            for col in range(COLS):
                if mat[row][col] == 0:
                    res[row][col] = 0
                    zeroes.append((row, col))

        while zeroes:
            row, col = zeroes.popleft()
            for r, c in directions:
                n_row, n_col = row + r, col + c
                if 0 <= n_row < ROWS and 0 <= n_col < COLS and res[n_row][n_col] > res[row][col] + 1:
                    res[n_row][n_col] = res[row][col] + 1
                    zeroes.append((n_row, n_col))

        return res