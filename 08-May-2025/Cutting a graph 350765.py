# Problem: Cutting a graph - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/D

from collections import defaultdict
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
    def checker(self,u,v):
        return self.find(u)==self.find(v)
def solve():
    n,m,k=map(int,input().split())
    dsu=UnionFind(n)
    for _ in range(m):
        input()
    queries=[]
    for _ in range(k):
        strr=input().split()
        queries.append(strr)
    res=[]
    for query_element in queries[::-1]:
        first_element=query_element[0]
        if first_element=="ask":
           if  dsu.checker(int(query_element[1]),int(query_element[2])):
               res.append("YES")
           else:
               res.append("NO")
        else:
            dsu.union(int(query_element[1]),int(query_element[2]))
    for ele in reversed(res):
        print(ele)
solve()
               

        


    