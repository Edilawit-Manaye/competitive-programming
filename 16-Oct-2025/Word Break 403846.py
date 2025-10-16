# Problem: Word Break - https://leetcode.com/problems/word-break/description/

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp=[False]*(len(s)+1)
        dp[len(s)]=True
        n=len(s)
        for i in range(n-1,-1,-1):
            for k in wordDict:
                if i+len(k)<=n  and  s[i:i+len(k)]==k:
                    dp[i]=dp[i+len(k)]
                if dp[i]:
                    break
        return dp[0]
         
        