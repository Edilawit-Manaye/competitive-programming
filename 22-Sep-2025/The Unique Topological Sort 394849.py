# Problem: The Unique Topological Sort - https://basecamp.eolymp.com/en/problems/10652

from collections import defaultdict, deque

def unique_topological_sort(n, edges):
    adj = defaultdict(list)
    in_degree = [0] * (n + 1)

    for u, v in edges:
        adj[u].append(v)
        in_degree[v] += 1

    q = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            q.append(i)

    topological_order = []

    while q:
        if len(q) > 1:
            return "NO"

        u = q.popleft()
        topological_order.append(u)

        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                q.append(v)

    if len(topological_order) != n:
        return -1
    else:
        return "YES"
n, m = map(int, input().split())
edges = []
for _ in range(m):
    u, v = map(int, input().split())
    edges.append((u, v))

print(unique_topological_sort(n, edges))