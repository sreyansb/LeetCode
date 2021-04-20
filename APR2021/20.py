#attempt2: ITERATIVE APPROACH: push a node into and push right and left children
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not(root):
            return []
        ans=[]
        stack=[root]
        while(stack):
            node=stack.pop()
            ans.append(node.val)
            stack+=node.children[::-1]
        return ans

#attempt1:
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans=[]
        def preorder(node):
            if node:
                ans.append(node.val)
                for i in node.children:
                    preorder(i)
        preorder(root)
        return ans
        
'''
