# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        head1=head
        n=0
        arrofnodes=[]
        while(head1):
            n+=1
            arrofnodes.append(head1)
            head1=head1.next
        index=n-1
        k=head
        for i in range(n//2):
            nodein=arrofnodes.pop()
            nodein.next=k.next
            k.next=nodein
            k=nodein.next
        if k:
            k.next=None#very important or we get cycle
