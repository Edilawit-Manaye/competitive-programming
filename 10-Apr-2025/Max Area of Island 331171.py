# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        max_area = 0
        
        def dfs(x, y):
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 0:
                return 0
            
            grid[x][y] = 0
            area = 1
            area += dfs(x + 1, y)
            area += dfs(x - 1, y)
            area += dfs(x, y + 1)
            area += dfs(x, y - 1)
            return area
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    current_area = dfs(i, j)
                    max_area = max(max_area, current_area)
        
        return max_area