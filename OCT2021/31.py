#attempt2: 40ms
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        def recurse(node):
            nodec = node
            while(node):
                if node.child:
                    temp = node.next
                    node.next = recurse(node.child)
                    node.next.prev = node
                    temp1 = node.next
                    while(temp1.next):
                        temp1 = temp1.next
                    node.child = None
                    temp1.next = temp
                    if temp:
                        temp.prev = temp1
                    node = temp
                    
                else:
                    node = node.next
            return nodec
        return recurse(head)
                
        

#attempt1: WA didn't take care of the fact that the current node's next could be 
#none
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        def recurse(node):
            nodec = node
            while(node):
                if node.child:
                    temp = node.next
                    node.next = recurse(node.child)
                    node.next.prev = node
                    temp1 = node.next
                    while(temp1.next):
                        temp1 = temp1.next
                    node.child = None
                    temp1.next = temp
                    if temp:
                        temp.prev = temp1
                    node = temp
                    
                else:
                    node = node.next
            return nodec
        return recurse(head)
'''