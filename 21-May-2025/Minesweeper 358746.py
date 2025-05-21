# Problem: Minesweeper - https://leetcode.com/problems/minesweeper/

class Solution:
    def find_mines(self,board,x,y):
        num_mines=0
        for r in range(x-1,x+2):
            for c in range(y-1,y+2):
                if 0<=r<len(board) and 0<=c<len(board[0]) and  board[r][c]=="M":
                    num_mines+=1
        return num_mines
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if not board:
            return board
        x,y=click
        if board[x][y]=="B" or  board[x][y].isdigit():
            return board
        if board[x][y]=="M":
            board[x][y]="X"
        else:
            mines=self.find_mines(board,x,y)
            if mines:
                board[x][y]=str(mines)
            else:
                board[x][y]="B"
                for r in range(x-1,x+2):
                      for c in range(y-1,y+2):
                         if 0<=r<len(board) and 0<=c<len(board[0]) and  board[r][c]=="E":
                            self.updateBoard(board,[r,c])
        return board


            
            

        
    