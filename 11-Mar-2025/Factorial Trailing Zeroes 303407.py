# Problem: Factorial Trailing Zeroes - https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    def trailingZeroes(self, n: int) -> int:
        def factorial(n):
            if n==1 or n==0:
                return 1
            return n*factorial(n-1)
        fact_n=factorial(n)
        count=0
        while fact_n % 10==0:
            count+=1
            fact_n//=10
        return count


      
        



