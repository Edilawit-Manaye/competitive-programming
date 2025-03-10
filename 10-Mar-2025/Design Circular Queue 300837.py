# Problem: Design Circular Queue - https://leetcode.com/problems/design-circular-queue/

class ListNode:
    def __init__(self, val=0, nxt=None, prev=None):
        self.val = val
        self.next = nxt
        self.prev = prev

class MyCircularQueue:
    def __init__(self, k: int):
        self.space = k
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        cur = ListNode(value)
        cur.prev = self.right.prev
        cur.next = self.right
        self.right.prev.next = cur
        self.right.prev = cur
        self.space -= 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.left.next = self.left.next.next
        self.left.next.prev = self.left
        self.space += 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.left.next.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.right.prev.val

    def isEmpty(self) -> bool:
        return self.left.next == self.right

    def isFull(self) -> bool:
        return self.space == 0