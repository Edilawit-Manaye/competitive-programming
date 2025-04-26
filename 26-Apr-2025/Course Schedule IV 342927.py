# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph=defaultdict(list)
        indgree=[0]*numCourses
        for i,j in prerequisites:
            graph[i].append(j)
            indgree[j]+=1
        queue=deque()
        
        for i in range(numCourses):
            if indgree[i]==0:
                queue.append(i)
        dp=[[False]*numCourses for _ in range(numCourses)]
        while queue:
            node=queue.popleft()
            for neigh in graph[node]:
                dp[node][neigh]=True
                for i in range(numCourses):
                    dp[i][neigh]|= dp[i][node]
                indgree[neigh]-=1
                if indgree[neigh]==0:
                    queue.append(neigh)
        return [dp[u][v] for u,v in queries]



        
       