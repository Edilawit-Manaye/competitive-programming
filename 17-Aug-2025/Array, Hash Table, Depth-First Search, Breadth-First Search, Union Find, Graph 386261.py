# Problem: Array, Hash Table, Depth-First Search, Breadth-First Search, Union Find, Graph - https://leetcode.com/problems/minimize-malware-spread/

class Solution:
    def minMalwareSpread(self, graph, initial):
        n = len(graph)
        
        class UnionFind:
            def __init__(self, n):
                self.parent = list(range(n))
                self.size = [1] * n

            def find(self, i):
                if self.parent[i] == i:
                    return i
                self.parent[i] = self.find(self.parent[i])
                return self.parent[i]

            def union(self, i, j):
                root_i = self.find(i)
                root_j = self.find(j)
                if root_i != root_j:
                    if self.size[root_i] < self.size[root_j]:
                        root_i, root_j = root_j, root_i
                    self.parent[root_j] = root_i
                    self.size[root_i] += self.size[root_j]

        uf = UnionFind(n)
        for i in range(n):
            for j in range(i + 1, n):
                if graph[i][j] == 1:
                    uf.union(i, j)

        component_infection_count = collections.Counter(uf.find(i) for i in initial)
        
        max_saved_size = -1
        result_node = -1
        
        initial.sort()

        for node_to_remove in initial:
            root = uf.find(node_to_remove)
            
            if component_infection_count[root] == 1:
                component_size = uf.size[root]
                if component_size > max_saved_size:
                    max_saved_size = component_size
                    result_node = node_to_remove

        if result_node == -1:
            return initial[0]
            
        return result_node