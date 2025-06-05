# Problem: longest-substring-without-repeating-characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ab=set()
        l=0
        max_len=0
        for r in range(len(s)):
            while s[r] in ab:
                ab.remove(s[l])
                l+=1
            ab.add(s[r])
            max_len=max(max_len,r-l+1)
            
            
        return max_len
            

        