#attempt1: 84ms
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        arr = []
        while(head):
            arr.append(head)
            head = head.next
        start = 0
        end = len(arr)-1
        newh = ListNode()
        newhc = newh
        while(1):
            
            newh.next = arr[start]
            newh = newh.next
            #print(newh.next.val)
            start += 1
            if (start<=end):
                newh.next = arr[end]
                #print(newh.next.val)
                end -= 1
                newh = newh.next
            if start>end:
                break
            
        newh.next = None
        return newhc.next
                
            
        
