# Problem: Find the Substring With Maximum Cost - https://leetcode.com/problems/find-the-substring-with-maximum-cost/

class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        lookUp = {}
        for i in range(26):
            lookUp[chr(i + ord("a"))] = i + 1
        
        for c, val in zip(chars, vals):
            lookUp[c] = val
        
        current = 0
        max_cost = float('-inf')

        for c in s:
            current += lookUp.get(c, 0)
            max_cost = max(max_cost, current)
            if current < 0:
                current = 0
        
        return max_cost if max_cost > 0 else 0