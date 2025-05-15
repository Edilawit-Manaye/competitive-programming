# Problem: Counting Bits - https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> List[int]:
        def count_bit(num):
            count=0
            for i in range(32):
                shifted=1<<i
                res=num & shifted
                if res:
                    count+=1
            return count

        ans=[0]*(n+1)
        for  num in range(n+1):
            ans[num]=count_bit(num)
            
        return ans 


        