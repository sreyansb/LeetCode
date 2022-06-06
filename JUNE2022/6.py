#attempt1:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def findlength(node):
            length_of_list = 0
            while(node):
                length_of_list += 1
                node = node.next
            return length_of_list
        length_listA, length_listB = findlength(headA), findlength(headB)
        if length_listA < length_listB:
            length_listA,length_listB = length_listB,length_listA
            headA,headB = headB,headA
        for i in range(length_listA-length_listB):
            headA = headA.next
        while(headA and headB and headA!=headB):
            headA,headB = headA.next,headB.next
        return headA
            
