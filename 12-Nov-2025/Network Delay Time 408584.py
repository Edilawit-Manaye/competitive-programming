# Problem: Network Delay Time - https://leetcode.com/problems/network-delay-time/description/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph=[[] for i in range(n+1)]
        for i,j,m in times:
            graph[i].append((j,m))
        distance=[float("inf")] * (n+1)
        distance[k]=0
        queue=[(0,k)]
        while queue:
            dist,node=heapq.heappop(queue)
            for child,time in graph[node]:
                new_distance=dist + time
                if new_distance < distance[child]:
                    distance[child]=new_distance
                    heapq.heappush(queue,(new_distance,child))
        return max(distance[1:]) if max(distance[1:]) != float("inf") else -1










# import heapq
# from typing import List

# class Solution:
#     def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
#         # Step 1: Create the graph as an adjacency list
#         graph = [[] for _ in range(n + 1)]
#         for u, v, time in times:
#             graph[u].append((v, time))

#         # Step 2: Initialize distances and a priority queue
#         distance = [float("inf")] * (n + 1)
#         distance[k] = 0  # Distance to the starting node is 0
#         queue = [(0, k)]  # Start processing with (distance, node)

#         while queue:
#             dist, node = heapq.heappop(queue)  # Get the node with the smallest distance

#             # Step 3: Process each neighbor of the current node
#             for child, time in graph[node]:
#                 new_distance = dist + time  # Calculate the new distance
                
#                 # Step 4: If the new distance is shorter, update the distance and add to the queue
#                 if new_distance < distance[child]:
#                     distance[child] = new_distance
#                     heapq.heappush(queue, (new_distance, child))

#         # Step 5: Find the maximum distance from the distance array,
#         # ignoring the distance for index 0 (since nodes start from 1)
       