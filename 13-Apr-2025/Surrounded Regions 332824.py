# Problem: Surrounded Regions - https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows,cols=len(board),len(board[0])
        def dfs(row,col):
            if row<0 or row==rows or col<0 or col==cols or board[row][col]!="O":
                return 
            board[row][col]="T"
            dfs(row+1,col)
            dfs(row-1,col)
            dfs(row,col+1)
            dfs(row,col-1)
        for i in range(rows):
            for j in range(cols):
                if (i in [0,rows-1] or  j in [0,cols-1]) and board[i][j]=="O":
                    dfs(i,j)
        for i in range(rows):
            for j in range(cols):
                if board[i][j]=="O":
                    board[i][j]="X"
        for i in range(rows):
            for j in range(cols):
                if board[i][j]=="T":
                    board[i][j]="O"
                

        