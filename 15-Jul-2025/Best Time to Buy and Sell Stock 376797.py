# Problem: Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self,prices:list[int])->int:
        l,r,maxP=0,1,0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit=prices[r]-prices[l]
                maxP=max(maxP,profit)
            else:
                l=r
            r+=1
        return maxP




        