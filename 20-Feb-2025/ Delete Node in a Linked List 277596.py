# Problem:  Delete Node in a Linked List - https://leetcode.com/problems/delete-node-in-a-linked-list/


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node: ListNode) -> None:
        # Copy the value from the next node to the current node
        node.val = node.next.val
        # Bypass the next node
        node.next = node.next.next