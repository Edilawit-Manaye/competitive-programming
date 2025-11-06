# Problem: Second Minimum Time to Reach Destination - https://leetcode.com/problems/second-minimum-time-to-reach-destination/

class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        pq = []
        heapq.heappush(pq, (0, 1, 0))
        min_time = [[float('inf'), float('inf')] for _ in range(n + 1)]
        min_time[1][0] = 0
        
        while pq:
            current_time, node, count = heapq.heappop(pq)
            if node == n:
                if count == 1:
                    return current_time
            
            for neighbor in graph[node]:
                wait_time = 0
                if current_time // change % 2 == 1:
                    wait_time = change - (current_time % change)
                
                new_time = current_time + wait_time + time
                
                if new_time < min_time[neighbor][0]:
                    min_time[neighbor][1] = min_time[neighbor][0]
                    min_time[neighbor][0] = new_time
                    heapq.heappush(pq, (new_time, neighbor, 0))
                
                elif min_time[neighbor][0] < new_time < min_time[neighbor][1]:
                    min_time[neighbor][1] = new_time
                    heapq.heappush(pq, (new_time, neighbor, 1))
        
        return -1