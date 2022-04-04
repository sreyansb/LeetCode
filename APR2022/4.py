# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        parentoffirstk = None
        knodeswindow = deque([]) 
        headc = head
        for i in range(k-1):
            knodeswindow.append(headc)
            headc = headc.next
        parentoffirstk = headc
        if headc:
            knodeswindow.append(headc)
            headc = headc.next
        while(headc):
            knodeswindow.popleft()
            knodeswindow.append(headc)
            headc = headc.next
        if not parentoffirstk:
            return head
        parentoffirstk.val,knodeswindow[0].val = knodeswindow[0].val,parentoffirstk.val
        return head
            
        
        
