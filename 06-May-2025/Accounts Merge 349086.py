# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dsu=UnionFind(len(accounts))
        emailToAccount={}
        for i ,e in enumerate(accounts):
            for email in e[1:]:
                if email in emailToAccount:
                    dsu.union(i,emailToAccount[email])
                else:
                    emailToAccount[email]=i
        emailMerge=defaultdict(list)
        for email,i in emailToAccount.items():
            leader=dsu.find(i)
            emailMerge[leader].append(email)
        res=[]
        for i ,y in emailMerge.items():
            name=accounts[i][0]
            res.append([name]+sorted(y))
        return res 



        

    


    
    