# Problem: Valid Parentheses - https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        map={")":"(","]":"[","}":"{"}
        stack=[]
        for k in s:
            if k in map.values():
                stack.append(k)
            elif k in map.keys(): 
                if not stack or stack[-1]!=map[k]:
                    return False
                else:
                    stack.pop()
        return not stack
        