# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow=head
        fast=head
        prev=None
        while fast and fast.next:
            tmp=slow.next
            fast=fast.next.next
            slow.next=prev
            prev=slow
            slow=tmp
        res=0
        while slow:
            res=max(res,slow.val+prev.val)
            slow=slow.next
            prev=prev.next
        return res 



        
       
            

        