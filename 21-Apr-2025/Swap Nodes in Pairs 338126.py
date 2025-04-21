# Problem: Swap Nodes in Pairs - https://leetcode.com/problems/swap-nodes-in-pairs/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        prev, cur = dummy, head

        while cur and cur.next:
            next_nodes = cur.next.next
            second_node = cur.next 

            #reverse
            second_node.next = cur
            cur.next = next_nodes
            prev.next = second_node

            #update
            prev = cur
            cur = next_nodes
        
        return dummy.next

