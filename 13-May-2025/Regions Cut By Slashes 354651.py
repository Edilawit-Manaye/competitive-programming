# Problem: Regions Cut By Slashes - https://leetcode.com/problems/regions-cut-by-slashes/description/

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
            
   
        # Type hints
        # :type grid: List[str]
        # :rtype: int
        roots = {}

        def find(x):
            if x not in roots:
                roots[x] = x
            if x != roots[x]:
                roots[x] = find(roots[x])  # Path compression
            return roots[x]

        def union(x, y):
            roots[find(x)] = find(y)

        length = len(grid)
        for i in range(length):
            for j in range(length):
                if grid[i][j] == '/':
                    union((i, j, 'N'), (i, j, 'W'))
                    union((i, j, 'S'), (i, j, 'E'))
                elif grid[i][j] == '\\':
                    union((i, j, 'N'), (i, j, 'E'))
                    union((i, j, 'S'), (i, j, 'W'))
                else:  # Empty space
                    union((i, j, 'N'), (i, j, 'E'))
                    union((i, j, 'S'), (i, j, 'W'))
                    union((i, j, 'N'), (i, j, 'S'))


                if j > 0:
                    union((i, j - 1, 'E'), (i, j, 'W'))
                if i > 0:
                    union((i - 1, j, 'S'), (i, j, 'N'))

        return len(set(find(x) for x in roots))

