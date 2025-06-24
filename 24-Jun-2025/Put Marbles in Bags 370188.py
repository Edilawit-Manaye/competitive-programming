# Problem: Put Marbles in Bags - https://leetcode.com/problems/put-marbles-in-bags/

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1:
            return 0
        
        splits = []
        for i in range(len(weights) - 1):
            splits.append(weights[i] + weights[i + 1])
        
        splits.sort()
        max_score = sum(splits[-(k - 1):])
        min_score = sum(splits[:k - 1])
        
        return max_score - min_score