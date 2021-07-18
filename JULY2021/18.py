#attempt3:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        node=head
        arr=[None]
        while(node):
            arr.append(node)
            node=node.next
        n=len(arr)-1
        count=n//k
        i=1
        cur=1
        prev=1
        while(cur<=count):
            arr[prev:cur*k+1]=arr[prev:cur*k+1][::-1]
            prev=cur*k+1
            cur+=1
        #print(arr)
        for i in range(1,n):
            arr[i].next=arr[i+1]
        arr[-1].next=None
        return arr[1]
        

#attempt2: last node's next wasn't grounded
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        node=head
        arr=[None]
        while(node):
            arr.append(node)
            node=node.next
        n=len(arr)-1
        count=n//k
        i=1
        cur=1
        prev=1
        while(cur<=count):
            arr[prev:cur*k+1]=arr[prev:cur*k+1][::-1]
            prev=cur*k+1
            cur+=1
        #print(arr)
        for i in range(1,n):
            arr[i].next=arr[i+1]
        return arr[1]
'''

#attempt1:Wrong idea prev should be kth node and not None
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        node=head
        kcopy=k
        prev=None
        parent,tobereversed=None,head
        while(node):
            temp=node.next
            node.next=prev
            prev=node
            kcopy-=1
            if kcopy==0:
                kcopy=k
                tobereversed=temp
                parent=node
            node=temp
        while(tobereversed):
            temp=tobereversed.next
            tobereversed.next=parent
            parent=tobereversed
            tobereversed=temp
        
        return head
'''