#aattempt1:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        final = ListNode()
        cop = final
        while(list1 and list2):
            value = 0
            if list1.val<list2.val:
                value = list1.val
                list1 = list1.next
            else:
                value = list2.val
                list2 = list2.next
            final.next = ListNode(value)
            final = final.next
        while(list1):
            final.next = ListNode(list1.val)
            list1 = list1.next
            final = final.next
        while(list2):
            final.next = ListNode(list2.val)
            list2 = list2.next
            final = final.next
        return cop.next
            
                
        
