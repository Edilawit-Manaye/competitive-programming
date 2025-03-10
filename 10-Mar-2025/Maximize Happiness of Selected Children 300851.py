# Problem: Maximize Happiness of Selected Children - https://leetcode.com/problems/maximize-happiness-of-selected-children/?envType=daily-question&envId=2024-05-09

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        max_heap = [-i for i in happiness]
        heapq.heapify(max_heap)
        max_happiness = 0
        
        for i in range(k):
            max_happiness += max(-heapq.heappop(max_heap) - i, 0)
        
        return max_happiness