#attempt3: Using QUEUE
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        window=deque()
        kc=k
        parent=None
        headc=head
        while(k):
            parent=head
            window.append(parent)
            head=head.next
            k-=1
        #print(parent.next.val)
        ptr=0
        while(head):
            window.append(head)
            head=head.next
            window.popleft()
        #print([i.val for i in window])
        parent.val,window[ptr].val=window[ptr].val,parent.val
        return headc

#attempt2: using a ptr
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        window=[]
        kc=k
        parent=None
        headc=head
        while(k):
            parent=head
            window.append(parent)
            head=head.next
            k-=1
        #print(parent.next.val)
        ptr=0
        while(head):
            window.append(head)
            head=head.next
            ptr+=1
        #print([i.val for i in window])
        parent.val,window[ptr].val=window[ptr].val,parent.val
        return headc
'''

#attempt1:TLE
#dont try to shift arrays based on index like: arr=arr[1:]
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        window=[]
        kc=k
        parent=None
        headc=head
        while(k):
            parent=head
            window.append(parent)
            head=head.next
            k-=1
        #print(parent.next.val)
        while(head):
            window.append(head)
            window=window[1:]
            head=head.next
        #print([i.val for i in window])
        parent.val,window[0].val=window[0].val,parent.val
        return headc
'''
