# Problem: Find the Substring With Maximum Cost - https://leetcode.com/problems/find-the-substring-with-maximum-cost/

class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        best = 0
        lookup = {}

        for i in range(26):
            lookup[chr(i + ord('a'))] = i + 1

        for c, v in zip(chars, vals):
            lookup[c] = v

        current = 0

        for c in s:
            current += lookup.get(c, 0)
            if current < 0:
                current = 0
            best = max(best, current)

        return best