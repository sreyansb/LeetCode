#attempt2: 88ms
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        
        newlist = ListNode()
        copynewlist = newlist
        
        while(l1 and l2):
            ele = (l1.val+l2.val+carry)
            carry = ele//10
            newlist.next = ListNode(ele%10)
            l1 = l1.next
            l2 = l2.next
            newlist = newlist.next
        if l2:
            l1 = l2
        while(l1):
            ele = (l1.val+carry) if l1 else l2
            carry = ele//10
            newlist.next = ListNode(ele%10)
            l1 = l1.next
            newlist = newlist.next
        if carry:
            newlist.next = ListNode(carry)
        return copynewlist.next

#attempt1: 97ms
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        
        newlist = ListNode()
        copynewlist = newlist
        
        while(l1 and l2):
            ele = (l1.val+l2.val+carry)
            carry = ele//10
            newlist.next = ListNode(ele%10)
            l1 = l1.next
            l2 = l2.next
            newlist = newlist.next
        
        while(l1):
            ele = (l1.val+carry)
            carry = ele//10
            newlist.next = ListNode(ele%10)
            l1 = l1.next
            newlist = newlist.next
        while(l2):
            ele = (l2.val+carry)
            carry = ele//10
            newlist.next = ListNode(ele%10)
            l2 = l2.next
            newlist = newlist.next
        if carry:
            newlist.next = ListNode(carry)
        return copynewlist.next
