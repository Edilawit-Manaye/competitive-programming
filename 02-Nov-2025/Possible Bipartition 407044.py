# Problem: Possible Bipartition - https://leetcode.com/problems/possible-bipartition/

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        grap = defaultdict(list)
        for u, v in dislikes:
            grap[u].append(v)
            grap[v].append(u)
        colors = [-1] * (n + 1) 
        def dfs(i):
            for neigh in grap[i]:
                if colors[neigh]!=-1:
                    if colors[i]==colors[neigh]:
                        return False
                else:
                    colors[neigh]=1-colors[i]
                    if not dfs(neigh):
                        return False
            return True 
        for i in range(1,n+1):
            if colors[i]==-1:
                colors[i]=0
                if not dfs(i):
                    return False
        return True 


    
            