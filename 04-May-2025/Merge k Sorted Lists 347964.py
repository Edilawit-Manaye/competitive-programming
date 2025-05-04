# Problem: Merge k Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
       heap=[]
       for i,node in enumerate(lists):
          if node:
            heappush(heap,(node.val,i,node))
       dummy=ListNode()
       cur=dummy
       while heap:
          val,i,node=heappop(heap)
          cur.next=node
          cur=node
          node=node.next
          if node:
             heappush(heap,(node.val,i,node))
       return  dummy.next

            