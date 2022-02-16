#attempt1:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not(head) or not(head.next):
            return head
        prev = head
        cur = head.next
        while(cur):
            prev.val,cur.val = cur.val,prev.val
            if cur.next and cur.next.next:
                prev = cur.next
                cur = prev.next
            else:
                cur = None
        return head
        
