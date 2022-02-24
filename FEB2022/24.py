#attempt1:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        eles = []
        while(head):
            eles.append(head.val)
            head = head.next
        eles.sort()
        newone = ListNode()
        newc = newone
        for i in eles:
            newone.next = ListNode(i)
            newone = newone.next
        return newc.next
