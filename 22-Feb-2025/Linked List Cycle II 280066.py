# Problem: Linked List Cycle II - https://leetcode.com/problems/linked-list-cycle-ii/

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        slow=fast=head
        temp = None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                temp = slow
                break
        if not temp:
            return None
        while head:
            if temp == head:
                break
            head = head.next
            temp = temp.next
        return temp
            
            
        