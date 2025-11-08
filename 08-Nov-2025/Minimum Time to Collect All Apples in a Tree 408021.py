# Problem: Minimum Time to Collect All Apples in a Tree - https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/description/

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = {i: [] for i in range(n)}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node, parent):
            total_time = 0
            for neighbor in graph[node]:
                if neighbor != parent:
                    time = dfs(neighbor, node)
                    if time > 0 or hasApple[neighbor]:
                        total_time += time + 2
            return total_time

        return dfs(0, -1)

