# Problem: Count the Number of Complete Components - https://leetcode.com/problems/count-the-number-of-complete-components/

class Solution(object):
    def countCompleteComponents(self, n, edges):
        """
        """
        def dfs(v,path):
            if v in path:
                return
            path.add(v)
            visited.add(v)
            for u in graph[v]:
                dfs(u,path)
        
        visited = set()
        component = 0
        graph = defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        for i in range(n):
            if i not in visited:
                path = set()
                dfs(i,path)
                size = len(path)-1
                for j in path:
                    if len(graph[j])!=size: break
                else: component += 1
            
        return component
                