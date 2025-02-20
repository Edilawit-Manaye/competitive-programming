# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # dummy=ListNode(0,head)
        # right=head
        # left=dummy
        # while right and n>0:
        #     right=right.next
        #     n-=1
        # while right:
        #     left=left.next
        #     right=right.next
        # left.next=left.next.next
        # return dummy.next
## or another implementation
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        right = dummy
        count = 0
        while count < n:
            right = right.next
            count += 1

        #the left pointer will be initialized and bothe pointers will be moved one step ahead
        left = dummy
        while right.next:
            left = left.next
            right = right.next
        left.next = left.next.next

        return dummy.next

