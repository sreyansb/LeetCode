#attempt1:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
        def findlength(head):
            n=0
            while(head):
                n+=1
                head=head.next
            return n
        n=findlength(head)
        eachmin,extra=n//k,n%k
        arr=[]
        curlen=0
        curhead=head
        while(k):
            curnode=ListNode()
            filler=curnode
            for i in range(eachmin):
                filler.next=curhead
                curhead=curhead.next
                filler=filler.next
            if extra:
                filler.next=curhead
                filler=filler.next
                extra-=1
                curhead=curhead.next
            if filler:
                filler.next=None
            arr.append(curnode.next)
            k-=1
        return arr
            
                
        