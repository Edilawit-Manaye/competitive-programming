# Problem: Divide intervals into minimum number of groups - https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        min_heap = []
        
        for start, end in intervals:
            if min_heap and start > min_heap[0]:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, end)
        
        return len(min_heap)

