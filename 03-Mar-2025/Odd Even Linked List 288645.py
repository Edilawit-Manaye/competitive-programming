# Problem: Odd Even Linked List - https://leetcode.com/problems/odd-even-linked-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head 
        odd=head
        even=even_head=head.next
        
        
        while even and even.next:
            odd.next=even.next
            odd=odd.next
            even.next=odd.next  # this odd.next the odd word is is modified in the second line while loop
            even=even.next
        odd.next=even_head
        return head 

        