# Problem: Checking Existence of Edge Length Limited Paths - https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

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
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        dsu=UnionFind()
        edgeList.sort(key=lambda x:x[2])
        q=[]
        for i in range(len(queries)):
            u,v,limit=queries[i]
            q.append([limit,u,v,i])
        q.sort()
        edge_index=0
        res=[False]*len(queries)
        for k in range(len(q)):
            limitt,p,l,i=q[k]

            while  edge_index<len(edgeList) and edgeList[edge_index][2]<limitt:
                u,v,_=edgeList[edge_index]
                
                dsu.union(u,v)
                edge_index+=1
            if dsu.find(p)==dsu.find(l):
                res[i]=True
        return res



        