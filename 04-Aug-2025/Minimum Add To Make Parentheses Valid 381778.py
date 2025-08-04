# Problem: Minimum Add To Make Parentheses Valid - https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_cnt = 0
        result = 0

        for c in s:
            if c == "(":
                open_cnt += 1
            else:
                open_cnt -= 1
            
            if open_cnt < 0:
                result += 1
                open_cnt = 0

        return result + open_cnt