#attempt1:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry=0
        parent=None
        head=l1
        while(l1 and l2):
            parent=l1
            k=l1.val+l2.val+carry
            l1.val=k%10
            carry=k//10
            l1=l1.next
            l2=l2.next
        if l1:
            while(l1):
                parent=l1
                k=(l1.val+carry)
                l1.val=k%10
                carry=k//10
                l1=l1.next
            if carry:
                parent.next=ListNode(carry)
            return head
        while(l2):
            k=(l2.val+carry)
            parent.next=ListNode(k%10)
            carry=k//10
            l2=l2.next
            parent=parent.next
        if carry:
            parent.next=ListNode(carry)
        return head
            
            
            
        
