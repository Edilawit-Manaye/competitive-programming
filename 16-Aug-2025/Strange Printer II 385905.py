# Problem: Strange Printer II - https://leetcode.com/problems/strange-printer-ii/

class Solution:
    def isPrintable(self, targetGrid: list[list[int]]) -> bool:
        bounds = {}
        for r, row in enumerate(targetGrid):
            for c, color in enumerate(row):
                if color not in bounds:
                    bounds[color] = [r, r, c, c]
                else:
                    b = bounds[color]
                    b[0] = min(b[0], r)
                    b[1] = max(b[1], r)
                    b[2] = min(b[2], c)
                    b[3] = max(b[3], c)

        graph = {color: set() for color in bounds}
        for u_color, (min_r, max_r, min_c, max_c) in bounds.items():
            for r in range(min_r, max_r + 1):
                for c in range(min_c, max_c + 1):
                    v_color = targetGrid[r][c]
                    if v_color != u_color:
                        graph[v_color].add(u_color)

        states = {color: 0 for color in bounds}

        def has_cycle(color):
            states[color] = 1

            for neighbor in graph[color]:
                if states[neighbor] == 1:
                    return True
                if states[neighbor] == 0:
                    if has_cycle(neighbor):
                        return True
            
            states[color] = 2
            return False

        for color in bounds:
            if states[color] == 0:
                if has_cycle(color):
                    return False
        
        return True