# Problem: Check if All Characters Have Equal Number of Occurrences - https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/description/

from collections import Counter

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        k = Counter(s)
        m = set(k.values())
        return len(m) == 1
        
        

     
