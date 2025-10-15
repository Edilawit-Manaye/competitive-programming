# Problem: Shuffle String - https://leetcode.com/problems/shuffle-string/description/

from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        strr=[0]*len(s)
        for k in range(len(s)):
            strr[indices[k]]=s[k]
        return "".join(strr)

        