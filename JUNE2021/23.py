#attempt1:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        headc=head
        i=1
        parent=None
        while(i<left):
            parent=head
            head=head.next
            i+=1
        headg=head
        i=right-left
        parentg=None
        while(i):
            parentg=headg
            headg=headg.next
            i-=1
        def reverse(newnext,head,headg):
            end=newnext
            while(head!=end):
                temp=head.next
                head.next=newnext
                newnext=head
                head=temp
            return newnext
        newnext=headg.next
        if parent:
            parent.next=reverse(newnext,head,headg)
        else:
            headc=reverse(newnext,head,headg)
        return headc