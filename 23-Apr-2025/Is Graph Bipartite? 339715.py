# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph):
        n=len(graph)
        self.color=[-1]*n
        result=True
        for node in range(n):
             if self.color[node]==-1:
                self.color[node]=0
                result=result and self.dfs(graph,node)
        return result
    def dfs(self,graph,node):
        temp=True
        for neighbour in graph[node]:
            if self.color[neighbour]==-1:
                if self.color[node]==0:
                    self.color[neighbour]=1
                else:
                    self.color[neighbour]=0
                temp=temp and self.dfs(graph,neighbour)
            elif self.color[node]==self.color[neighbour]:
                return False
        return temp
        