# Problem: Time Needed to Inform All Employees - https://leetcode.com/problems/time-needed-to-inform-all-employees/

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph=defaultdict(list)
        for i,val in enumerate(manager):
            graph[val].append(i)
        queue=deque()
        queue.append((headID,0))
        res=0
        while queue:
            node,time=queue.popleft()
            res=max(res,time)
            for neigh in  graph[node]:
                queue.append((neigh,time+informTime[node]))
        return res
        