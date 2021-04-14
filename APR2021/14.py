#attempt1
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        smaller=ListNode()
        smallc=smaller
        larger=ListNode()
        largec=larger
        while(head):
            if head.val<x:
                smaller.next=head
                smaller=smaller.next
            else:
                larger.next=head
                larger=larger.next
            head=head.next
        larger.next=None
        smaller.next=largec.next
        head=smallc.next
        return head
        
        
        
