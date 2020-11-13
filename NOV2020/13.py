"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
#attempt2: 80%
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not(root):
            return root
        curlevel=[root]
        while(curlevel):
            nextlevel=[]
            curlevel=[i for i in curlevel if i]
            if curlevel:
                curlevel[-1].next=None
            for i in range(len(curlevel)-1):
                curlevel[i].next=curlevel[i+1]
                nextlevel.append(curlevel[i].left)
                nextlevel.append(curlevel[i].right)
            if curlevel and curlevel[-1]:
                nextlevel.append(curlevel[-1].left)
                nextlevel.append(curlevel[-1].right)
            curlevel=nextlevel
        return root
"""
#attempt1: WA actual attempt2->had lot of work,didnt try to solve
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not(root):
            return root
        def makecon(root,conn=None):
            if root:
                root.next=conn
                if not(root.left):
                    return
                makecon(root.left,root.right)
                if not(root.right):
                    return
                makecon(root.right,root.right.next)
                if root.left.right and root.right.left:
                    root.left.right.next=root.right.left
            else:
                return
        makecon(root)
        return root
"""
