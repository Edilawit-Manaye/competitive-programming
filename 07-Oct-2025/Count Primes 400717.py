# Problem: Count Primes - https://leetcode.com/problems/count-primes/

class Solution:
    def countPrimes(self, n: int) -> int:
        is_Prime=[True] * n
        if n<=1:
            return 0
        is_Prime[0]=False
        is_Prime[1]=False
        i=2
        while  i*i<=n:
            if is_Prime[i]:
                j=i*i
                while j< n:
                     is_Prime[j]=False
                     j+=i
            i+=1
        count=0
        for i in range(len(is_Prime)):
            if is_Prime[i]==True:
                count+=1
        return count

                


        