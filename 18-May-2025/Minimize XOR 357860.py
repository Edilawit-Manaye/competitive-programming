# Problem: Minimize XOR - https://leetcode.com/problems/minimize-xor/description/

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        def count_bits(n):
            res = 0
            while n > 0:
                res += n & 1
                n = n >> 1
            return res
        
        cnt1, cnt2 = count_bits(num1), count_bits(num2)
        x = num1
        i = 0
        while cnt1 != cnt2:
            if cnt2 < cnt1 and x & (1 << i):
                cnt1 -= 1
                x ^= (1 << i)
            elif cnt1 < cnt2 and x & (1 << i) == 0:
                cnt1 += 1
                x |= (1 << i)
            i += 1
            
        return x