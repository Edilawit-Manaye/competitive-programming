# Problem: Repeated DNA Sequences - https://leetcode.com/problems/repeated-dna-sequences/

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen, res = set(), set()
        for i in range(len(s) - 9):
            cur = s[i:i + 10]  # Corrected indexing from 1 to i
            if cur in seen:
                res.add(cur)
            seen.add(cur)
        return list(res)