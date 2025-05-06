# Problem: Satisfiability of Equality Equations - https://leetcode.com/problems/satisfiability-of-equality-equations/

class UnionFind:
    def __init__(self,n):
        self.root=dict()
        self.rank=defaultdict(int)
    def find(self,x):
        if x not in self.root:
            self.root[x]=x
            return x
        while self.root[x]!=x:
            self.root[x]=self.root[self.root[x]]
            x=self.root[x]
        return self.root[x]
    def  union(self,x,y):
       rootx,rooty=self.find(x),self.find(y)
       if rootx==rooty:
            return  
       if self.rank[rootx]>self.rank[rooty]:
           self.root[rooty]=rootx
       elif self.rank[rooty]>self.rank[rootx]:
           self.root[rootx]=rooty
       else:
           self.root[rootx]=rooty
           self.rank[rooty]+=1
      
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        dsu=UnionFind(26)
        for s in equations:
            if s[1]=="=":
                dsu.union(ord(s[0])-ord("a"),ord(s[-1])-ord("a"))
        for s in equations:
            if s[1]=="!" and dsu.find(ord(s[0])-ord("a"))==dsu.find(ord(s[-1])-ord("a")):
                return False
        return True 


        