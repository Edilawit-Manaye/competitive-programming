# Problem: Count Good Numbers - https://leetcode.com/problems/count-good-numbers/

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        
       
        if n % 2 == 0:
            E = n // 2
            O = n // 2
        else:
            E = (n // 2) + 1
            O = n // 2
            
        
        def mod_exp(base, exp, mod):
            result = 1
            while exp > 0:
                if exp % 2 == 1:
                    result = (result * base) % mod
                base = (base * base) % mod
                exp //= 2
            return result
        
        even_count = mod_exp(5, E, MOD)
        odd_count = mod_exp(4, O, MOD)
        
       
        return (even_count * odd_count) % MOD