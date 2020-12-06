#attempt1: 88%
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not(root):
            return root
        curlevel=[root]
        while(curlevel):
            nextlevel=[]
            for i in curlevel:
                if i.left:
                    nextlevel.append(i.left)
                if i.right:
                    nextlevel.append(i.right)
            for i in range(len(nextlevel)-1):
                nextlevel[i].next=nextlevel[i+1]
            curlevel=nextlevel
        return root
        
