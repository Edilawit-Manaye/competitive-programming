# Problem: Decode Ways - https://leetcode.com/problems/decode-ways/

# class Solution:
#     def numDecodings(self, s: str) -> int:
#         # using bottom up approach
#         n=len(s)
#         dp=[0]*(n+1)
        
#         dp[n]=1
#         for i in range(n-1,-1,-1):
#             if s[i]=="0":
#                 dp[i]=0
#             else:
#                 dp[i]=dp[i+1]
#             if i+1<n and (s[i]=="1" or (s[i]=="2" and  s[i+1] in "0123456")):
#                     dp[i]+=dp[i+2]
#         return dp[0]
#         # using top down

class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        memo={len(s):1}
        def dp(i):
            if i in memo:
                return memo[i]
            if s[i]=="0":
                return 0
            else:
                res=dp(i+1)
            if i+1<n and (s[i]=="1" or (s[i]=="2" and  s[i+1] in "0123456")):
                     res+=dp(i+2)
            memo[i]=res
            return memo[i]
        return dp(0)

            
            



