# Problem: Daily Temperatures - https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        stack=[]
        for i,val  in enumerate(temperatures):
            while stack and val >stack[-1][0]:
                stack_val,stack_index=stack.pop()
                res[stack_index]=i-stack_index
            stack.append([val,i])
        return res 
            


