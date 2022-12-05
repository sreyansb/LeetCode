#attempt1:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = None
        while(fast):
            slow = slow.next if slow else head
            if fast.next:
                fast = fast.next.next
            else:
                return slow
        return slow.next
            
