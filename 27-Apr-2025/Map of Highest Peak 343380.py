# Problem: Map of Highest Peak - https://leetcode.com/problems/map-of-highest-peak/description/

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        queue = deque()
        height = [[-1] * n for _ in range(m)]
        
        for r in range(m):
            for c in range(n):
                if isWater[r][c] == 1:
                    queue.append((r, c))
                    height[r][c] = 0
                    
        
        while queue:
            row, col = queue.popleft()
           
            
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                if 0 <= new_row < m and 0 <= new_col < n and height[new_row][new_col] == -1:
                    height[new_row][new_col] = height[row][col] + 1
                    queue.append((new_row, new_col))
        
        return height