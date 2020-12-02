#attempt1:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from random import randint
class Solution:

    def __init__(self, head: ListNode):
        self.head=head
        
    def getRandom(self) -> int:
        x=self.head
        n=0
        while(x):
            n+=1
            x=x.next
        index=0
        n=randint(0,n-1)
        x=self.head
        while(n):
            x=x.next
            n-=1
        return x.val
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
