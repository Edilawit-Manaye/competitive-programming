# Problem: Min Cost to Connect All Points - https://leetcode.com/problems/min-cost-to-connect-all-points/

class UnionFind:
    def __init__(self,n):
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
    def manhattan(self,p:list[int],q:list[int]) ->int:
        return abs(p[0]-q[0])+abs(p[1]-q[1])

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
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        dsu=UnionFind(len(points))
        min_heap=[]
        for i in range(len(points)):
            for j in range(1,len(points)):
                distance=dsu.manhattan(points[i],points[j])
                heappush(min_heap,(distance,i,j))
        min_edge=0
        min_weight=0
        while min_heap:
            weight,u,v=heappop(min_heap)
            if dsu.find(u)!=dsu.find(v):
                dsu.union(u,v)
                min_weight+=weight
                min_edge+=1
                if min_edge==len(points)-1:
                    break
        return min_weight



        
        