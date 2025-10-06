# Problem: Frog Jump - https://leetcode.com/problems/frog-jump/

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        dp = defaultdict(set)
        k = stones[1] - stones[0]
        if k > 1:
            return False

        dp[stones[1]].add(k)

        for stone in stones[1:]:
            if stone in dp:
                for jump in dp[stone]:
                    dp[stone + jump].add(jump)
                    if jump > 1:
                        dp[stone + jump - 1].add(jump - 1)
                    dp[stone + jump + 1].add(jump + 1)
        return True if dp[stones[-1]] else False