# Problem: Number of 1 Bits - https://leetcode.com/problems/number-of-1-bits/description/

class Solution:
    def hammingWeight(self, n: int) -> int:
        c=0
        for i in range(32):
            shifted=1<<i
            res=shifted & n
            if res:
                c+=1
        return c

        