#attempt2: 38ms
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        curlevel = [(root)]
        while(curlevel):
            nextlevel = []
            xpres = 0
            ypres = 0
            for node in curlevel:
                l,r = 0,0
                if node.left:
                    l=1
                    if node.left.val == x:
                        xpres = 1
                    if node.left.val == y:
                        ypres = 1
                    nextlevel.append(node.left)
                if node.right:
                    r=1
                    if node.right.val == x:
                        xpres = 1
                    if node.right.val == y:
                        ypres = 1
                    nextlevel.append(node.right)
                if l and r and {node.left.val,node.right.val}=={x,y}:
                    return False
            if xpres and ypres:
                return True
            curlevel = nextlevel.copy()
        return False
'''

#attempt1: 26ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        curlevel = [(root,0)]
        while(curlevel):
            nextlevel = []
            xpres = 0
            ypres = 0
            for node,level in curlevel:
                l,r = 0,0
                if node.left:
                    l=1
                    if node.left.val == x:
                        xpres = 1
                    if node.left.val == y:
                        ypres = 1
                    nextlevel.append((node.left,level+1))
                if node.right:
                    r=1
                    if node.right.val == x:
                        xpres = 1
                    if node.right.val == y:
                        ypres = 1
                    nextlevel.append((node.right,level+1))
                if l and r and {node.left.val,node.right.val}=={x,y}:
                    return False
            if xpres and ypres:
                return True
            curlevel = nextlevel.copy()
        return False