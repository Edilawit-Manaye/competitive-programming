# Problem: Counting Bits - https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[0]*(n+1)
        for i in range(n+1):
            num=int.bit_count(i)
            ans[i]=num
        return ans 


        