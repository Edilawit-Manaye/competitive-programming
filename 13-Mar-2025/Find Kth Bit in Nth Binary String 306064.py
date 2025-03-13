# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(n):
           return  "".join(["0" if c=="1" else "1" for c in n])
        def res(n):   # n as an index
            if n==1:
               return "0"
            x=res(n-1)
            return x + "1"+ "".join(reversed(invert(x)))
        result=res(n)
        return result[k-1]
