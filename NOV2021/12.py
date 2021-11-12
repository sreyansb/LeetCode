#attempt1:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        headn = ListNode(0)
        headc = headn
        while(head):
            temp = head.next
            if  head.val != val:
                headn.next = head
                headn = headn.next
            head = temp
        headn.next = None
        return headc.next
        
        
