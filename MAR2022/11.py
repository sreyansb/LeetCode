#attempt1:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not(head):
            return None
        def findlen(node):
            leng = 0
            while(node):
                leng += 1
                node = node.next
            return leng
        
        n = findlen(head)
        k %= n
        move_forward = n-k
        parent,current = head,head
        while(move_forward):
            parent = current
            current = current.next
            move_forward -= 1
        parentnew = current
        curcopy = current
        while(current):
            parentnew = current
            current = current.next
        if parentnew:
            parent.next = None
            parentnew.next = head
            head = curcopy
        return head
            
            
        
