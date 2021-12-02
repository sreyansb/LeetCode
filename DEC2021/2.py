#attempt1:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odds = ListNode()
        s = odds
        odde = odds
        evens = ListNode()
        es = evens
        odd = 1
        while(head):
            temp = head.next
            if odd:
                odds.next = head
                odds.next.next = None
                odde = odds.next
                odds = odds.next
            else:
                evens.next = head
                evens.next.next = None
                evens = evens.next
                #print(evens.val)
            odd ^= 1
            head = temp
        if odde:
            odde.next = es.next
        return s.next
            
            
