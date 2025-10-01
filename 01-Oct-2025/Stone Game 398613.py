# Problem: Stone Game - https://leetcode.com/problems/stone-game/

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo={}
        def dp(l,r):
            if (l,r) in memo:
                return memo[(l,r)]
            if l>r:
                return 0
            even=True if (r-l)%2 else False
            left=piles[l] if even else 0
            right=piles[r]if even else 0
            memo[(l,r)]= max((dp(l+1,r)+left) , (dp(l,r-1)+right))
            return memo[(l,r)]
        alice_max_value=dp(0,len(piles)-1)
        return alice_max_value > sum(piles)/2
             

            