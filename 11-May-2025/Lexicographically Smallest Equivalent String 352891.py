# Problem: Lexicographically Smallest Equivalent String - https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

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
        self.root[rootx]=self.root[rooty]=min(rootx,rooty)
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        res=[]
        dsu=UnionFind()
        for u,v in zip(s1,s2):
            dsu.union(u,v)
        for c in baseStr:
            res.append(dsu.find(c))
        return "".join(res)

        