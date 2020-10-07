#attempt3: 55% and 30%
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not(head):
            return head
        headc=head
        n=0
        while(headc):
            headc=headc.next
            n+=1
        k=k%n
        newhead=ListNode(0)
        newheadc=newhead
        index=0
        while(index<n-k):
            newhead.next=ListNode(head.val)
            newhead=newhead.next
            head=head.next
            index+=1
        newhead.next=None
        newpre=ListNode(0)
        newprec=newpre
        index=n-k
        while(index<n):
            index+=1
            newpre.next=ListNode(head.val)
            newpre=newpre.next
            head=head.next
        newpre.next=newheadc.next
        return newprec.next

#attempt2: 55% and 50%
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        arr=[]
        headc=head
        if not(head):
            return head
        while(headc):
            arr.append(headc.val)
            headc=headc.next
        n=len(arr)
        k=k%n
        index=n-k
        headc=ListNode(0)
        headz=headc
        while(index<n):
            headc.next=ListNode(arr[index])
            headc=headc.next
            index+=1
        index=0
        while(index<n-k):
            headc.next=ListNode(arr[index])
            headc=headc.next
            index+=1
        headc.next=None
        return headz.next
"""

#attempt1: 93% and 15%
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        arr=[]
        headc=head
        if not(head):
            return head
        while(headc):
            arr.append(headc.val)
            headc=headc.next
        n=len(arr)
        k=k%n
        arr=arr[n-k:]+arr[:n-k]
        headc=ListNode(arr[0])
        headz=headc
        for i in arr[1:]:
            headc.next=ListNode(i)
            headc=headc.next
        headc.next=None
        return headz
"""     
