#attempt2: 94% -> y*2+x == y<<1|x and not y<<1+x
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        initno=0
        while(head):
            initno=initno<<1|head.val
            head=head.next
        return initno
        

#attempt1: 55%
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        initno=0
        while(head):
            initno=initno*2+head.val
            head=head.next
        return initno
        
"""
