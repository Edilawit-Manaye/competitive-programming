# Problem: N-Queens - https://leetcode.com/problems/n-queens/description/

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(row: int):
            if row == n:
                board = []
                for i in range(n):
                    line = ['.'] * n
                    line[queens[i]] = 'Q'
                    board.append("".join(line))
                solutions.append(board)
                return
            
            for col in range(n):
                if col in columns or (row - col) in diagonals1 or (row + col) in diagonals2:
                    continue
                
                columns.add(col)
                diagonals1.add(row - col)
                diagonals2.add(row + col)
                queens[row] = col
                
                backtrack(row + 1)
                
                columns.remove(col)
                diagonals1.remove(row - col)
                diagonals2.remove(row + col)
        
        solutions = []
        columns = set()
        diagonals1 = set()
        diagonals2 = set()
        queens = [0] * n
        
        backtrack(0)
        return solutions