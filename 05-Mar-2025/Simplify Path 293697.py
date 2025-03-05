# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        cur = ""
        for c in path + "/":
            if c == "/":
                if cur == "":
                    continue
                if cur == "..":
                    if stack:
                        stack.pop()
                elif cur != ".":
                    stack.append(cur)
                cur = ""
            else:
                cur += c
        return "/" + "/".join(stack) if stack else "/"