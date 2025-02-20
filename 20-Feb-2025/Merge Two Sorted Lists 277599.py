# Problem: Merge Two Sorted Lists - https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to simplify the merging process
        dummy = ListNode(0)
        current = dummy
        
        # While both lists have nodes to compare
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            
            # Move the current pointer forward
            current = current.next
        
        # If one of the lists is not exhausted, append it
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
        
        # Return the merged list, which starts at the next of the dummy node
        return dummy.next