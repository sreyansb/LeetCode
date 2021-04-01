#attempt2: TOOK HELP: reverse 2nd half (after finding mid) and check
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast=head
        slow=head
        while(fast and fast.next):
            fast=fast.next.next
            slow=slow.next
        prev=ListNode()
        middie=slow
        while(slow):
            temp=slow.next
            slow.next=prev
            prev=slow
            slow=temp
        while(head!=middie and prev):
            if head.val!=prev.val:
                return False
            head=head.next
            prev=prev.next
        return True

#attempt1:O(n) and O(n)
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        arr=[]
        while(head):
            arr.append(head.val)
            head=head.next
        low,high=0,len(arr)-1
        flag=1
        while(low<=high):
            if arr[low]!=arr[high]:
                flag=0
                break
            low+=1
            high-=1
        return flag==1
'''
