# Problem: Remove Max Number of Edges to Keep Graph Fully Traversable - https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/

class UnionFind:
    def __init__(self, n: int):
        self.root = list(range(n + 1))
        self.components = n

    def find(self, x: int) -> int:
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x: int, y: int) -> int:
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.root[rootY] = rootX
            self.components -= 1
            return 1
        return 0

    def is_connected(self) -> bool:
        return self.components == 1

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: list[list[int]]) -> int:
        alice = UnionFind(n)
        bob = UnionFind(n)
        kept_edges = 0

        for t, u, v in edges:
            if t == 3:
                if alice.union(u, v) | bob.union(u, v):
                    kept_edges += 1
        
        for t, u, v in edges:
            if t == 1:
                if alice.union(u, v):
                    kept_edges += 1
            elif t == 2:
                if bob.union(u, v):
                    kept_edges += 1

        if alice.is_connected() and bob.is_connected():
            return len(edges) - kept_edges
        
        return -1