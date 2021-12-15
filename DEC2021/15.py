#attempt1:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        headc = head
        prev = headc
        while(head):
            temp = head.val
            prev = headc
            while(prev!=head):
                if prev.val>temp:
                    prev.val,head.val = head.val,prev.val
                prev = prev.next
            head=head.next
        return headc
            
