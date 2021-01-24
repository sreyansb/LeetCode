#attempt2:
from heapq import heappush,heappop
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        ele=[]
        for i in lists:
            j=i
            while(j):
                heappush(ele,j.val)
                j=j.next
        head=ListNode()
        k=head
        while(ele):
            k.next=ListNode(heappop(ele))
            k=k.next
        return head.next

#attempt1:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        final=[]
        for i in lists:
            j=i
            while(j!=None):
                final.append(j.val)
                j=j.next
        final.sort()
        k=ListNode()
        head=k
        for i in final:
            k.next=ListNode(i)
            k=k.next            
        return head.next
'''       
