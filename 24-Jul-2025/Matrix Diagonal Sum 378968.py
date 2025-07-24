# Problem: Matrix Diagonal Sum - https://leetcode.com/problems/matrix-diagonal-sum/description/

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
       sum=0
       row=len(mat)
       col=len(mat[0])
       for r in range(row):
            for c in range(col):
                if r==c or r+c==(row-1):
                    sum+=mat[r][c]
       return sum
