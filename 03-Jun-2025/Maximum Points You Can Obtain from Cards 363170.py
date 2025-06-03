# Problem: Maximum Points You Can Obtain from Cards - https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total_sum = sum(cardPoints)
        
        if k == n:
            return total_sum
        
        min_sum = float('inf')
        current_sum = 0
        
        for i in range(n - k):
            current_sum += cardPoints[i]
        
        min_sum = current_sum
        
        for i in range(n - k, n):
            current_sum += cardPoints[i] - cardPoints[i - (n - k)]
            min_sum = min(min_sum, current_sum)
        
        return total_sum - min_sum