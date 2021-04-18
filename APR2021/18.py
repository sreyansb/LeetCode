#attempt1:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        window=deque([])
        leng=0
        parent=None
        number=0
        headc=head
        while(head):
            number+=1
            if leng==n:
                parent=window.popleft()
                leng-=1
            window.append(head)
            leng+=1
            head=head.next
        if number==n:
            headc=headc.next
            return headc
        parent.next=parent.next.next
        return headc
            
        
