# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        odds=ListNode(0)
        evens=ListNode(0)
        oddhead=odds
        evenhead=evens
        isodd=True
        while(head):
            if isodd:
                odds.next=head
                odds=odds.next
            else:
                evens.next=head
                evens=evens.next
            isodd=not(isodd)
            head=head.next
        odds.next=evenhead.next
        evens.next=None
        return oddhead.next
        
            
        
