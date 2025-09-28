# Problem: Solving Questions With Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * n
        for i in range(len(questions)-1,-1,-1):
            dp[i]=dp[i+1] if i+1 <n else 0
            next_step=i+questions[i][1]+1
            if next_step <n:
                dp[i]=max(dp[i],dp[next_step]+questions[i][0])
            else:
                dp[i]=max(dp[i],questions[i][0])
        return dp[0]
