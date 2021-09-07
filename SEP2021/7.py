#attempt1:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        prev=None
        while(head):
            temp=head.next
            head.next=prev
            prev=head
            head=temp
        return prev
        