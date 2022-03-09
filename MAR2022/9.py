#attempt1:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newlist = ListNode()
        copynewlist = newlist
        while(head):
            ele = head.val
            head = head.next
            cop = head
            while(head and head.val == ele):
                head = head.next
            if head==cop:
                newlist.next = ListNode(ele)
                newlist = newlist.next
        return copynewlist.next
                
        
