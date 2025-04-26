# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue=deque()
        row=len(grid)
        col=len(grid[0])
        time,fresh=0,0
        directions=[[-1,0],[0,1],[0,-1],[1,0]]
        for r in range(row):
            for c in range(col):
                if grid[r][c]==1:
                    fresh+=1
                if grid[r][c]==2:
                    queue.append([r,c])
        while queue and fresh>0:
            que_len=len(queue)
            for _ in range(que_len):
                [i,j]=queue.popleft()
                for k,m in directions:
                    new_row,new_col=i+k,m+j
                    if new_row<0 or new_row==row or new_col<0 or new_col==col or grid[new_row] [new_col] !=1:
                        continue
                    grid[new_row][new_col]=2
                    fresh-=1
                    queue.append([new_row,new_col])
            time+=1
        return time if fresh==0 else -1





        