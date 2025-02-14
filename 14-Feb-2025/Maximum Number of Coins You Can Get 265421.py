# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n=len(piles)//3
        res=0   
        piles.sort(reverse=True)
        for i in range(1,2*n,2):
            res+=piles[i]
        return res 


      
        