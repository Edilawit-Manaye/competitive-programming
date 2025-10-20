# Problem: Shuffle String - https://leetcode.com/problems/shuffle-string/description/

from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        strrr=[0]*len(s)
        for k in range(len(s)):
            strrr[indices[k]]=s[k]
        return "".join(strrr)

        