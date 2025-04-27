# Problem: Time Needed to Inform All Employees - https://leetcode.com/problems/time-needed-to-inform-all-employees/

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph=defaultdict(list)
        for i,val in enumerate(manager):
            graph[val].append(i)
        ans=0
        def dfs(node,cur_time):
           nonlocal ans
           ans=max(ans,cur_time)
           for child in graph[node]:
                dfs(child,cur_time + informTime[node])
        dfs(headID,0)
        return ans

        