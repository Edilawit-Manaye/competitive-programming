# Problem: Score of Parentheses - https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = []
        
        for char in S:
            if char == '(':
                stack.append(0) 
            else:
               
                last = stack.pop()
                if last == 0:
                    
                    score = 1
                else:
                    
                    score = 2 * last
               
                if stack:
                    stack[-1] += score
                else:
                    stack.append(score)  
        return stack[0] if stack else 0 

