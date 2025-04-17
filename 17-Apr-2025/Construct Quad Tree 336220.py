# Problem: Construct Quad Tree - https://leetcode.com/problems/construct-quad-tree/description/

class Node:
    def __init__(self, val: int, isLeaf: bool, topleft=None, topRight=None, bottomleft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topleft
        self.topRight = topRight
        self.bottomLeft = bottomleft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(n, r, c):
            allSame = True
            for i in range(n):
                for j in range(n):
                    if grid[r + i][c + j] != grid[r][c]:
                        allSame = False
                        break
                if not allSame:
                    break
            
            if allSame:
                return Node(grid[r][c], True)
            
            n //= 2
            topleft = dfs(n, r, c)
            topright = dfs(n, r, c + n)
            bottomleft = dfs(n, r + n, c)
            bottomright = dfs(n, r + n, c + n)
            return Node(0, False, topleft, topright, bottomleft, bottomright)

        return dfs(len(grid), 0, 0)