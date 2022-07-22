#attempt1:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lesser = ListNode()
        lesserc = lesser
        greaterEqual = ListNode()
        greaterEqualc = greaterEqual
        while(head):
            nextnode = head.next
            if head.val<x:
                lesser.next = head
                lesser.next.next = None
                lesser = lesser.next
            else:
                greaterEqual.next = head
                greaterEqual.next.next = None
                greaterEqual = greaterEqual.next
            head = nextnode
        lesser.next = greaterEqualc.next
        return lesserc.next
        
            
        
