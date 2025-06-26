# Problem: People are leaving - https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/A

import sys

class UnionFind:
    def __init__(self, n):
        self.root = list(range(n + 2))

    def find(self, x):
        root_node = x
        while root_node != self.root[root_node]:
            root_node = self.root[root_node]
        
        current_node = x
        while current_node != root_node:
            parent_node = self.root[current_node]
            self.root[current_node] = root_node
            current_node = parent_node
            
        return root_node

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.root[rootX] = rootY

class Solution:
    def solve(self):
        input = sys.stdin.readline
        
        try:
            line = input().strip()
            if not line: return
            n, m = map(int, line.split())
        except (ValueError, IndexError):
            return

        dsu = UnionFind(n)
        
        output_buffer = []
        
        for _ in range(m):
            query = input().split()
            query_type = query[0]
            
            if query_type == '-':
                x = int(query[1])
                dsu.union(x, x + 1)
            elif query_type == '?':
                x = int(query[1])
                nearest_person = dsu.find(x)
                
                if nearest_person > n:
                    output_buffer.append("-1")
                else:
                    output_buffer.append(str(nearest_person))
        
        print("\n".join(output_buffer))

if __name__ == "__main__":
    solution = Solution()
    solution.solve()