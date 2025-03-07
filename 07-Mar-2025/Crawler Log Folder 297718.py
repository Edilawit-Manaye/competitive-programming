# Problem: Crawler Log Folder - https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
       stack=[]
       for c in logs:
         if c=="./":
            continue
         elif stack and c=="../":
            stack.pop()
         elif c!="../":
            stack.append(c)
       return  len(stack)
        