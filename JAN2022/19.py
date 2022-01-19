#attempt1: NAive solution. Didn't understand the good approach
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = set()
        index = 0
        while(head):
            if head in visited:
                return head
            visited.add(head)
            #index += 1
            head = head.next
        return None
            
        
