# Problem: Check if There is a Valid Path in a Grid - https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        ports = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)]
        }
        
        visited = set()

        def dfs(r, c):
            if r == m - 1 and c == n - 1:
                return True
            
            visited.add((r, c))
            
            current_street = grid[r][c]
            
            for dr, dc in ports[current_street]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                    next_street = grid[nr][nc]
                    if (-dr, -dc) in ports[next_street]:
                        if dfs(nr, nc):
                            return True
            
            return False

        return dfs(0, 0)

# class Solution:
#     def hasValidPath(self, grid: List[List[int]]) -> bool:
#         m, n = len(grid), len(grid[0])
        
#         ports = {
#             1: [(0, -1), (0, 1)], 2: [(-1, 0), (1, 0)], 3: [(0, -1), (1, 0)],
#             4: [(0, 1), (1, 0)], 5: [(0, -1), (-1, 0)], 6: [(0, 1), (-1, 0)]
#         }
        
#         queue = collections.deque([(0, 0)])
#         visited = set([(0, 0)])
        
#         while queue:
#             r, c = queue.popleft()
            
#             if r == m - 1 and c == n - 1:
#                 return True
            
#             current_street = grid[r][c]
            
#             for dr, dc in ports[current_street]:
#                 nr, nc = r + dr, c + dc
                
#                 if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
#                     next_street = grid[nr][nc]
#                     if (-dr, -dc) in ports[next_street]:
#                         visited.add((nr, nc))
#                         queue.append((nr, nc))
                        
#         return False