#attempt2: 91% and 20%
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        di={}
        while(head):
            if head in di:
                return True
            di[head]=1
            head=head.next
        return False

#attempt1:15% and 39%
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow=head
        fast=head
        flag=0
        while(slow and fast and fast.next):
            if flag and slow==fast:
                return True
            slow=slow.next
            fast=fast.next.next
            flag+=1
        return False
'''
