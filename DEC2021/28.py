#attempt1:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        count = 0
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        if fast and fast.next:
            slow = slow.next
        return slow
