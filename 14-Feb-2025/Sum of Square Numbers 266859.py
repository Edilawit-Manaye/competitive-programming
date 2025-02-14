# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l,r=0,int(sqrt(c))
        while l<=r:
            total=l*l +r*r
            if total>c:
                r-=1
            elif total<c:
                l+=1
            else:
                return True 

        return False 