# Problem: Spanning Tree - https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/E

from collections import defaultdict
class UnionFind:
    def __init__(self):
        self.root = {}
        self.rank = defaultdict(int)

    def find(self, x):
        if x not in self.root:
            self.root[x] = x
            return x
        while x != self.root[x]:
            self.root[x] = self.root[self.root[x]]
            x = self.root[x]
        return self.root[x]  

    def union(self, x, y):
        rootx, rooty = self.find(x), self.find(y)
        if rootx == rooty:
            return
        rankx, ranky = self.rank[rootx], self.rank[rooty]
        if rankx > ranky:
            self.root[rooty] = rootx
        elif ranky > rankx:
            self.root[rootx] = rooty
        else:
            self.root[rootx] = rooty
            self.rank[rooty] += 1

class Solution:
    def solve():
        n,m=map(int,input().split())
        edge=[]
        for _ in range(m):
            b,e,w=map(int,input().split())
            edge.append((w,b,e))
        edge.sort()
        dsu=UnionFind()
        num_edge=0
        num_weight=0
        for w,b,e in edge:
            if dsu.find(b)!=dsu.find(e):
                dsu.union(b,e)
                num_edge+=1
                num_weight+=w
        print(num_weight)
    solve()


        
        