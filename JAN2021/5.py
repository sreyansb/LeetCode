#attempt1:keep a copy of the current node and if the copy occurs make the copy of
#the node's next=None and backtrack current node to previous node

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        headc=ListNode(101)
        headc1=headc
        headc1c=headc1
        curvalue=101
        while(head):
            if head.val!=curvalue:
                curvalue=head.val
                headc.next=head
                headc1=headc
                headc=headc.next
            else:
                headc1.next=None
                headc=headc1
            head=head.next
        return headc1c.next
        
