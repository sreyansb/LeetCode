# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        headp=head
        while(head):
            headval=head
            headnext=head.next
            while(headnext):
                if headval.val>headnext.val:
                    headval=headnext
                headnext=headnext.next
            if head!=headval:
                head.val,headval.val=headval.val,head.val
            head=head.next
        return headp
                
