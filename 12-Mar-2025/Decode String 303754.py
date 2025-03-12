# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        for i in range(len(s)):
            if s[i]!="]":
                stack.append(s[i])
            else:
                x=""
                while stack and stack[-1]!="[":
                    x=stack.pop() + x
                stack.pop()
                l=""
                while stack and stack[-1].isdigit():
                    l=stack.pop()+l
                stack.append(int(l)*x)
        return "".join(stack)

        