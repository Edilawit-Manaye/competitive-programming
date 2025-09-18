# Problem: Water Bottles - https://leetcode.com/problems/water-bottles/description

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        maxDrink=numBottles
        while numExchange<=numBottles:
            numBottles= numBottles-numExchange
            numBottles+=1
            maxDrink+=1
        return maxDrink



        