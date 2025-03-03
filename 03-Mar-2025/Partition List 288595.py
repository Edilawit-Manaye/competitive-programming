# Problem: Partition List - https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left,right=ListNode(),ListNode()
        ltail,rtail=left,right
        while head:
            if head.val<x:
                ltail.next=head
                ltail=ltail.next
            else:
                rtail.next=head
                rtail=rtail.next
            head=head.next
        ltail.next=right.next  # we donnot assign the ltail next point to right because right is dummy node so we must to use  it right.next
        rtail.next=None
        return left.next


            
        