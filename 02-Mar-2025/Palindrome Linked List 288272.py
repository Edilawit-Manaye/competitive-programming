# Problem: Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         res=[]
#         while head:
#             res.append(head.val)
#             head=head.next

#         l,r=0,len(res)-1
#         while l<=r:
#             if res[l]!=res[r]:
#                 return False
#             l+=1
#             r-=1
#         return True 
#   another way 
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        # reverse the second half
        prev=None 
        while slow:
           
           temp=slow.next
           slow.next=prev
           prev=slow
           slow=temp
        left,right =head,prev
        while right:
            if left.val!=right.val:
                return False
            left=left.next
            right=right.next
        return True 






        
        