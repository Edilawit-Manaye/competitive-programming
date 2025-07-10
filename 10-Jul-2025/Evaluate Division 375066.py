# Problem: Evaluate Division - https://leetcode.com/problems/evaluate-division/

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj=defaultdict(list)
        for i ,equ in enumerate(equations):
            a,b=equ
            adj[a].append((b,values[i]))  # value[i]-> indicates weight between a and b 
            adj[b].append((a,1 / values[i]) )
        def bfs(src,target):
            if src not in adj or target not in adj:
                return -1
            queue=deque([])
            queue.append((src,1))
            visited=set([src])
            while queue:
                n,w=queue.popleft()
                if n==target:
                    return w
                for (neigh,weight) in adj[n]:
                    if neigh not in visited:
                        queue.append((neigh,w * weight))
                        visited.add(neigh)
            return -1
        return [bfs(q[0],q[1]) for q in queries]

            



        