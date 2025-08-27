# Problem: Richest Customer Wealth - https://leetcode.com/problems/richest-customer-wealth/description/

from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # return max(sum(i) for i in accounts)
        arrrr=[]
        for i in accounts:
            x=sum(i)
            arrrr.append(x)
        return max(arrrr)
        

        
        
       
        

