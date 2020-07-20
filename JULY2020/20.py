#FASTEST SOLUTION:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return None
        k=head
        li=[]
        while(head):
            if head.next and head.next.val==val:
                li.append(head)
            head=head.next
        if not(li):
            if k.val==val:
                k=k.next
            return k
        else:
            for i in li[::-1]:
                i.next=i.next.next
            if k.val==val:
                k=k.next
            return k

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return None
        k=head
        li=[]
        while(head):
            if head.next and head.next.val==val:
                li.append(head)
            head=head.next
        for i in li[::-1]:
            i.next=i.next.next
        if k.val==val:
            k=k.next
        return k
"""        
        
