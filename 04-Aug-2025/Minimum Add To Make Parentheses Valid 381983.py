# Problem: Minimum Add To Make Parentheses Valid - https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_count = 0
        result = 0

        for c in s:
            if c=="(":
                open_count+=1
            else:
                if open_count==0:
                    result+=1
                open_count=max(open_count-1,0)
        return result + open_count