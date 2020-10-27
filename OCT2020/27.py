#attempt2: SLow and fast pointer
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not(head) or head==head.next:
            return head
        slow=head
        fast=head
        number=1
        #ends at the tail or the element before the tail, cant say
        while(slow and fast and fast.next):
            
            #print(slow.val,fast.val)
            if slow==fast and number==0:
                #print(slow.val)
                break
            number=0
            parent=slow
            slow=slow.next
            fast=fast.next.next
        if slow!=fast or number:
            return None
        #this will take us to the closest element in the list
        while(head!=fast):
            head=head.next
            fast=fast.next
        return head
            
        

#attempt1: 84%
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        s=set()
        while(head):
            if head in s:
                return head
            s.add(head)
            head=head.next
        return None
"""
