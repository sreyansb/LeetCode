#attempt2:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        def reverse(leftNode,rightNode):
            prev = rightNode.next
            while(leftNode != rightNode):
                nextNode = leftNode.next
                leftNode.next = prev
                prev = leftNode
                leftNode = nextNode
            rightNode.next = prev
            return rightNode
        
        index = 1
        headc = head
        leftNode = None
        rightNode = None
        leftNodeParent = None
        while(index < right):
            if index == left-1:
                leftNodeParent = head
            index += 1
            head = head.next
        rightNode = head
        if leftNodeParent:
            leftNodeParent.next = reverse(leftNodeParent.next,rightNode)
        else:
            headc = reverse(headc,rightNode)
        return headc
                
                

#attempt1: 75 ms
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        index = 1
        stack = []
        headc = head
        while(index <= right):
            if index >= left:
                stack.append(head)
            head = head.next
            index += 1
        start = 0
        end = len(stack)-1
        while(start < end):
            stack[start].val,stack[end].val = stack[end].val,stack[start].val
            start += 1
            end -= 1
        return headc
                
