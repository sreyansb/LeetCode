#attempt1: 93%
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        i=0
        j=0
        newhead=ListNode()
        headc=newhead
        while(l1 and l2):
            if l1.val<l2.val:
                newhead.next=l1
                l1=l1.next
            else:
                newhead.next=l2
                l2=l2.next
            newhead=newhead.next
        while(l1):
            newhead.next=l1
            newhead=newhead.next
            l1=l1.next
        while(l2):
            newhead.next=l2
            newhead=newhead.next
            l2=l2.next
        return headc.next
            
            
        
