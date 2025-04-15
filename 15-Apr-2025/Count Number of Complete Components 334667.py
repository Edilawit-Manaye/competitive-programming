# Problem: Count Number of Complete Components - https://leetcode.com/problems/count-the-number-of-complete-components/

class Solution:
    def countCompleteComponents(self, n, edges):
        graph = defaultdict(list)
        visited = [False] * n
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node):
            visited[node] = True
            nodes = 1
            edges_count = 0
            for neighbor in graph[node]:
                edges_count += 1
                if not visited[neighbor]:
                    n_nodes, n_edges = dfs(neighbor)
                    nodes += n_nodes
                    edges_count += n_edges
            return nodes, edges_count

        complete_components = 0
        for i in range(n):
            if not visited[i]:
                nodes, edges_count = dfs(i)
                if edges_count == nodes * (nodes - 1):
                    complete_components += 1

        return complete_components