# Problem: Design Circular Deque - https://leetcode.com/problems/design-circular-deque/

class MyCircularDeque:

    def __init__(self, k: int):
        self.size = k
        self.deque = deque()

    def insertFront(self, value: int) -> bool:
        if len(self.deque) == self.size:
            return False
        self.deque.append(value)
        return True

    def insertLast(self, value: int) -> bool:
        if len(self.deque) == self.size:
            return False
        self.deque.appendleft(value)
        return True
        
    def deleteFront(self) -> bool:
        if len(self.deque) == 0:
            return False
        self.deque.pop()
        return True

    def deleteLast(self) -> bool:
        if len(self.deque) == 0:
            return False
        self.deque.popleft()
        return True

    def getFront(self) -> int:
        if len(self.deque) == 0:
            return -1
        return self.deque[-1]

    def getRear(self) -> int:
        if len(self.deque) == 0:
            return -1
        return self.deque[0]

    def isEmpty(self) -> bool:
        return len(self.deque) == 0

    def isFull(self) -> bool:
        return len(self.deque) == self.size