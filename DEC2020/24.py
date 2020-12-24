#attempt2:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not(head) or not(head.next):
            return head
        def recurse(head):
            if head and head.next:
                temp=head.next
                head.next=recurse(temp.next)
                temp.next=head
                return temp
            return head
        headc=recurse(head)
        return headc

#attempt1: WA
    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not(head) or not(head.next):
            return head
        headc=head
        while(head and head.next):
            temp=head.next
            temp1=temp.next
            head.next=temp.next
            temp.next=head
            head=temp1
        return headc
            
        
        

