# Problem: Implement Queue using Stacks - https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        self.MyQueue=[]
        self.stackkk=[]
        
        
    def push(self, x: int) -> None:
        self.MyQueue.append(x)
        
    def pop(self) -> int:
         if not self.stackkk:
            while self.MyQueue:
                self.stackkk.append(self.MyQueue.pop())
         return self.stackkk.pop()
        
    def peek(self) -> int:
        if not self.stackkk:
            while self.MyQueue:
                self.stackkk.append(self.MyQueue.pop())
        return self.stackkk[-1]
        
    def empty(self) -> bool:
        return max(len(self.MyQueue),len(self.stackkk))==0
        