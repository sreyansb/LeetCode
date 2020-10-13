#ATTEMPT3: Didnt implement
"""
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
def merge(head,head1):
    if head1==head.next:
        head.val,head1.val=min(head.val,head1.val),max(head.val,head1.val)
        return head
    newone=ListNode(0)
    newcopy=newone
    head1copy=head1
    while(head!=head1copy and head1):
        if head.val>head1.val:
            newone.next=head1
            head1=head1.next
            newone=newone.next
        elif head.val<head1.val:
            newone.next=head
            head=head.next
            newone=newone.next
        else:
            newone.next=head
            head=head.next
            head1=head1.next
            newone=newone.next
    while(head1):
        newone.next=head1
        newone=newone.next
        head1=head1.next
    while(head!=head1copy):
        newone.next=head
        newone=newone.next
        head=head.next
    newone.next=None
    return newcopy
    #head.next=None           
        
def mergesort(head,n):
    if n==2:
        head=merge(head,head.next)
    else:
        mergesort(head,n//2)
        m=n//2+n%2
        headc=head
        while(m):
            m-=1
            headc=headc.next
        mergesort(headc,n-n//2)
        head=merge(head,headc)
        
class Solution:
    def sortList(self, head):
        if not(head) or not(head.next):
            return head
        headc=head
        n=0
        while(headc):
            n+=1
            headc=headc.next
        mergesort(head,n)
        headc=head
        print("done")
        while(headc):
            print(headc.val)
            headc=headc.next
        return head
t1=ListNode(4)
t1.next=ListNode(2)
t1.next.next=ListNode(1)
t1.next.next.next=ListNode(3)
t1.next.next.next.next=None
obj=Solution()
print(obj.sortList(t1))
"""

#ATTEMPT2: TLE using selection sort but constant space
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not(head) or not(head.next):
            return head
        head1=head
        i=head
        while(i):
            k=i
            j=i.next
            while(j):
                if j.val<k.val:
                    k=j
                j=j.next
            i.val,k.val=k.val,i.val
            i=i.next
        return head1
"""              
                
#Attempt1: AC without using constant space()
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not(head):
            return head
        arr=[]
        while(head):
            arr.append(head.val)
            head=head.next
        arr.sort()
        head=ListNode(arr[0])
        head1=head
        for i in arr[1:]:
            head.next=ListNode(i)
            head=head.next
        return head1
"""     
