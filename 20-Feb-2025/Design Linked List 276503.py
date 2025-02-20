# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class Node():
    def __init__(self, val= 0):
        self.val = val
        self.next = None


class MyLinkedList():

    def __init__(self):
        self.head = None

    def get(self, index):
        curr = self.head
        count = 0
        while curr and count < index:
            count += 1
            curr = curr.next
        if curr:
            return curr.val
        return -1

    def addAtHead(self,val):
        node = Node(val)
        node.next = self.head
        self.head = node
      
    def addAtTail(self, val):
        node=Node(val)
        curr = self.head
        if not curr:
            self.head=node
            return
        while curr.next:
            curr=curr.next
        curr.next=node

    def addAtIndex(self, index, val):
        dummy = Node()
        dummy.next = self.head
        count = 0
        curr = dummy
        while count < index and curr:
            curr = curr.next
            count += 1

        node = Node(val)
        if curr:
            node.next = curr.next
            curr.next = node
            self.head = dummy.next


    def deleteAtIndex(self, index):
        dummy = Node()
        count = 0
        dummy.next = self.head
        curr = dummy

        while count < index and curr.next:
            curr = curr.next
            count += 1
        if curr.next:
            curr.next = curr.next.next
        self.head = dummy.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
