#attempt2:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not(head):
            return False
        slow = head
        fast = head
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            if slow==fast:
                return True
        return False

#attempt1: WA because check has to be at the end of the loop
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not(head):
            return False
        slow = head
        fast = head
        while(fast and fast.next):
            if slow==fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False
        
'''
