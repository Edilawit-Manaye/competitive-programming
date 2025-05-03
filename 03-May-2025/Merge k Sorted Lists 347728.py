# Problem: Merge k Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for arr in lists:
            head = arr
            while head:
                heapq.heappush(heap, head.val)
                head = head.next

        dummy = ListNode()
        head = dummy

        for i in range(len(heap)):
            head.next = ListNode(heapq.heappop(heap))
            head = head.next

        return dummy.next