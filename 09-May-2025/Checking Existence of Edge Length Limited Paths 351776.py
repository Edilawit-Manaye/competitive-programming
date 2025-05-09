# Problem: Checking Existence of Edge Length Limited Paths - https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        parent = list(range(n))

        def find(i: int) -> int:
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]

        def union(i1: int, i2: int) -> bool:
            root1 = find(i1)
            root2 = find(i2)
            if root1 != root2:
                parent[root1] = root2
                return True
            return False

        edgeList.sort(key=lambda x: x[2])

        augmented_queries = []
        for i, query_tuple in enumerate(queries):
            p, q, limit = query_tuple
            augmented_queries.append((limit, p, q, i))

        augmented_queries.sort()

        ans = [False] * len(queries)
        edge_idx = 0
        num_edges = len(edgeList)

        for path_limit, p, q, original_query_idx in augmented_queries:
            while edge_idx < num_edges and edgeList[edge_idx][2] < path_limit:
                u, v, _ = edgeList[edge_idx]
                union(u, v)
                edge_idx += 1

            if find(p) == find(q):
                ans[original_query_idx] = True

        return ans