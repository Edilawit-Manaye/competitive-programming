# Problem: Richest Customer Wealth - https://leetcode.com/problems/richest-customer-wealth/description/

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        res=0
        maxx=0
        
        r=len(accounts)
        k=len(accounts[0])
        for i in range(r):
            for j in range(k):
                
                maxx+=accounts[i][j]
            res=max(res,maxx)
            maxx=0
        return res
            
        
        

        
        
       
        

