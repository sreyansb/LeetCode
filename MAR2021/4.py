#attempt1:
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        headA1,l1=headA,0
        headB1,l2=headB,0
        while(headA1):
            l1+=1
            headA1=headA1.next
        while(headB1):
            l2+=1
            headB1=headB1.next
        if l2>l1:
            headA,headB=headB,headA
            l1,l2=l2,l1
        while(l1>l2):
            l1-=1
            headA=headA.next
        ans=None
        while(headA and headA!=headB):
            headA,headB=headA.next,headB.next
        return ans
