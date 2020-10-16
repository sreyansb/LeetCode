#Attempt1: 66% and 100% very important condition

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not(head) or not(head.next) or m>n:
            return head
        i=1
        headc=head
        parentm=None
        while(i<m):
            parentm=head
            head=head.next
            i+=1
        headco=head
        prev=None
        while(i<=n):
            temp=head.next
            head.next=prev
            prev=head
            head=temp
            i+=1
        headco.next=head
        if parentm:
            parentm.next=prev
        else:
            return prev
        return headc
        
        
