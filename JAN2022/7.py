#attempt3: TOOK HELP
#Reservoir Sampling - When length of linked list is too huge as in a stream and
#we can't push into an array
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from random import random,randint,choice
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
            
    def getRandom(self) -> int:
        current_ele = self.head.val
        nexthead = self.head.next
        curi = 2
        while(nexthead):
            if random()<1/curi:
                current_ele = nexthead.val
            curi += 1
            nexthead = nexthead.next
        return current_ele
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()

#attempt2: 84ms

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from random import randint,choice
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.values = []
        self.leng = 0
        while(head):
            self.values.append(head.val)
            self.leng += 1
            head = head.next
            
    def getRandom(self) -> int:
        return choice(self.values)
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()

#attempt1: 156ms
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from random import randint
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.values = []
        self.leng = 0
        while(head):
            self.values.append(head.val)
            self.leng += 1
            head = head.next
            
    def getRandom(self) -> int:
        return self.values[randint(0,self.leng-1)]
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
'''
