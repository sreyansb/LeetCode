#attempt1: BFS
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        ans=[]
        if not(root):
            return []
        curlevel=[root]
        while(curlevel):
            newlevel=[]
            curans=[]
            for i in curlevel:
                curans.append(i.val)
                for child in i.children:
                    newlevel.append(child)
            ans.append(curans.copy())
            curlevel=newlevel.copy()
        return ans
                
        