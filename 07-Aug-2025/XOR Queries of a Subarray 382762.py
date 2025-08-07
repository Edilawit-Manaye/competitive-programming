# Problem: XOR Queries of a Subarray - https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        pref = [0] * n
        pref[0] = arr[0]
        
        for i in range(1, n):
            pref[i] = pref[i - 1] ^ arr[i]
        
        res = []
        for l, r in queries:
            if l == 0:
                res.append(pref[r])
            else:
                res.append(pref[r] ^ pref[l - 1])
        
        return res
