# Problem: Most Stones Removed with Same Row or Column - https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

class UnionFind:
    def __init__(self,n):
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
    def removeStones(self, stones: List[List[int]]) -> int:
        rows,cols={},{}
        dsu=UnionFind(len(stones))
        for i in range(len(stones)):
            r,c=stones[i]
            if r in rows:
                prev_element=rows[r]
                dsu.union(i,prev_element)
            else:
                rows[r]=i
            if c in cols:
                prev_element=cols[c]
                dsu.union(i,prev_element)
            else:
                cols[c]=i
        s=set()
        for i in range(len(stones)):
            parent=dsu.find(i)
            s.add(parent)
        return len(stones)-len(s)
