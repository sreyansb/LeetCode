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
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        di_old_new = {None:None}
        di_new_random = {}
        newlist = Node(0)
        ncopy = newlist
        while(head):
            newlist.next = Node(head.val)
            di_old_new[head] = newlist.next
            newlist = newlist.next
            di_new_random[newlist] = head.random
            head = head.next
        for i in di_new_random:
            i.random = di_old_new[di_new_random[i]]
        return ncopy.next
            
            
            
            
        
