# Problem: Removing Stars From a String - https://leetcode.com/problems/removing-stars-from-a-string/

class Solution:
    def removeStars(self, s: str) -> str:
        stack=[]
        for c in s:
            if stack and c=="*":
                stack.pop()
            else :
                stack.append(c)
        return "".join(stack)
                
        