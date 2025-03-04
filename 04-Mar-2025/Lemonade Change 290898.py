# Problem: Lemonade Change - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five ,ten=0,0
        for i in range(len(bills)):
            if bills[i]==5:
                five+=1
            elif bills[i]==10:
                ten+=1
            change=bills[i]-5
            if change==5:
                if five>0:
                    five-=1
                else:
                    return  False
            if change==15:
                if five>0 and ten>0 :
                    five-=1
                    ten-=1
                elif five >=3:
                    five-=3
                else:
                    return False 
        return True 