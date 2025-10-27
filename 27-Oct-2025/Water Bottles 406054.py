# Problem: Water Bottles - https://leetcode.com/problems/water-bottles/description

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        maxDri=numBottles
        while numExchange<=numBottles:
            numBottles= numBottles-numExchange
            numBottles+=1
            maxDri+=1
        return maxDri



        