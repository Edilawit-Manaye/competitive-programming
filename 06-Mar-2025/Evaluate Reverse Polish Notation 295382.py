# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
     def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i=="+":
                stack.append(stack.pop()+stack.pop())
            elif i=="*":
                stack.append(stack.pop()*stack.pop())
            elif i=="-":
                b=stack.pop()
                a=stack.pop()
                stack.append(a-b)
            elif i=="/":
                b=stack.pop()
                a=stack.pop()
                stack.append(int(a/b))
            else:
                stack.append(int(i)) 
        return stack[0]
        

