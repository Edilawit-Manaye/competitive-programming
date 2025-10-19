# Problem: Longest Common Prefix - https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
       res=""
       for i in range(len(strs[0])):
            for m in strs:
                if i==len(m) or m[i]!=strs[0][i]:
                    return res
            res+=strs[0][i]
       return res