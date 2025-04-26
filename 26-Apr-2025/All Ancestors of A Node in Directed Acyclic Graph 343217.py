# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph=defaultdict(list)
        indgree=[0]*n
        for a,b in edges:
            graph[a].append(b)
            indgree[b]+=1
        queue=deque()
        for i in range(n):
            if indgree[i]==0:
                queue.append(i)
        res={i:set() for i in range(n)}
        while queue:
            node=queue.popleft()
            for neigh in graph[node]:
                res[neigh] |= res[node]
                res[neigh].add(node)
                indgree[neigh]-=1
                if indgree[neigh]==0:
                    queue.append(neigh)
        return [sorted(list(arr)) for  arr in res.values()]


        