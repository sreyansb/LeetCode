#attempt3: TOOK HELP : recursion To set the right child's next: you need to know the
#next of the parent and the next of right child = next of parent ka left child
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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def setnext(node,rightnode):
            if node:
                #print(node.val,node,rightnode)
                node.next = rightnode
                leftright = None
                if node.right:
                    leftright = node.right
                setnext(node.left,leftright)
                rightright = None
                if node.next:
                    rightright = node.next.left
                setnext(node.right,rightright)
        setnext(root,None)
        return root

#attempt2: BFS
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        curlevel = deque([root])
        while(curlevel):
            nextlevel = deque([])
            while(curlevel):
                curtop = curlevel.popleft()
                curtop.next = curlevel[0] if curlevel else None
                if curtop.left:
                    nextlevel.append(curtop.left)
                    if curtop.right:
                        nextlevel.append(curtop.right)
            curlevel = nextlevel
        return root

#attempt1: WA at lower levels, the right of a left node should point to left of
#the right node
'''
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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def setnext(node,rightnode):
            if node:
                print(node.val,node,rightnode)
                node.next = rightnode
                leftright = None
                if node.right:
                    leftright = node.right
                setnext(node.left,leftright)
                setnext(node.right,None)
        setnext(root,None)
        return root
'''
