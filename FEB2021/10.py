#attempt1:
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not(head):
            return None
        headc=head
        newhead=Node(0)
        headcc=newhead
        rl=[]
        rll=[]
        headc=head
        while(head):
            rl.append(head)
            headcc.next=Node(head.val)
            headcc=headcc.next
            rll.append(headcc)
            head=head.next
        i=0
        while(headc):
            if headc.random==None:
                rll[i].random=None
            else:
                rll[i].random=rll[rl.index(headc.random)]
            headc=headc.next
            i+=1
        return newhead.next
        
        
        
