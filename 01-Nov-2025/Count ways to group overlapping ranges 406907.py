# Problem: Count ways to group overlapping ranges - https://leetcode.com/problems/count-ways-to-group-overlapping-ranges/

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP != rootQ:
            if self.rank[rootP] > self.rank[rootQ]:
                self.parent[rootQ] = rootP
            elif self.rank[rootP] < self.rank[rootQ]:
                self.parent[rootP] = rootQ
            else:
                self.parent[rootQ] = rootP
                self.rank[rootP] += 1

class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(ranges)
        ranges.sort()
        uf = UnionFind(n)
        for i in range(n):
            for j in range(i + 1, n):
                if ranges[i][1] < ranges[j][0]:
                    break
                if ranges[i][0] <= ranges[j][1]:
                    uf.union(i, j)
        components = set()
        for i in range(n):
            components.add(uf.find(i))
        k = len(components)
        return pow(2, k, MOD)

