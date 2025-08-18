# Problem: Circumference of a Tree - https://codeforces.com/gym/102694/problem/A

import sys
from collections import defaultdict, deque
input = sys.stdin.readline
def bfs(start_node, graph):
    queue = deque([(start_node, 0)])
    visited = {start_node}
    farthest_node = start_node
    max_distance = 0

    while queue:
        current_node, distance = queue.popleft()

        if distance > max_distance:
            max_distance = distance
            farthest_node = current_node

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))
    return farthest_node, max_distance
n_str = input()
if n_str.strip():
    n = int(n_str)

    if n <= 1:
        print(0)
    else:
        graph = defaultdict(list)
        for _ in range(n - 1):
            u, v = map(int, input().split())
            graph[u].append(v)
            graph[v].append(u)
        endpoint_a, _ = bfs(1, graph)
        _, diameter = bfs(endpoint_a, graph)
        print(3 * diameter)