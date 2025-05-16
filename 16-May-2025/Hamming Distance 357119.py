# Problem: Hamming Distance - https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        k=x^y
        count=0
        for i in range(32):
            shifted=1<<i
            res=shifted & k
            if res:
                count+=1
        return count 

        