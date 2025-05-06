# Problem: Find if Path Exists in Graph - https://leetcode.com/problems/find-if-path-exists-in-graph/

class UnionFind:
    def __init__(self):
        self.root=dict()
        self.rank=defaultdict(int)
    def find(self,x):
        if x not in self.root:
            self.root[x]=x
            return x
        while x !=self.root[x]:
            self.root[x]=self.root[self.root[x]]
            x=self.root[x]
        return x
    def union(self ,x,y):
        rootx,rooty=self.find(x),self.find(y)
        if rootx==rooty:
            return 
        rankx,ranky=self.rank[rootx],self.rank[rooty]
        if rankx>ranky:
            self.root[rooty]=rootx
        elif ranky>rankx:
            self.root[rootx]=rooty
        else:
            self.root[rootx]=rooty
            self.rank[rooty]+=1
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        dsu=UnionFind()
        for u,v in edges:
            dsu.union(u,v)
        return dsu.find(source)==dsu.find(destination)

        