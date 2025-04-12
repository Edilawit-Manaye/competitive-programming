# Problem: Employee Importance - https://leetcode.com/problems/employee-importance/

"""

class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        dictt=dict()
        for emp in employees:
            dictt[emp.id]=emp
        visited=set()
        importance=0
        def dfs(emp):
            nonlocal importance 
            visited.add(emp)
            if  emp.id>=id:
                importance+=emp.importance
            for subordinate in emp.subordinates:
                 if subordinate not in visited:
                    dfs(dictt[subordinate])
        dfs(dictt[id])
        return importance 
            
                      

                 


        

        