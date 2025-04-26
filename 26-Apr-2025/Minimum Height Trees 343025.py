# Problem: Minimum Height Trees - https://leetcode.com/problems/minimum-height-trees/

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph=defaultdict(list)
        indgree=[0]*n
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
            indgree[a]+=1
            indgree[b]+=1
        queue=deque(i for i,v in enumerate(indgree) if v==1)
        res=[]
        while queue:
            res=list(queue)
            for _ in range(len(queue)):
                node=queue.popleft()
                for neigh in graph[node]:
                    indgree[neigh]-=1
                    if indgree[neigh]==1:
                        queue.append(neigh)
        return res if res else list(range(n)) 