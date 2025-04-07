# Problem: N Queens II - https://leetcode.com/problems/n-queens-ii/

class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row, cols, diags1, diags2):
            if row == n:
                return 1
            count = 0
            for col in range(n):
                if col in cols or (row - col) in diags1 or (row + col) in diags2:
                    continue
                cols.add(col)
                diags1.add(row - col)
                diags2.add(row + col)
                count += backtrack(row + 1, cols, diags1, diags2)
                cols.remove(col)
                diags1.remove(row - col)
                diags2.remove(row + col)
            return count

        return backtrack(0, set(), set(), set())

